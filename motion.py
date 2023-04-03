import numpy as np
import random
import matplotlib.pyplot as plt

class DiscountedAveragerator(object):
    """Discounted averagerator class"""
    def __init__(self, discount=0.96):
        self.discount = discount
        self.avg = 0.

    def add(self, x):
        """Add new value to the discounted average"""
        self.avg = self.discount * self.avg + (1 - self.discount) * x

class MotionDetection(object):
    """Motion detection class"""

    def __init__(self, num_sigmas=4., discount=0.96):
        """Initializes the motion detection object"""
        self.num_sigmas= num_sigmas
        self.discount = DiscountedAveragerator(discount)

    def detect_motion(self, img):
        """Detects motion"""
        # Add the new image to the discounted average
        self.discount.add(img)

        # Compute the upper and lower thresholds for detecting motion
        upper = self.discount.avg + self.num_sigmas * self.discount.std
        lower = self.discount.avg - self.num_sigmas * self.discount.std

        # Compute where motion has occurred
        motion = np.logical_or(img > upper, img < lower)
        motion = np.max(motion, axis=2)

        return motion

def detect_motion(image_list, num_sigmas=4., discount=0.96, min_pixels=500):
    """Detects motion in a list of images"""
    detector = MotionDetection(num_sigmas=num_sigmas, discount=discount)
    detected_motion = []
    for i, img in enumerate(image_list):
        motion = detector.detect_motion(img)
        if np.sum(motion) > min_pixels:
            detected_motion.append((i, motion))
    return detected_motion

def noisy_temp(noise=1., d=0.05):
    """Generates a noisy temperature signal"""
    t = -d
    while True:
        t += d
        yield 15. + 10. * np.sin(t) + noise * 2.  * (random.random() - 0.5)

def noisy_temp_with_outliers(noise=1., d=0.05, outlier_prob=0.02, outlier_size=10.):
    """Generates a noisy temperature signal with outliers"""
    t = -d
    while True:
        t += d
        x = 15. + 10. * np.sin(t) + noise * 2.  * (random.random() - 0.5)
        if random.random() < outlier_prob:
            x += outlier_size * 2. * (random.random() - 0.5)
        yield x

if __name__ == '__main__':
    # Generate a noisy temperature signal and detect motion in it
    temperature_stream = noisy_temp_with_outliers()
    temperature_list = [next(temperature_stream) for i in range(60)]
    motions = detect_motion(temperature_list, num_sigmas=2.)

    # Plot the motion detection results
    for i, m in motions:
        if np.sum(m) > 500:
            print("Motion at image", i, ":", np.sum(m), "------------------------------------")
            plt.plot(temperature_list)
            plt.plot(np.where(m, np.max(temperature_list), np.nan), 'rx')
            plt.show()



'''
Install the required packages by running the following command in your terminal or command prompt:
(pip install numpy matplotlib)

Use the noisy_temp_with_outliers function to generate a stream of noisy temperature readings with some occasional outliers. 
You can adjust the parameters noise, d, outlier_prob, and outlier_size to control the characteristics of the stream.
Create an instance of the MotionDetection class by providing the num_sigmas and discount parameters.
num_sigmas specifies the number of standard deviations a pixel must deviate from the average to count as motion.
discount is the discount factor for the averagerator.
Use the detect_motion method of the MotionDetection class to detect motion in a series of images. 
You can pass a list of images to this method, where each image is a 3D array of shape (height, width, 3) representing an RGB image. 
The method will return a list of tuples, where each tuple contains the index of the image in the list and 
a boolean 2D array of shape (height, width) indicating the pixels where motion was detected.
Use the matplotlib library to visualize the images and the motion detection results. 
You can loop through the list of tuples returned by the detect_motion method and 
display the corresponding images and motion detection results using the plt.imshow function.



This algorithm could be useful in various applications that require motion detection, such as surveillance systems, traffic monitoring, or sports analysis.

'''