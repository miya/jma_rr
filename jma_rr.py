import os
import glob
import dropbox
import requests
from PIL import Image
from multiprocessing import Pool
from datetime import datetime, timedelta, timezone

'''時間データをセットするメソッド
降水画像データをダウンロードするためのURLにセットする時間データを生成します。
'''
def get_timeData():
    time1 = datetime.now(jst) - timedelta(days=(1))
    time2 = datetime(year=time1.year, month=time1.month, day=time1.day)
    time3 = [(time2 + timedelta(minutes=(5*i))).strftime('%Y%m%d%H%M') for i in range(288)]
    return time3

'''画像取得メソッド
気象庁のレーダー・ナウキャスト(https://www.jma.go.jp/jp/radnowc/)にアクセスし、前日の1日分の観測画像(5分毎にアップロードされるので5*12=288)をダウンロードします。
ダウンロードはmultiprocessingを使い並行処理で行います。
`'''
def get_image(timeData):
    url = 'http://www.jma.go.jp/jp/radnowc/imgs/radar/000/{}-00.png'.format(timeData)
    r = requests.get(url)
    if r.status_code == 200:
        with open(timeData + '.png', "wb") as w:
            w.write(r.content)

'''gif作成メソッド
画像取得メソッドでダウンロードした画像をPillowを使いgifを作成します。
gif作成後使用した画像は全て削除します。
'''
def make_gif():
    fname = (datetime.now(jst) - timedelta(days=1)).strftime('%Y-%m-%d') + '.gif'
    files = sorted(glob.glob('*.png'))
    images = [Image.open(i) for i in files]
    images[0].save(fname, save_all=True, append_images=images[1:], duration=50, loop=0)
    [os.remove(f) for f in files]
    print('[complete] make_gif')

'''Dropboxに保存するためのメソッド
作成したgifをDropboxに保存します。
予めDropboxAPI(https://www.dropbox.com/developers/apps/create)にて作成したアクセストークンをTravisCIのEnvironmentVariablesに登録します。
'''
def send_dropbox():
    access_token = os.environ.get('DROPBOX_ACCESS_TOKEN')
    dbx = dropbox.Dropbox(access_token)
    with open(file_name, 'rb') as f:
        dbx.files_upload(f.read(), '/' + file_name)
    print('[complete] send_dropbox')

'''メイン処理
TravisCIのタイムゾーンがUTCなのでJSTに変更。
'''
if __name__ == '__main__':
    jst = timezone(timedelta(hours=+9), 'JST')
    timeData = get_timeData()
    with Pool(processes=3) as p:
        p.map(get_image, timeData)
    print('[complete] get_image')
    make_gif()
    send_dropbox()
