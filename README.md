# Motion-Detection


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

