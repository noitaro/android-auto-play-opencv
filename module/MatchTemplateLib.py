import cv2 # pip install opencv-python
import numpy

class MatchTemplateLib():
    
    img = None
    temp = None
    loc = []
    minVal = 0
    maxVal = 0
    minLoc = []
    maxLoc = []
    
    #類似度の設定(0~1)
    threshold = 0.8
    
    def matchTemplate(self, _img, _temp):
        self.img = cv2.imread(_img, 0)
        self.temp = cv2.imread(_temp, 0)
        # テンプレートマッチング
        match_result = cv2.matchTemplate(self.img, self.temp, cv2.TM_CCOEFF_NORMED)

        #検出結果から検出領域の位置を取得
        self.loc = numpy.where(match_result >= self.threshold)
        
        # 最も類似度が高い位置と低い位置を取得します
        self.minVal, self.maxVal, self.minLoc, self.maxLoc = cv2.minMaxLoc(match_result)

    def matchTemplate2(self, _img, _temp):
        self.img = cv2.imdecode(numpy.frombuffer(_img, numpy.uint8), 0)
        self.temp = cv2.imread(_temp, 0)
        # テンプレートマッチング
        match_result = cv2.matchTemplate(self.img, self.temp, cv2.TM_CCOEFF_NORMED)

        #検出結果から検出領域の位置を取得
        self.loc = numpy.where(match_result >= self.threshold)
        
        # 最も類似度が高い位置と低い位置を取得します
        self.minVal, self.maxVal, self.minLoc, self.maxLoc = cv2.minMaxLoc(match_result)

    def judgeMatching(self):
        if self.threshold < self.maxVal:
            return True
        else:
            return False

    def getCenterPos(self):
        w, h = self.temp.shape[::-1]
        for top_left in zip(*self.loc[::-1]):
            return (top_left[0] + (w /2), top_left[1] + (h / 2))

    def rectImgwrite(self, _writePath):
        # 検出領域を四角で囲んで保存
        w, h = self.temp.shape[::-1]
        for top_left in zip(*self.loc[::-1]):
            bottom_right = (top_left[0] + w, top_left[1] + h)

        # 保存
        cv2.rectangle(result, top_left, bottom_right, (255, 0, 0), 10)
        cv2.imwrite(_writePath, self.img)

    def rawToOpenCVImg(self, raw):
        # wigth, heightを取得。
        wigth = int.from_bytes(raw[0:4], 'little')
        height = int.from_bytes(raw[4:8], 'little')
        _ = int.from_bytes(raw[8:12], 'little')

        # ここのCopyは必須。そうでないと、編集が出来ない
        tmp = numpy.frombuffer(raw[12:], numpy.uint8, -1, 0).copy() 

        # 配列の形状変換。
        # 1つの要素がRGBAである、height * widthの行列を作る。
        img = numpy.reshape(tmp, (height, wigth, 4))    

        # 要素入れ替え。
        # RawDataはRGB、OpenCVはBGRなので、0番目の要素と、2番目の要素を入れ替える必要がある。
        b = img[:, :, 0].copy()               # ここのコピーも必須
        img[:, :, 0] = img[:, :, 2] 
        img[:, :, 2] = b

        # alpha値を削除。alpha値が必要な場合は、下記行は消しても良いかも？
        img2 = numpy.delete(img, 3, 2)

        return img2