from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Loading data from dataset.
train_data = np.load('dataset/train_data.npz')
test_data = np.load('dataset/test_data.npz')

train_inputs = train_data['inputs']
test_inputs = test_data['inputs']
image_height, image_width, channels = train_inputs.shape[1:]

# One-Hot encoding at the targets.
train_targets = np_utils.to_categorical( train_data['targets'] )
test_targets = np_utils.to_categorical( test_data['targets'] )
num_of_classes = train_targets.shape[1]

# Applying data augmentation to data.
train_generator = ImageDataGenerator(
    rescale=1.0/255,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1
)
test_generator = ImageDataGenerator(
    rescale=1.0/255
)

# Loading the model, without weights.
model = InceptionResNetV2(weights=None,
                          input_shape=(image_height, image_width, channels), classes=num_of_classes,
                          classifier_activation='softmax')

model.compile( optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'] )

# Setting Early-Stopping method for the model.
checkpoint = ModelCheckpoint(filepath='inception_resnetv2_callback_weights.h5',
                             monitor='val_loss',
                             mode='min',
                             save_best_only=True,
                             verbose=1)
early_stopping = EarlyStopping(monitor='val_loss',
                               min_delta=0,
                               patience=9,
                               verbose=1,
                               restore_best_weights=True)
callbacks = [checkpoint, early_stopping]

# Training parameters of the model.
batch_size = 64
epochs = 40

history = model.fit(
    train_generator.flow(x=train_inputs, y=train_targets, batch_size=batch_size),
    epochs=epochs, verbose=1, sample_weight=None, callbacks=callbacks,
    validation_data=test_generator.flow(x=test_inputs, y=test_targets, batch_size=batch_size)
)

# Testing model's accuracy.
test_metrics = model.evaluate(test_generator.flow(x=test_inputs, y=test_targets, batch_size=batch_size), verbose=0)
test_loss, test_accuracy = test_metrics[0], test_metrics[1]
print('Test Loss:', test_loss)
print('Test Accuracy:', test_accuracy)

# Plotting Training, Validation loss.
history_dict = history.history

train_loss = history_dict['loss']
valid_loss = history_dict['val_loss']
epoch_steps = range(1, len(train_loss)+1)
plt.plot(epoch_steps, train_loss, label='Training Loss')
plt.plot(epoch_steps, valid_loss, label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Saving the model.
model.save('inception_resnetv2_weights.h5')

# Saving the History.
pickle_file = open('inception_resnetv2_history.pickle', 'wb')
pickle.dump(history_dict, pickle_file)
pickle_file.close()