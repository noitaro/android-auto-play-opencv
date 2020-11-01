from module import Adblib as adb
from module import MatchTemplateLib as mt
from module import Winlib as win
from time import sleep

class AapoManager:

    adbl = None
    mtl = None
    screencap = []

    # コンストラクタ
    def __init__(self, _adbpath):
        self.adbl = adb.Adblib(_adbpath)
        if self.adbl.device == '':
            win.Winlib().MessageBox("アンドロイド端末が接続されていません。")
            exit()
        
        # インスタンス生成
        self.mtl = mt.MatchTemplateLib()

    def start(self, _package):
        self.adbl.start(_package)

    def end(self, _package):
        self.adbl.end(_package)
        win.Winlib().MessageBox("アプリを終了しました。")

    def sleep(self, _secs):
        sleep(_secs)

    def screencap(self):
        # 画面キャプチャ
        print(' 画面キャプチャ')
        self.adbl.screencap()

    def chkImg(self, _temp):
        # 曖昧画像検索
        self.mtl.matchTemplate2(self.adbl.screenImg , _temp)
        
        # 類似度閾値超え判定
        result = self.mtl.judgeMatching()
        if result:
            return True
        else:
            return False

    def touchImg(self, _temp):
        result = self.chkImg(_temp)
        if result == False:
            return False
        
        # 中央位置取得
        cPos = self.mtl.getCenterPos()
        if cPos is None:
            return False
        else:
            # タッチ
            self.adbl.touch(cPos[0], cPos[1])
            print('タッチ: x=' + str(cPos[0]) + ', y=' + str(cPos[1]) + ', img=' + _temp)
            return True

    def touchPos(self, _x, _y):
        self.adbl.touch(_x, _y)
        print('タッチ: x=' + str(_x) + ', y=' + str(_y))

    def longTouchPos(self, _x, _y, _msec):
        self.adbl.longTouch(_x, _y, _msec)
        print('ロングタッチ: x=' + str(_x) + ', y=' + str(_y))

    def swipeTouchPos(self, _x1, _y1, _x2, _y2, _msec):
        self.adbl.swipeTouch(_x1, _y1, _x2, _y2, _msec)
        print('スワイプ: x1=' + str(_x1) + ', y1=' + str(_y1) + ', x2=' + str(_x2) + ', y2=' + str(_y2))

    def inputtext(self, _message):
        self.adbl.inputtext(_message)

    def inputkeyevent(self, _keyevent):
        self.adbl.inputkeyevent(_keyevent)

            