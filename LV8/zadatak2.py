from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

model = load_model('best_model.h5')

img = image.load_img('test.png', target_size=(28, 28), color_mode='grayscale')
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array.astype('float32') / 255.0

pred = model.predict(img_array)
pred_class = np.argmax(pred)

plt.imshow(img, cmap='gray')
plt.title(f'Predicted: {pred_class}')
plt.show()
