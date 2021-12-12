import subprocess

class Adblib:
    
    adbpath = ''
    device = ''
    screenImg = []
    devices = []

    # コンストラクタ（引数なし）
    def __init__(self):
        pass

    # コンストラクタ
    def __init__(self, _adbpath):
        self.adbpath = _adbpath

        try:
            results = subprocess.check_output([self.adbpath + 'adb', 'devices'])
        except FileNotFoundError:
            print('adb.exe が見つかりません。（' + self.adbpath + 'adb.exe' + '）')
            exit()

        # バイト列を文字列に変換
        results = str(results, 'utf-8')
        # 文字列を分割
        self.devices = results.splitlines()
        if len(self.devices) <= 2:
            return
        # 先頭行を削除（不要なメッセージのため）
        self.devices.pop(0)
        # とりあえず先頭のデバイスを設定（後で変更もできる）
        self.setdevice(self.devices[0])
    
    def setdevice(self, _devise):
        self.device = _devise.split()[0]
        print(self.device)

    def inputtext(self, _message):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'text', _message])

    def inputkeyevent(self, _keyevent):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'keyevent', str(_keyevent)])

    def touch(self, _x, _y):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'touchscreen', 'tap', str(_x), str(_y)])

    def longTouch(self, _x, _y, _msec):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'touchscreen', 'swipe', str(_x), str(_y), str(_x), str(_y), str(_msec)])

    def swipeTouch(self, _x1, _y1, _x2, _y2, _msec):
        subprocess.call([self.adbpath + 'adb', '-s', self.device, 'shell', 'input', 'touchscreen', 'swipe', str(_x1), str(_y1), str(_x2), str(_y2), str(_msec)])

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
