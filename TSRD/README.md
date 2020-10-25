# TSRD  Challenge

Chinese Traffic Sign Database (TSRD) is a traffic sign recognition dataset, which contains 58 different classes of traffic signs. The difficulty in this dataset is that:

1. Provides little data (images) for each class.
1. Images don't have a standard size.

# Preprocessing

The first thing I've done is to resize all images from both the training and the validation dataset to a preferred Width x Height shape = (128, 128). In order to deal with
the small size of the dataset, I've applied the following data augmentation techniques to the training images:

1. Rescaling (Normalizing) all pixel values to a range between [0, 1].
1. Rotating images for 20 degrees.
1. Shifting the images both horizontally and vertically.
1. Horizontal Flipping.
1. Zooming.
1. Shearing.

# Model & Training

For the training part, I used an Inception-ResnetV2 from keres.applications library. I included the top layers, but I didn't use any of the pre-trained weights, so
I trained the model from the beginning. At the output layer, I used a softmax activation function, because there are 58 different classes.

Then, I compiled the model using Adam Optimizer with initial learning rate = 0.001 and a Categorical Cross-Entropy loss.

# Results
