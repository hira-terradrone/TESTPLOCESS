import os
import time


def CreateF(list_create_file):
    for i, create_file in enumerate(list_create_file):
        f = open(os.path.join(os.getcwd(), "temp/", create_file), 'w')
        f.write(F'i = {i}')  # 何も書き込まなくてファイルは作成されました
        # ダウンロードに時間がかかっていると想定
        time.sleep(1.0)
        f.close()
        # ダウンロード済みのファイルには"Done_"を付ける
        os.rename(os.path.join(os.getcwd(), "temp/", create_file),
            os.path.join(os.getcwd(), "temp/",F"Done_{create_file}"))