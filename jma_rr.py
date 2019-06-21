import os
import glob
import dropbox
import requests
from PIL import Image
from io import BytesIO
from multiprocessing import Pool
from datetime import datetime, timedelta, timezone

'''時間データをセットするメソッド
降水画像データをダウンロードするためのURLにセットする時間データを生成します。
'''
def getTime():
    time1 = datetime.now(jst) - timedelta(days=(1))
    time2 = datetime(year=time1.year, month=time1.month, day=time1.day)
    time3 = [(time2 + timedelta(minutes=(5*i))).strftime('%Y%m%d%H%M') for i in range(288)]
    return time3

'''画像取得メソッド
気象庁のレーダー・ナウキャスト(https://www.jma.go.jp/jp/radnowc/)にアクセスし、前日の1日分の観測画像(5分毎にアップロードされるので5*12=288)をダウンロードします。
ダウンロードはmultiprocessingを使い並行処理で行います。
`'''
def getImg(time):
    url = 'http://www.jma.go.jp/jp/radnowc/imgs/radar/000/{}-00.png'.format(time)
    req = requests.get(url)
    if req.status_code == 200:
        img = BytesIO(req.content)
        return img

'''Dropboxに保存するためのメソッド
作成したgifをDropboxに保存します。
予めDropboxAPI(https://www.dropbox.com/developers/apps/create)にて作成したアクセストークンをTravisCIのEnvironmentVariablesに登録します。
'''
def sendDropbox():
    access_token = os.environ.get('DROPBOX_ACCESS_TOKEN')
    dbx = dropbox.Dropbox(access_token)
    with open(fname, 'rb') as f:
        dbx.files_upload(f.read(), '/' + fname)

'''メイン処理
TravisCIのタイムゾーンがUTCなのでJSTに変更。
'''
if __name__ == '__main__':
    jst = timezone(timedelta(hours=+9), 'JST')
    time = getTime()
    with Pool(processes=3) as p:
        img = p.map(getImg, time)
    print('[success] get images')
    img_result = [Image.open(i) for i in img]
    fname = (datetime.now(jst) - timedelta(days=1)).strftime('%Y-%m-%d') + '.gif'
    img_result[0].save(fname, save_all=True, append_images=img_result[1:], duration=50, loop=0)
    print('[success] create gif' )
    sendDropbox()
    print('[success] send dropbox')
