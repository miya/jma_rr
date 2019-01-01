import os
import dropbox

FILE_NAME  = 'test.png'

def send_db():
    access_token = os.environ.get('DROPBOX_ACCESS_TOKEN')
    dbx = dropbox.Dropbox(access_token)
    with open(FILE_NAME, 'rb') as f:
        dbx.files_upload(f.read(), '/' + FILE_NAME)
    print('[complete] save_dropbox')

send_db()
