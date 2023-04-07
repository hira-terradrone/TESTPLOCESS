import multiprocessing
from mUpload import SendF
from mDownload import CreateF

def Do():
    # アップロード先のパス
    s3_path_list = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt", "6.txt"]
    dic = dict(zip(map(str,range(len(s3_path_list))),s3_path_list))
    
    # アップロードプログラム(tempフォルダに投げ込まれたファイルをアップロードしていく)(非同期処理で起動しておく)
    process = multiprocessing.Process(target=SendF, kwargs=(dic), daemon=False)
    process.start()

    # ダウンロードプログラム(tempフォルダーにファイルをダウンロードする)
    CreateF(s3_path_list)

if __name__ == '__main__':
    Do()