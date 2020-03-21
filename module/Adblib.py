import subprocess
import math

class Adblib:
    
    adbpath = ''
    device = ''
    screenImg = []

    # コンストラクタ
    def __init__(self, _adbpath):
        self.adbpath = _adbpath
    
        results = subprocess.check_output([self.adbpath + 'adb', 'devices'])
        # バイト列を文字列に変換
        results = str(results, 'utf-8')
        # 文字列を分割
        devices = results.splitlines()
        if len(devices) <= 2:
            return
        self.device = devices[1].split()[0]
        print(self.device)

    def inputtext(self, _message):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'text', _message])

    def inputkeyevent(self, _keyevent):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'keyevent', str(_keyevent)])

    def touch(self, _x, _y):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'touchscreen', 'tap', str(_x), str(_y)])

    def longTouch(self, _x, _y, _msec):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'touchscreen', 'swipe', str(_x), str(_y), str(_x), str(_y), str(_msec)])

    def screencap(self):
        # 画面キャプチャ
        self.screenImg = subprocess.check_output([self.adbpath + 'adb', '-s', self.device, 'exec-out', 'screencap', '-p'])

    def kill(self):
        subprocess.call([self.adbpath + 'adb', 'kill-server'])

    def start(self, _package):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'am', 'start', '-n', _package])

    def end(self, _package):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'am', 'force-stop', _package])

    def clear(self, _package):
        # キャッシュ削除
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'pm', 'clear', _package])
