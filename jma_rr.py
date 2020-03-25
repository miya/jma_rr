import os
import dropbox
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime, timedelta, timezone

def get_time():
    time1 = datetime.now(jst) - timedelta(days=1)
    time2 = datetime(year=time1.year, month=time1.month, day=time1.day)
    time3 = [(time2 + timedelta(minutes=(5*i))).strftime("%Y%m%d%H%M") for i in range(288)]
    return time3

def get_img(time):
    url = "http://www.jma.go.jp/jp/radnowc/imgs/radar/000/{}-00.png".format(time)
    req = requests.get(url)
    if req.status_code == 200:
        img = BytesIO(req.content)
        return img

def create_gif():
    img_result = [Image.open(i) for i in imgs]
    img_result[0].save(fname, save_all=True, append_images=img_result[1:], duration=50, loop=0)

def send_dropbox():
    access_token = os.environ.get("DROPBOX_ACCESS_TOKEN")
    dbx = dropbox.Dropbox(access_token)
    with open(fname, "rb") as f:
        dbx.files_upload(f.read(), "/" + fname)


if __name__ == "__main__":

    jst = timezone(timedelta(hours=+9), "JST")
    fname = (datetime.now(jst) - timedelta(days=1)).strftime("%Y-%m-%d") + ".gif"

    # 画像データのタイムスタンプを生成
    times = get_time()

    # タイムスタンプからURLを生成、リクエストを送りバイナリデータを取得してbytesIOに渡し画像オブジェクトを返す
    imgs = [get_img(time) for time in times]
    print("[success] get images")

    # gifファイルの生成
    create_gif()
    print("[success] create gif")

    # 生成されたgifファイルをDropBoxに送信する
    send_dropbox()
    print("[success] send Dropbox")
