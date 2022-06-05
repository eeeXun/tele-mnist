from flask import Flask, request
import numpy as np
import keras
import cv2
from PIL import Image, ImageOps


class Mnist:
    def __init__(self):
        self.model = keras.models.load_model("model.h5")

    def img_split(self, img):
        result = []
        img = cv2.imdecode(np.frombuffer(img, np.uint8), -1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        cnts = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        pos_list = []
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            pos_list.append([x, y, w, h])
        pos_list.sort(key=lambda s: s[0])
        for i in pos_list:
            x, y, w, h = i
            digit = thresh[y:y+h, x:x+w]
            # border expand
            im_type = Image.fromarray(digit)
            img_with_border = ImageOps.expand(im_type, border=10, fill='black')
            digit = np.array(img_with_border)
            # resize
            digit = (cv2.resize(digit, (28, 28)))
            # normalize
            digit = digit.astype("float32") / 255.0
            digit = np.expand_dims(digit, axis=0)
            result.append(digit)

        return result

    def predict(self, img):
        result = ""
        proc_imgs = self.img_split(img)
        for proc_img in proc_imgs:
            result += str(np.argmax(self.model.predict(proc_img)[0]))

        return result


app = Flask(__name__)
mnist = Mnist()


@app.route("/", methods=["GET", "POST"])
def index():
    img = request.files["img"].read()
    return mnist.predict(img)


if __name__ == "__main__":
    app.debug = False
    app.run("0.0.0.0")
