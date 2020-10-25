# TSRD  Challenge

Chinese Traffic Sign Database (TSRD) is a traffic sign recognition dataset, which contains 58 different classes of traffic signs. The difficulty in this dataset is that:

1. Provides little data (images) for each class.
1. Images don't have a standard size.

More info about the dataset can be found here: http://www.nlpr.ia.ac.cn/pal/trafficdata/recognition.html

# Preprocessing

The first thing I've done is to resize all images from both the training and the validation dataset to a preferred Width x Height shape = (128, 128). In order to deal with
the small size of the dataset, I've applied the following data augmentation techniques to the training images:

1. Rescaling (Normalizing) all pixel values to a range between [0, 1].
1. Rotating images for 20 degrees.
1. Shifting the images both horizontally and vertically.
1. Zooming.
1. Shearing.

# Model & Training

For the training part, I used an Inception-ResnetV2 from keres.applications library. I included the top layers, but I didn't use any of the pre-trained weights, so
I trained the model from the beginning. At the output layer, I used a softmax activation function, because there are 58 different classes.

Then, I compiled the model using Adam Optimizer with initial learning rate = 0.001 and a Categorical Cross-Entropy loss. Then I started training the model for 40 epochs,
using the Early Stopping strategy.

# Results

Even though I haven't done enough things to increase the accuracy and prevent the overfitting of the model, the results are quite amazing. The model managed to achieve almost 95% accuracy, with a so small dataset and so little improvements.

    Epoch 00001: val_loss improved from inf to 5.62458, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 37s 558ms/step - loss: 1.4630 - accuracy: 0.6118 - val_loss: 5.6246 - val_accuracy: 0.0090
    Epoch 2/40
    66/66 [==============================] - ETA: 0s - loss: 0.4883 - accuracy: 0.8612
    Epoch 00002: val_loss improved from 5.62458 to 5.15087, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 509ms/step - loss: 0.4883 - accuracy: 0.8612 - val_loss: 5.1509 - val_accuracy: 0.0391
    Epoch 3/40
    66/66 [==============================] - ETA: 0s - loss: 0.2107 - accuracy: 0.9379
    Epoch 00003: val_loss did not improve from 5.15087
    66/66 [==============================] - 31s 476ms/step - loss: 0.2107 - accuracy: 0.9379 - val_loss: 5.5207 - val_accuracy: 0.0120
    Epoch 4/40
    66/66 [==============================] - ETA: 0s - loss: 0.1610 - accuracy: 0.9532
    Epoch 00004: val_loss improved from 5.15087 to 3.76962, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 33s 508ms/step - loss: 0.1610 - accuracy: 0.9532 - val_loss: 3.7696 - val_accuracy: 0.1805
    Epoch 5/40
    66/66 [==============================] - ETA: 0s - loss: 0.0508 - accuracy: 0.9856
    Epoch 00005: val_loss improved from 3.76962 to 2.04266, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 519ms/step - loss: 0.0508 - accuracy: 0.9856 - val_loss: 2.0427 - val_accuracy: 0.5055
    Epoch 6/40
    66/66 [==============================] - ETA: 0s - loss: 0.0229 - accuracy: 0.9933
    Epoch 00006: val_loss improved from 2.04266 to 1.24411, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 509ms/step - loss: 0.0229 - accuracy: 0.9933 - val_loss: 1.2441 - val_accuracy: 0.6630
    Epoch 7/40
    66/66 [==============================] - ETA: 0s - loss: 0.0140 - accuracy: 0.9971
    Epoch 00007: val_loss improved from 1.24411 to 0.87443, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 511ms/step - loss: 0.0140 - accuracy: 0.9971 - val_loss: 0.8744 - val_accuracy: 0.7633
    Epoch 8/40
    66/66 [==============================] - ETA: 0s - loss: 0.0197 - accuracy: 0.9954
    Epoch 00008: val_loss improved from 0.87443 to 0.73282, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 518ms/step - loss: 0.0197 - accuracy: 0.9954 - val_loss: 0.7328 - val_accuracy: 0.8024
    Epoch 9/40
    66/66 [==============================] - ETA: 0s - loss: 0.0770 - accuracy: 0.9803
    Epoch 00009: val_loss did not improve from 0.73282
    66/66 [==============================] - 32s 478ms/step - loss: 0.0770 - accuracy: 0.9803 - val_loss: 2.0376 - val_accuracy: 0.5787
    Epoch 10/40
    66/66 [==============================] - ETA: 0s - loss: 0.0739 - accuracy: 0.9763
    Epoch 00010: val_loss did not improve from 0.73282
    66/66 [==============================] - 32s 479ms/step - loss: 0.0739 - accuracy: 0.9763 - val_loss: 2.4293 - val_accuracy: 0.5998
    Epoch 11/40
    66/66 [==============================] - ETA: 0s - loss: 0.0223 - accuracy: 0.9947
    Epoch 00011: val_loss did not improve from 0.73282
    66/66 [==============================] - 32s 479ms/step - loss: 0.0223 - accuracy: 0.9947 - val_loss: 0.8490 - val_accuracy: 0.7854
    Epoch 12/40
    66/66 [==============================] - ETA: 0s - loss: 0.0073 - accuracy: 0.9990
    Epoch 00012: val_loss improved from 0.73282 to 0.61164, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 512ms/step - loss: 0.0073 - accuracy: 0.9990 - val_loss: 0.6116 - val_accuracy: 0.8506
    Epoch 13/40
    66/66 [==============================] - ETA: 0s - loss: 0.0193 - accuracy: 0.9964
    Epoch 00013: val_loss did not improve from 0.61164
    66/66 [==============================] - 32s 479ms/step - loss: 0.0193 - accuracy: 0.9964 - val_loss: 1.2260 - val_accuracy: 0.7382
    Epoch 14/40
    66/66 [==============================] - ETA: 0s - loss: 0.0071 - accuracy: 0.9976
    Epoch 00014: val_loss improved from 0.61164 to 0.47466, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 516ms/step - loss: 0.0071 - accuracy: 0.9976 - val_loss: 0.4747 - val_accuracy: 0.8756
    Epoch 15/40
    66/66 [==============================] - ETA: 0s - loss: 0.0107 - accuracy: 0.9969
    Epoch 00015: val_loss did not improve from 0.47466
    66/66 [==============================] - 32s 485ms/step - loss: 0.0107 - accuracy: 0.9969 - val_loss: 0.8147 - val_accuracy: 0.7974
    Epoch 16/40
    66/66 [==============================] - ETA: 0s - loss: 0.0089 - accuracy: 0.9969
    Epoch 00016: val_loss did not improve from 0.47466
    66/66 [==============================] - 32s 482ms/step - loss: 0.0089 - accuracy: 0.9969 - val_loss: 0.9357 - val_accuracy: 0.7854
    Epoch 17/40
    66/66 [==============================] - ETA: 0s - loss: 0.0040 - accuracy: 0.9990
    Epoch 00017: val_loss improved from 0.47466 to 0.39416, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 510ms/step - loss: 0.0040 - accuracy: 0.9990 - val_loss: 0.3942 - val_accuracy: 0.9037
    Epoch 18/40
    66/66 [==============================] - ETA: 0s - loss: 0.0078 - accuracy: 0.9983
    Epoch 00018: val_loss did not improve from 0.39416
    66/66 [==============================] - 32s 481ms/step - loss: 0.0078 - accuracy: 0.9983 - val_loss: 0.7130 - val_accuracy: 0.8315
    Epoch 19/40
    66/66 [==============================] - ETA: 0s - loss: 0.0096 - accuracy: 0.9974
    Epoch 00019: val_loss did not improve from 0.39416
    66/66 [==============================] - 32s 483ms/step - loss: 0.0096 - accuracy: 0.9974 - val_loss: 1.0416 - val_accuracy: 0.7874
    Epoch 20/40
    66/66 [==============================] - ETA: 0s - loss: 0.0459 - accuracy: 0.9873
    Epoch 00020: val_loss did not improve from 0.39416
    66/66 [==============================] - 32s 483ms/step - loss: 0.0459 - accuracy: 0.9873 - val_loss: 0.9300 - val_accuracy: 0.7894
    Epoch 21/40
    66/66 [==============================] - ETA: 0s - loss: 0.0128 - accuracy: 0.9966
    Epoch 00021: val_loss did not improve from 0.39416
    66/66 [==============================] - 32s 487ms/step - loss: 0.0128 - accuracy: 0.9966 - val_loss: 0.4901 - val_accuracy: 0.8756
    Epoch 22/40
    66/66 [==============================] - ETA: 0s - loss: 0.0157 - accuracy: 0.9952
    Epoch 00022: val_loss did not improve from 0.39416
    66/66 [==============================] - 32s 481ms/step - loss: 0.0157 - accuracy: 0.9952 - val_loss: 0.5568 - val_accuracy: 0.8596
    Epoch 23/40
    66/66 [==============================] - ETA: 0s - loss: 0.0111 - accuracy: 0.9966
    Epoch 00023: val_loss did not improve from 0.39416
    66/66 [==============================] - 32s 481ms/step - loss: 0.0111 - accuracy: 0.9966 - val_loss: 4.0564 - val_accuracy: 0.5005
    Epoch 24/40
    66/66 [==============================] - ETA: 0s - loss: 0.0116 - accuracy: 0.9969
    Epoch 00024: val_loss did not improve from 0.39416
    66/66 [==============================] - 32s 482ms/step - loss: 0.0116 - accuracy: 0.9969 - val_loss: 0.6308 - val_accuracy: 0.8606
    Epoch 25/40
    66/66 [==============================] - ETA: 0s - loss: 0.0249 - accuracy: 0.9945
    Epoch 00025: val_loss did not improve from 0.39416
    66/66 [==============================] - 32s 482ms/step - loss: 0.0249 - accuracy: 0.9945 - val_loss: 0.6043 - val_accuracy: 0.8626
    Epoch 26/40
    66/66 [==============================] - ETA: 0s - loss: 0.0017 - accuracy: 0.9995
    Epoch 00026: val_loss improved from 0.39416 to 0.34880, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 517ms/step - loss: 0.0017 - accuracy: 0.9995 - val_loss: 0.3488 - val_accuracy: 0.9107
    Epoch 27/40
    66/66 [==============================] - ETA: 0s - loss: 4.9262e-04 - accuracy: 1.0000
    Epoch 00027: val_loss improved from 0.34880 to 0.27867, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 517ms/step - loss: 4.9262e-04 - accuracy: 1.0000 - val_loss: 0.2787 - val_accuracy: 0.9218
    Epoch 28/40
    66/66 [==============================] - ETA: 0s - loss: 2.5028e-04 - accuracy: 1.0000
    Epoch 00028: val_loss improved from 0.27867 to 0.21768, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 516ms/step - loss: 2.5028e-04 - accuracy: 1.0000 - val_loss: 0.2177 - val_accuracy: 0.9378
    Epoch 29/40
    66/66 [==============================] - ETA: 0s - loss: 1.8780e-04 - accuracy: 1.0000
    Epoch 00029: val_loss improved from 0.21768 to 0.21504, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 511ms/step - loss: 1.8780e-04 - accuracy: 1.0000 - val_loss: 0.2150 - val_accuracy: 0.9348
    Epoch 30/40
    66/66 [==============================] - ETA: 0s - loss: 1.3438e-04 - accuracy: 1.0000
    Epoch 00030: val_loss improved from 0.21504 to 0.19943, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 511ms/step - loss: 1.3438e-04 - accuracy: 1.0000 - val_loss: 0.1994 - val_accuracy: 0.9398
    Epoch 31/40
    66/66 [==============================] - ETA: 0s - loss: 1.2473e-04 - accuracy: 1.0000
    Epoch 00031: val_loss improved from 0.19943 to 0.19765, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 35s 524ms/step - loss: 1.2473e-04 - accuracy: 1.0000 - val_loss: 0.1977 - val_accuracy: 0.9448
    Epoch 32/40
    66/66 [==============================] - ETA: 0s - loss: 1.1913e-04 - accuracy: 1.0000
    Epoch 00032: val_loss improved from 0.19765 to 0.19572, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 512ms/step - loss: 1.1913e-04 - accuracy: 1.0000 - val_loss: 0.1957 - val_accuracy: 0.9418
    Epoch 33/40
    66/66 [==============================] - ETA: 0s - loss: 9.6115e-05 - accuracy: 1.0000
    Epoch 00033: val_loss improved from 0.19572 to 0.19328, saving model to inception_resnetv2_callback_weights.h5
    66/66 [==============================] - 34s 515ms/step - loss: 9.6115e-05 - accuracy: 1.0000 - val_loss: 0.1933 - val_accuracy: 0.9398
    Epoch 34/40
    66/66 [==============================] - ETA: 0s - loss: 0.0010 - accuracy: 0.9995
    Epoch 00034: val_loss did not improve from 0.19328
    66/66 [==============================] - 32s 479ms/step - loss: 0.0010 - accuracy: 0.9995 - val_loss: 0.4704 - val_accuracy: 0.8917
    Epoch 35/40
    66/66 [==============================] - ETA: 0s - loss: 0.0040 - accuracy: 0.9990
    Epoch 00035: val_loss did not improve from 0.19328
    66/66 [==============================] - 32s 478ms/step - loss: 0.0040 - accuracy: 0.9990 - val_loss: 0.3863 - val_accuracy: 0.8917
    Epoch 36/40
    66/66 [==============================] - ETA: 0s - loss: 0.0049 - accuracy: 0.9988
    Epoch 00036: val_loss did not improve from 0.19328
    66/66 [==============================] - 32s 479ms/step - loss: 0.0049 - accuracy: 0.9988 - val_loss: 2.5954 - val_accuracy: 0.6810
    Epoch 37/40
    66/66 [==============================] - ETA: 0s - loss: 7.1156e-04 - accuracy: 1.0000
    Epoch 00037: val_loss did not improve from 0.19328
    66/66 [==============================] - 32s 479ms/step - loss: 7.1156e-04 - accuracy: 1.0000 - val_loss: 0.3377 - val_accuracy: 0.9178
    Epoch 38/40
    66/66 [==============================] - ETA: 0s - loss: 2.0008e-04 - accuracy: 1.0000
    Epoch 00038: val_loss did not improve from 0.19328
    66/66 [==============================] - 32s 479ms/step - loss: 2.0008e-04 - accuracy: 1.0000 - val_loss: 0.2798 - val_accuracy: 0.9268
    Epoch 39/40
    66/66 [==============================] - ETA: 0s - loss: 9.3544e-05 - accuracy: 1.0000
    Epoch 00039: val_loss did not improve from 0.19328
    66/66 [==============================] - 32s 480ms/step - loss: 9.3544e-05 - accuracy: 1.0000 - val_loss: 0.2566 - val_accuracy: 0.9328
    Epoch 40/40
    66/66 [==============================] - ETA: 0s - loss: 1.3938e-04 - accuracy: 1.0000
    Epoch 00040: val_loss did not improve from 0.19328
    66/66 [==============================] - 32s 479ms/step - loss: 1.3938e-04 - accuracy: 1.0000 - val_loss: 0.2404 - val_accuracy: 0.9398
    Test Loss: 0.24035021662712097
    Test Accuracy: 0.9398194551467896

# Training - Validation loss plot

[!Loss plot](https://github.com/kochlisGit/Traffic-Sign-Detection/blob/main/TSRD/loss_plot.png)
