import requests,glob,datetime,os
from PIL import Image
from bs4 import BeautifulSoup as bs4


def get_image():
    time_data = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    for h in [str(i).zfill(2) for i in range(24)]:
        for m in [str(i*5).zfill(2) for i in range(12)]:
            time = time_data + h + m
            url = 'http://www.jma.go.jp/jp/radnowc/imgs/radar/000/' + time + '-00.png'
            req = requests.get(url)
            if req.status_code == 404:
                print('Error --> {}'.format(url))
            else:
                with open(time + '.png', "wb") as w:
                    w.write(req.content)
                    print('Downloaded --> {}'.format(url))
    print('[complete] get_image')


def make_gif():
    file_name = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d') + '.gif'
    files = sorted(glob.glob('./*.png'))
    images = list(map(lambda file: Image.open(file), files))
    images[0].save(file_name, save_all=True, append_images=images[1:], duration=50, loop=0)
    [os.remove(f) for f in glob.glob('*.png')]
    print('[complete] make_gif')


if __name__ == '__main__':
    get_image()
    make_gif()
    save_dropbox()



