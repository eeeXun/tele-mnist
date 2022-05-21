from PIL import Image, ImageOps
import numpy as np
import keras

img = Image.open("./pic.png").convert("L").resize((28, 28))
img = ImageOps.invert(img)
arr = np.array(img)
arr = arr.astype('float32') / 255.0
arr = np.expand_dims(arr, axis=0)

model = keras.models.load_model("model.h5")

print(np.argmax(model.predict(arr)[0]))
