# Sign Language Interpreter
The following sign language interpreter was created using OpenCV using a live video feed from a camera.

### Libraries Used

* OpenCV
* NumPy
* Scikit-Learn
* Keras
* Pyttsx3
* h5py

### Architecture 

Below is the basic architecture used to create this sign language interpreter

* Data Collection: Collect a large dataset of sign language images, including different gestures, hand positions, and backgrounds. Each image should be labeled with the corresponding sign language gesture.
* Data Preprocessing: Use OpenCV to preprocess the images before feeding them into the CNN. Preprocessing steps may include resizing the images to a consistent size, converting them to grayscale, and applying normalization techniques.
* Hand Detection: Utilize OpenCV's image processing and computer vision capabilities to detect and locate the hands within the video frames or images. This can be achieved using techniques such as background subtraction, skin color detection, or advanced machine learning methods like Haar cascades or deep learning-based models.
* ROI Extraction: After detecting hands, extract the region of interest (ROI) containing the hand from the image or video frame. This helps isolate the hand gesture for further processing.
* CNN Architecture: Use a deep learning library (e.g., TensorFlow, PyTorch) to design the CNN architecture. The architecture typically consists of multiple convolutional layers, pooling layers, and fully connected layers. The specific configuration and number of layers depend on the complexity of the sign language recognition task and the dataset.
* Training: Train the CNN using the preprocessed sign language dataset. Split the dataset into training and validation sets and use techniques like stochastic gradient descent (SGD) or Adam optimization algorithms to update the network's parameters (weights and biases) during the training process.
* Validation and Testing: Evaluate the trained model on a separate validation dataset to assess its performance and fine-tune hyperparameters if necessary. Once the model performs well on the validation set, test it on unseen data to measure its accuracy and generalization capabilities.
* Deployment: Deploy the trained CNN sign language interpreter by integrating it with OpenCV. Capture video frames using OpenCV, preprocess the frames, detect hands, extract the ROI, and feed it into the CNN model for gesture recognition. The model's output can then be used to interpret sign language gestures in real-time applications.

### Process
* Run Set_Hand.py to set the hand histogram for creating gestures.
* Next add gestures and label them by running Create_Gestures.py
* Create variations in data by using Rotate_Images.py
* Next run Load_Images.py to develop training and test sets
* To see and verify the gestures that were created run Display_Gestures.py
* Now it is time to train our model by running CNN_Model.py
* Now use Main.py to open the window on your computer and test how well your Sign Language Interpreter is. 

