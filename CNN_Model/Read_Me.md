# Convolutional Neural Networks (CNNs)
Convolutional Neural Networks (CNNs) are a class of neural networks commonly used in image and video recognition tasks. They are designed to automatically and adaptively learn spatial hierarchies of features from input data, which makes them particularly effective at processing images and other high-dimensional data.

The current Convolutional Neural Network (CNN) Model was built using Tensorflow and Keras.
The following flowchart was used to develope the model.
![image](https://user-images.githubusercontent.com/71196508/236646896-5a5fcc71-311e-44e0-9a88-d30efe084599.png)

The Main goal of developing this CNN model was to analyze the veracity of the data.
* Confidentiatlity
* Integrity
* Availability

### Key Components to developing the CNN Model: 
* Data Preparation
* Data Verification
* Create the Convolutional base
* Compiling the Model
* Model Verification

### Architecture
A typical CNN architecture consists of three types of layers:

Convolutional Layers: These layers apply convolutional filters to the input data in order to extract features. The filters slide over the input data, producing a feature map that highlights certain aspects of the data.

Pooling Layers: These layers reduce the size of the feature maps produced by the convolutional layers. They do this by sub-sampling the data, either by taking the average or maximum value in a certain area of the map.

Fully-Connected Layers: These layers connect every neuron in one layer to every neuron in the next layer, just like in a regular neural network. They are typically used towards the end of the network, when the input data has been processed sufficiently.

### Training
Training a CNN typically involves the following steps:

To develop the model the [CIFAR-10](https://www.tensorflow.org/datasets/catalog/cifar10) dataset was used. 
Note this model was trained on 30 epochs resulting in loss of 0.2437 with accuracy of 91.6%

* Data Preprocessing was performed to establish test and train values
* Labels were flattened
* Data was plotted
* Model was built using Conv2D, BatchNormalization, and MaxPooling2D
* Model was compiled and data plotted to determine accuracy

### Conclusion

The model was built using Python code, the TensorFlow framework, Keras, NumPy, and Matplolib libraries as well as the CIFAR-10 data set. 
The model was developed and trained for 30 epochs which resulted in the loss of 0.2437, the accuracy was 91.6%, the validation loss was 0.4385, and the validation accuracy was 86.7%.
To validate the veracity of the data further, several metrics were used such as loss, accuracy,  validation loss (val_loss), and validation accuracy (val_acc).  These metrics were used to determine if the model was performing optimally and not overfitting. After analyzing the data generated during each epoch the validation loss and validation accuracy verified that the model was performing optimally.  
