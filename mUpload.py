import os
import glob
import shutil
import time


def SendF(*args, **kwargs):
    list_send_file = []
    print(kwargs)
    for value in kwargs.values():
        list_send_file.append(value)
    # 追加
    i_latest_number = 0
    i_time_out_number = 0
    d_sleep_time = 0.1
    temp_folder = os.path.join(os.getcwd(), "temp")
    print(F"{temp_folder}/Done_*.txt")
    while(True):
        try:
            # ダウンロードの完了しているファイルのみ引っ張ってくる
            files = glob.glob(
                F"{temp_folder}/Done_*.txt"
                )
            if(len(files) == 0):
                # 10秒間ダウンロード完了ファイルが増えなければ終了とさせる(タイムアウトとして)
                if(i_time_out_number > int(10 / d_sleep_time)):
                    break
                time.sleep(d_sleep_time)
                i_time_out_number+=1
            else:
                time.sleep(0.01)
                i_time_out_number = 0
                # ファイルを一枚ずつアップロードする
                for i, downloaded_file in enumerate(files):
                    print(downloaded_file)
                    # アップロードにかかる時間を想定
                    time.sleep(0.5)
                    os.rename(downloaded_file, os.path.join(os.getcwd(), "goal/",F"{list_send_file[i_latest_number]}"))
                    # アップロードしたファイル数を更新
                    i_latest_number+=1
                # 送るパスと送信したファイル数が同じになったら終了
                if(len(list_send_file) == i_latest_number):
                    break

        except Exception as e:
            print(e)
            print(type(e))