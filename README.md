# android-auto-play-opencv
OpenCV の画像認識を使って、Android を自動操作するライブラリです。

Android を操作する時に [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb "Android Debug Bridge (adb)  |  Android Developers") を使うので、マウスカーソルが奪われません。

NoxPlayer を操作することも出来ます。

## Readme
https://noitalog.tokyo/android-auto-play-opencv/

## Installation
このライブラリを使うには、[Android SDK Platform-Tools](https://developer.android.com/studio/releases/platform-tools "SDK Platform Tools release notes  |  Android Developers") に含まれる ```adb.exe``` が必要です。
```
pip install android-auto-play-opencv
```
OpenCV も同時にインストールされます。

## How to use
```python
# This Python file uses the following encoding: utf-8

# pip install android-auto-play-opencv
import android_auto_play_opencv as am

adbpath = '..\\platform-tools\\'

def main():

    aapo = am.AapoManager(adbpath)
    
    while True:
    
        # 画面キャプチャ
        aapo.screencap()
        
        # 早送りボタンは常にタップ
        if aapo.touchImg('./umamusume/hayaokuri.png'):
            # タップ出来たら待機
            aapo.sleep(1)
    
        # Google Playダイアログが出たら、キャンセルの位置をタップ
        elif aapo.chkImg('./umamusume/google-play.png'):
            aapo.touchPos(135, 630)
            aapo.sleep(1)

if __name__ == '__main__':
    main()
```

### 完成品
* [ウマ娘自動リセマラ周回](https://github.com/noitaro/python-umamusume)

## Reference

### start
アプリを起動する。
```python
# FGOを起動する.
aapo.start('com.aniplex.fategrandorder/jp.delightworks.Fgo.player.AndroidPlugin')
```

### end
アプリを終了する。
```python
# FGOを終了する.
aapo.end('com.aniplex.fategrandorder')
```

### sleep
処理を待機させる。
```python
# 5秒待機.
aapo.sleep(5)
```

### screencap
Android の画面をキャプチャする。
```python
# 画面キャプチャ
aapo.screencap()
```

### chkImg
[`screencap`](#screencap) で取得したスクリーンショットに、テンプレート画像があるか確認します。タップはしません。
```python
if aapo.chkImg('./template/stage_clear.png'):
    # あった時の処理.
    pass
```

### chkImg2
[`screencap`](#screencap) で取得したスクリーンショットに、テンプレート画像があるか確認します。タップはしません。見つけた座標も返してくれます。
```python
# 古龍の心臓 が見つかったら位置を戻す。
result, x, y = aapo.chkImg2('./template/koryunosinzo.png')
print('result=' + str(result) + ', x=' + str(x) + ', y=' + str(y))

if result:
    # 見つかった位置から指定ピクセルズラしてロングタップ(5秒)
    aapo.longTouchPos(x+50, y+50, 5000)
```

### touchImg
[`screencap`](#screencap) で取得したスクリーンショットに、テンプレート画像があればタップします。タップ結果を返してくれます。
```python
aapo.touchImg('./template/stage_clear.png')
```

### touchPos
指定位置をタップします。
```python
# X=750、Y=400 の位置をタップする.
aapo.touchPos(750, 400)
```
第3引数を指定すると、ロングタップします。
```python
# X=750、Y=400 の位置を5秒間タップする.
aapo.longTouchPos(750, 400, 5000)
```

### swipeTouchPos
指定位置をスワイプします。
```python
# X=750、Y=800 から、X=750、Y=400 まで、1秒かけてスワイプする.
aapo.swipeTouchPos(750, 800, 750, 400, 1000)
```

### inputtext
文字を入力します。
```python
# abc を入力する.
aapo.inputtext('abc')
```

### inputkeyevent
HOMEキーやバックキーを送ります。
```python
# ホームキーを押す.
aapo.inputkeyevent(3)
# バックキーを押す.
aapo.inputkeyevent(4)
```

### inputkeyevent
[`screencap`](#screencap) で取得したスクリーンショットを保存します。
```python
# キャプチャ画像を保存
aapo.imgSave('screenshot.png')

# 現在の日時でキャプチャ画像を保存
aapo.imgSave('img/screenshot_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.png')
# ↑をする場合「import datetime」をファイルの先頭に書くこと。
```

### デバイス選択
複数の端末で同時実行できます。
```python
import inquirer  # pip install inquirer
aapo = am.AapoManager('C:\\Program Files\\Nox\\bin\\')
devicesselect = [
    inquirer.List(
        "device",
        message="デバイスを選択して下さい。",
        choices=aapo.adbl.devices
    )
]
selected = inquirer.prompt(devicesselect)
aapo.adbl.setdevice(selected['device'])
aapo.screencap()
```
