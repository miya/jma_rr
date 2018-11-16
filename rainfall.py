import os
import glob
import datetime
import requests
from PIL import Image

def get_image():
    time1 = (datetime.datetime.now() - datetime.timedelta(days=(1)))
    time2 = datetime.datetime(year=time1.year, month=time1.month, day=time1.day)
    time3 = [(time2 + datetime.timedelta(minutes=(5*i))).strftime('%Y%m%d%H%M') for i in range(288)]
    for i in time3:
        url = 'http://www.jma.go.jp/jp/radnowc/imgs/radar/000/{}-00.png'.format(i)
        req = requests.get(url)
        if req.status_code == 200:
            with open(i + '.png', "wb") as w:
                w.write(req.content)
                print('Downloaded --> {}'.format(url))
        else:
            print('Error --> {}'.format(url))
    print('[complete] get_image')

def make_gif():
    file_name = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d') + '.gif'
    files = sorted(glob.glob('*.png'))
    images = [Image.open(i) for i in files]
    images[0].save(file_name, save_all=True, append_images=images[1:], duration=50, loop=0)
    [os.remove(f) for f in files]
    print('[complete] make_gif')

if __name__ == '__main__':
    get_image()
    make_gif()
