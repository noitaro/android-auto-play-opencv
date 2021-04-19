# This Python file uses the following encoding: utf-8

# pip install android-auto-play-opencv
import android_auto_play_opencv as am

adbpath = 'C:\\Program Files\\Nox\\bin\\'


aapo = am.AapoManager(adbpath)

# 画面キャプチャ
aapo.screencap()

# 古龍の心臓 が見つかったら位置を戻す。
result, x, y = aapo.chkImg2('./template/koryunosinzo.png')
print('result=' + str(result) + ', x=' + str(x) + ', y=' + str(y))

if result:
    # 見つかった位置から指定ピクセルズラしてロングタップ(5秒)
    aapo.longTouchPos(x+50, y+50, 5000)
