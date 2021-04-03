# This Python file uses the following encoding: utf-8

from module import AapoManager as am

adbpath = 'C:\\Program Files\\Nox\\bin\\'

def main():

    aapo = am.AapoManager(adbpath)

    while True:
        # 画面キャプチャ
        aapo.screencap()

        # ステージクリア
        if aapo.touchImg('./template/stage_clear.png'):
            aapo.sleep(3)
            # 確認
            aapo.touchPos(1150, 640)
            aapo.sleep(3)
            # 再挑戦
            aapo.touchPos(1180, 640)
            aapo.sleep(3)
            # 編成選択
            aapo.touchPos(1080, 640)
            aapo.sleep(3)
            # 急速回復
            aapo.touchPos(70, 540)
            aapo.sleep(3)
            # 確認
            aapo.touchPos(666, 485)
            aapo.sleep(3)
            # 挑戦
            aapo.touchPos(1140, 645)
            aapo.sleep(3)
            continue
        # 宝箱
        if aapo.touchImg('./template/treasure_box.png'):
            aapo.touchPos(1100, 400)
            aapo.touchPos(1150, 400)
            aapo.touchPos(1000, 400)
            aapo.touchPos(1050, 400)
            aapo.touchPos(900, 400)
            aapo.touchPos(950, 400)
            aapo.touchPos(800, 400)
            aapo.touchPos(850, 400)
            aapo.touchPos(700, 400)
            aapo.touchPos(750, 400)
            aapo.touchPos(600, 400)
            aapo.touchPos(650, 400)
            aapo.touchPos(500, 400)
            aapo.touchPos(550, 400)
            aapo.touchPos(400, 400)
            aapo.touchPos(300, 400)
            aapo.touchPos(350, 400)
            aapo.touchPos(450, 400)
            aapo.touchPos(250, 400)
            continue
        # マナ回復
        if aapo.touchImg('./template/manna_recovery.png'):
            aapo.touchPos(250, 170)
            aapo.touchPos(300, 170)
            aapo.touchPos(350, 170)
            aapo.touchPos(400, 170)
            aapo.touchPos(450, 170)
            aapo.touchPos(500, 170)
            aapo.touchPos(550, 170)
            aapo.touchPos(600, 170)
            aapo.touchPos(650, 170)
            aapo.touchPos(700, 170)
            aapo.touchPos(750, 170)
            aapo.touchPos(800, 170)
            aapo.touchPos(850, 170)
            aapo.touchPos(900, 170)
            aapo.touchPos(950, 170)
            aapo.touchPos(1000, 170)
            aapo.touchPos(1050, 170)
            aapo.touchPos(1100, 170)
            aapo.touchPos(1150, 170)
            continue
        # デスピノル
        if aapo.touchImg('./template/death_pino.png'):
            continue

if __name__ == '__main__':
    main()
