import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.load_model('best_model.h5')

img_path = 'path_to_image.jpg'
img = image.load_img(img_path, target_size=(48, 48))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

predictions = model.predict(img_array)
predicted_class = np.argmax(predictions)

print(f'Predicted class: {predicted_class}')

plt.imshow(img)
plt.title(f'Predicted Class: {predicted_class}')
plt.show()
