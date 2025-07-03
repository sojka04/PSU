import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np
from sklearn.metrics import confusion_matrix

# Prilagodite putanju prema stvarnom smještaju direktorija "dataset"
train_ds = image_dataset_from_directory(
    directory=r'C:\Users\student\Desktop\dataset\train',  # Prilagodite putanju prema stvarnom direktoriju
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    subset="training",
    seed=123,
    validation_split=0.2,
    image_size=(48, 48)
)

validation_ds = image_dataset_from_directory(
    directory=r'C:\Users\student\Desktop\dataset\train',  # Prilagodite putanju prema stvarnom direktoriju
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    subset="validation",
    seed=123,
    validation_split=0.2,
    image_size=(48, 48)
)

test_ds = image_dataset_from_directory(
    directory=r'C:\Users\student\Desktop\dataset\test',  # Prilagodite putanju prema stvarnom direktoriju
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48)
)

model = models.Sequential([
    layers.InputLayer(input_shape=(48, 48, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(43, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True, monitor='val_loss', mode='min', verbose=1)
tensorboard = TensorBoard(log_dir='logs')

history = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=20,
    callbacks=[checkpoint, tensorboard]
)

test_loss, test_acc = model.evaluate(test_ds)
print(f'Test Accuracy: {test_acc}')

y_pred = np.argmax(model.predict(test_ds), axis=-1)
y_true = np.argmax(test_ds.labels, axis=-1)

cm = confusion_matrix(y_true, y_pred)
print('Confusion Matrix:\n', cm)
