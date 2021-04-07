# This Python file uses the following encoding: utf-8
# 解像度 960x540 で作ってあるので、実行前にNoxの解像度を変更して下さい。

from module import AapoManager as am
import datetime

# adbpath = 'C:\\Program Files\\Nox\\bin\\'
adbpath = 'D:\\Program Files\\Nox64\\bin\\'
aapo = None

def main():

    global aapo
    aapo = am.AapoManager(adbpath)
    mode = 0 # モード0(リセット)
    folderName = ''
    stackCount = 0

    # スタート
    start()
    
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

        # アカウント連携ダイアログが出たら、後でするの位置をタップ
        elif aapo.chkImg('./umamusume/account.png'):
            aapo.touchPos(135, 630)
            aapo.sleep(1)

        # チュートリアルダイアログが出たら、スキップの位置をタップ
        elif aapo.chkImg('./umamusume/tutorial.png'):
            aapo.touchPos(270, 630)
            aapo.sleep(1)

        # トレーナー登録ダイアログが出たら、
        elif aapo.chkImg('./umamusume/trainer.png'):
            # トレーナー名入力の位置をタップ
            aapo.touchPos(405, 430)
            aapo.sleep(1)
            # abc と入力
            aapo.inputtext('abc')
            aapo.sleep(1)
            # トレーナー名入力の位置をタップ
            aapo.touchPos(270, 430)
            aapo.sleep(1)
            # 登録ボタンの位置をタップ1
            aapo.touchPos(270, 630)
            aapo.sleep(1)
            # 登録ボタンの位置をタップ2
            aapo.touchPos(270, 630)
            aapo.sleep(1)
            # OKボタンの位置をタップ
            aapo.touchPos(405, 630)
            aapo.sleep(1)

        # お知らせダイアログが出たら、閉じるの位置をタップ
        elif aapo.chkImg('./umamusume/osirase.png'):
            aapo.touchPos(270, 890)
            aapo.sleep(1)

        # メインストーリー開放ダイアログが出たら、閉じるの位置をタップ
        elif aapo.chkImg('./umamusume/main-story.png'):
            aapo.touchPos(270, 630)
            aapo.sleep(1)
    
        # ウマ娘ストーリー開放ダイアログが出たら、閉じるの位置をタップ
        elif aapo.chkImg('./umamusume/umamusume-story.png'):
            aapo.touchPos(270, 890)
            aapo.sleep(1)
    
        # ウマ娘詳細ダイアログが出たら、閉じるの位置をタップ
        elif aapo.chkImg('./umamusume/umamusume-syosai.png'):
            aapo.touchPos(270, 680)
            aapo.sleep(1)
    
        # プレゼントが届いている場合
        elif aapo.touchImg('./umamusume/present1.png'):
            # タップ出来たら待機
            aapo.sleep(1)
            # 一括受取の位置をタップ
            aapo.touchPos(405, 890)
            aapo.sleep(1)
            # 閉じるの位置をタップ1
            aapo.touchPos(270, 890)
            aapo.sleep(1)
            # 閉じるの位置をタップ2
            aapo.touchPos(135, 890)
            aapo.sleep(1)

        # プレゼントを受け取っている場合
        elif aapo.chkImg('./umamusume/present2.png'):
            # フォルダ名がカラの場合セット
            if len(folderName) == 0:
                folderName = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            # 実績ログが終わるまで10秒ほど待機（メニューボタンが隠れて押せないから）
            aapo.sleep(13)
            # メニューボタンの位置をタップ
            aapo.touchPos(490, 50)
            aapo.sleep(1)
            # データ連携の位置をタップ1
            aapo.touchPos(410, 640)
            aapo.sleep(1)
            # データ連携の位置をタップ2
            aapo.touchPos(405, 640)
            aapo.sleep(1)
            # 連携パスワードの位置をタップ
            aapo.touchPos(450, 550)
            aapo.sleep(1)
            # 設定の位置をタップ
            aapo.touchPos(405, 640)
            aapo.sleep(1)
            # 連携パスワード入力の位置をタップ
            aapo.touchPos(270, 405)
            aapo.sleep(1)
            # 1qazXSW2 と入力
            aapo.inputtext('1qazXSW2')
            aapo.sleep(1)
            # 確認入力の位置をタップ1
            aapo.touchPos(270, 505)
            aapo.sleep(1)
            # 確認入力の位置をタップ2
            aapo.touchPos(270, 505)
            aapo.sleep(1)
            # 1qazXSW2 と入力
            aapo.inputtext('1qazXSW2')
            aapo.sleep(1)
            # プライバシーポリシーの位置をタップ1
            aapo.touchPos(135, 620)
            aapo.sleep(1)
            # プライバシーポリシーの位置をタップ2
            aapo.touchPos(135, 620)
            aapo.sleep(1)
            # OKの位置をタップ
            aapo.touchPos(405, 680)
            aapo.sleep(1)
            # 画面キャプチャ
            aapo.screencap()
            # スクショを保存
            aapo.imgSave('gatya/' + folderName + '/screenshot_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.png')
            aapo.sleep(1)
            # 閉じるの位置をタップ
            aapo.touchPos(270, 630)
            aapo.sleep(3)
            # ガチャボタンの位置をタップ
            aapo.touchPos(480, 930)
            aapo.sleep(2)
            # サポートカードの位置をタップ
            # aapo.touchPos(460, 580)
            # aapo.sleep(1)
        
        # 10回引く！
        elif aapo.touchImg('./umamusume/10-kaihiku.png'):
            # タップ出来たら待機
            aapo.sleep(1)
            
        # ガチャを引く！
        elif aapo.touchImg('./umamusume/gatyahiku.png'):
            # タップ出来たら待機
            aapo.sleep(1)
            
        # ガチャ結果
        elif aapo.chkImg('./umamusume/gatya-kekka.png'):
            # フォルダ名がカラの場合セット
            if len(folderName) == 0:
                folderName = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            # スクショを保存
            aapo.imgSave('gatya/' + folderName + '/screenshot_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.png')
            aapo.sleep(1)
            # もう1回引くの位置をタップ
            aapo.touchPos(480, 890)
            aapo.sleep(1)

        # 購入するボタンが出たら、ガチャ終了
        elif aapo.chkImg('./umamusume/konyusuru.png'):
            # リセット
            reset()
            # スタート
            start()

            mode = 0 # モード0(リセット)
            folderName = ''

        # モードが0(リセット)の場合
        elif mode == 0:
            # ハンバーガーメニューボタンをタップ
            if aapo.touchImg('./umamusume/hanba-ga-menu.png'):
                # タップ出来たら待機
                aapo.sleep(1)
                # ユーザーデータ削除の位置をタップ1
                aapo.touchPos(270, 750)
                aapo.sleep(1)
                # ユーザーデータ削除の位置をタップ2
                aapo.touchPos(405, 630)
                aapo.sleep(1)
                # ユーザーデータ削除の位置をタップ3
                aapo.touchPos(405, 630)
                aapo.sleep(1)
                # 閉じるの位置をタップ
                aapo.touchPos(270, 630)
                aapo.sleep(1)
                # モードを1(チュートリアル)に変更
                mode = 1 

        # モードが1(チュートリアル)の場合
        elif mode == 1:
            # ロゴをタップ
            if aapo.touchImg('./umamusume/logo.png'):
                # タップ出来たら待機
                aapo.sleep(1)

            # 同意をタップ
            elif aapo.touchImg('./umamusume/doui.png'):
                # タップ出来たら待機
                aapo.sleep(1)

        # スタック対策
        if aapo.chkImg('./umamusume/stack.png'):
            aapo.sleep(1)
            stackCount = stackCount + 1
            if stackCount > 10:
                # リセット
                reset()
                # スタート
                start()
                
                mode = 0 # モード0(リセット)
                folderName = ''
                stackCount = 0
        else:
            stackCount = 0

def start():
    # アプリ起動
    aapo.start('jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity')
    aapo.sleep(10)
    return

def reset():
    # ホームキーを押す
    aapo.inputkeyevent(3)
    aapo.sleep(1)
    # タスクキーを押す
    aapo.inputkeyevent(187)
    aapo.sleep(1)
    # すべて消去の位置をタップ
    aapo.touchPos(700, 55)
    aapo.sleep(1)
    return

if __name__ == '__main__':
    main()
