import android_auto_play_opencv.Adblib as adb
import android_auto_play_opencv.MatchTemplateLib as mt
from time import sleep
import os

class AapoManager:

    adbl = None
    mtl = None

    # コンストラクタ
    def __init__(self, _adbpath=None):

        if _adbpath is not None:
            self.adbl = adb.Adblib(_adbpath)
            if self.adbl.device == '' or self.adbl.device == '*':
                print('アンドロイド端末が接続されていません。')
                exit()
            
        # インスタンス生成
        self.mtl = mt.MatchTemplateLib()

    def start(self, _package):
        self.adbl.start(_package)

    def end(self, _package):
        self.adbl.end(_package)
        print('アプリを終了しました。')

    def sleep(self, _secs):
        sleep(_secs)

    def screencap(self):
        """
        Android の画面をキャプチャします。
        """
        # 画面キャプチャ
        print('画面キャプチャ')
        self.adbl.screencap()

    def chkImg(self, _temp, _threshold=None):
        """
        テンプレート画像があるか確認します。タップはしません。
        """

        # 曖昧画像検索
        self.mtl.matchTemplate(self.adbl.screenImg , _temp, _threshold=_threshold)
        
        # 類似度閾値超え判定
        result = self.mtl.judgeMatching()
        if result:
            print('画像発見, img=' + _temp)
            return True
        else:
            return False

    def chkImg2(self, _temp, _screenshot=None, _multi=False, _threshold=None):
        """
        テンプレート画像があるか確認します。タップはしません。見つけた座標も返してくれます。
        引数1: テンプレート画像
        引数2: スクリーンショット画像（任意）
        """

        if _screenshot is None:
            # 曖昧画像検索
            self.mtl.matchTemplate(self.adbl.screenImg , _temp, _threshold=_threshold)
        else:
            self.mtl.matchTemplate(None , _temp, _screenshot, _threshold=_threshold)
        
        # 類似度閾値超え判定
        result = self.mtl.judgeMatching()


        if _multi:
            if result:
            
                # 複数の中央位置取得
                cPos = self.mtl.getCenterPosMulti()
                print(f'画像発見 {len(cPos)}件')
                return (True, cPos)
        
            else:
                return (False, None)

        else:
            if result:
                # 中央位置取得
                cPos = self.mtl.getCenterPos()
                print('画像発見, img=' + _temp + ', x=' + str(cPos[0]) + ', y=' + str(cPos[1]))
                return (True, cPos[0], cPos[1])
            else:
                return (False, 0, 0)


    def touchImg(self, _temp):
        """
        テンプレート画像があればタップします。タップ結果も返してくれます。
        """
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

    def imgSave(self, fileName):
        print('キャプチャ画像保存')

        # 保存先のフォルダを取得
        dirname = os.path.dirname(fileName)

        # フォルダが指定してあれば、作成
        if len(dirname) != 0: os.makedirs(dirname, exist_ok=True)
        
        # キャプチャ画像保存
        with open(fileName, mode='wb') as f:
            f.write(self.adbl.screenImg)


        

            