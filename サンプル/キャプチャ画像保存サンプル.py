# This Python file uses the following encoding: utf-8

# pip install android-auto-play-opencv
import android_auto_play_opencv as am
import datetime # 日時を取得するために必要

adbpath = 'C:\\Program Files\\Nox\\bin\\'

def main():
    aapo = am.AapoManager(adbpath)

    # 画面キャプチャ
    aapo.screencap()
    # キャプチャ画像を保存（フォルダ指定ナシ）
    aapo.imgSave('screenshot.png')

    while True:
        # 画面キャプチャ
        aapo.screencap()
        # 現在の日時でキャプチャ画像を保存
        aapo.imgSave('img/screenshot_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.png')

if __name__ == '__main__':
    main()
