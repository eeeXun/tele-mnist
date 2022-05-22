from flask import Flask, request
from PIL import Image, ImageOps
from io import BytesIO
import numpy as np
import keras


model = keras.models.load_model("model.h5")
app = Flask(__name__)


@app.route("/")
def index():
    img = request.files["img"].read()
    img = BytesIO(img)
    img = Image.open(img).convert("L").resize((28, 28))
    img = ImageOps.invert(img)
    img_arr = np.array(img)
    img_arr = img_arr.astype("float32") / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)
    result = np.argmax(model.predict(img_arr)[0])

    return "{}".format(result)


if __name__ == "__main__":
    app.debug = False
    app.run("0.0.0.0")
