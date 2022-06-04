from flask import Flask, request
from PIL import Image, ImageOps
from io import BytesIO
import numpy as np
import keras


class Mnist:
    def __init__(self):
        self.model = keras.models.load_model("model.h5")

    def resize(self, img):
        img = BytesIO(img)
        img = Image.open(img).convert("L").resize((28, 28))
        img = ImageOps.invert(img)
        return img

    def normalize(self, img):
        img_arr = np.array(img)
        img_arr = img_arr.astype("float32") / 255.0
        img_arr = np.expand_dims(img_arr, axis=0)
        return img_arr

    def img_process(self, img):
        img = self.resize(img)
        return self.normalize(img)

    def predict(self, img):
        data = self.img_process(img)
        result = np.argmax(self.model.predict(data)[0])

        return str(result)


app = Flask(__name__)
mnist = Mnist()


@app.route("/", methods=["GET", "POST"])
def index():
    img = request.files["img"].read()
    return mnist.predict(img)


if __name__ == "__main__":
    app.debug = False
    app.run("0.0.0.0")
