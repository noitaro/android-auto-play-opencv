# This Python file uses the following encoding: utf-8

# pip install android-auto-play-opencv
import android_auto_play_opencv as am

adbpath = 'C:/Program Files/Nox/bin/'
package = 'com.aniplex.fategrandorder'
classname = 'jp.delightworks.Fgo.player.AndroidPlugin'

def main():
    aapo = am.AapoManager(adbpath)

    # FGO開始
    aapo.start(package + '/' + classname)

    while True:
        # 画面キャプチャ
        aapo.screencap()

        # データ更新開始
        if aapo.touchImg('./template/chk_StartDataUpdate_001.png'):
            pass
        # 画面をタッチしてください
        elif aapo.touchImg('./template/chk_ScreenTouch_001.png'):
            pass
        # タイトル画面
        elif aapo.touchImg('./template/chk_Title_001.png'):
            pass
        # 同意する
        elif aapo.touchImg('./template/chk_Agree_001.png'):
            pass
        # SKIP
        elif aapo.touchImg('./template/chk_Skip_001.png'):
            aapo.sleep(1)
            # はいの位置をタッチ
            aapo.touchPos(1235, 835)
        # SKIP
        elif aapo.touchImg('./template/chk_Skip_002.png'):
            aapo.sleep(1)
            # はいの位置をタッチ
            aapo.touchPos(1235, 835)
        # はい
        elif aapo.touchImg('./template/chk_Yes_001.png'):
            pass
        # Attack
        elif aapo.touchImg('./template/chk_Attack_001.png'):
            aapo.sleep(1)
            # 予備で1回多めにタッチ
            aapo.touchPos(615, 320)
            # 左から順にタッチ
            aapo.touchPos(195, 780)
            aapo.touchPos(580, 780)
            aapo.touchPos(965, 780)
        # 12文字まで入力可能です
        elif aapo.touchImg('./template/chk_InputText_001.png'):
            aapo.sleep(1)
            aapo.inputtext('a')
        # OK
        elif aapo.touchImg('./template/chk_OK_001.png'):
            pass
        # 決定
        elif aapo.touchImg('./template/chk_Decide_001.png'):
            pass

            

        

    # FGO終了
    # aapo.end(package)

    


if __name__ == '__main__':
    main()
