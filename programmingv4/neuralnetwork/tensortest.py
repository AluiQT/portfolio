import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

#Create layer


#Weights - use a small range of values with a median close to 0 such as -0.5 to 0.5
#Weight matrix = weight x node etc 4 x 5 




#Epoch

#Weights - use a small range of values with a median close to 0 such as -0.5 to 0.5
#Weight matrix = weight x node etc 4 x 5

#Initial bias should be 0

#To train on all values increase the weights in the code (20,784)

#Initialize dataset with images, labels = dataset

#One Hot Label Encoded

#Sigmoid function activation

#Mean squared error? 

#Backpropagation