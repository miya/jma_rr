import os
import glob
import dropbox
import requests
import datetime
from tqdm import tqdm
from PIL import Image

def get_image():
    time1 = (datetime.datetime.now() - datetime.timedelta(days=(1)))
    time2 = datetime.datetime(year=time1.year, month=time1.month, day=time1.day)
    time3 = [(time2 + datetime.timedelta(minutes=(5*i))).strftime('%Y%m%d%H%M') for i in range(288)]
    for i in tqdm(range(288)):
        url = 'http://www.jma.go.jp/jp/radnowc/imgs/radar/000/{}-00.png'.format(time3[i])
        req = requests.get(url)
        with open(time3[i] + '.png', "wb") as w:
            w.write(req.content)
    print('[complete] get_image')

def make_gif():
    files = sorted(glob.glob('*.png'))
    images = [Image.open(i) for i in files]
    images[0].save(FILE_NAME, save_all=True, append_images=images[1:], duration=50, loop=0)
    [os.remove(f) for f in files]
    print('[complete] make_gif')

def send_dropbox():
    access_token = os.environ.get('DROPBOX_ACCESS_TOKEN')
    dbx = dropbox.Dropbox(access_token)
    with open(FILE_NAME, 'rb') as f:
        dbx.files_upload(f.read(), '/' + FILE_NAME)
    print('[complete] send_dropbox')

if __name__ == '__main__':
    FILE_NAME = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d') + '.gif'
    print('FILE_NAME:', FILE_NAME)
    get_image()
    make_gif()
    send_dropbox()
