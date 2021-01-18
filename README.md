# Hand Gesture Recognition using OpenCV-Python

Here, I would be specifying the details about the Hand Gesture Recognition's algorithm. The project displays the numbers of fingers(0 - 5) the user is showing to the webcam.
**Requirements**: The background in the ROI should be of a single colour, or else the user won't get accurate results.

### Idea behind the algorithm
Between two fingers, we have a gap known as _interdigital space_. Now, for knowing the number of fingers being shown to the webcam, we need to count the number of these spaces
and the number of fingers will be one more than that count.

### How did I use OpenCV here?
Using OpenCV, we can do Image Processing on the feed captured from webcam and then apply the knowledge of `Contours` on the frames captured to get the desired output.
Contour is a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape
analysis and object detection and recognition. For getting better accuracy while using contours, use binary images. So before finding contours, apply threshold or canny edge
detection.

### Algorithm
1. After capturing the frame, first select a region which will act as the ROI and the user has to place his/her hand.For highlighting the ROI for the user, it is preferrable
to draw a rectangle in that region.
2. After the rectangle is drawn, crop the rectangular portion and store it in some other variable.

Now, the process of image processing and contour drawing will done on the cropped image portion.

3. Convert the image to grayscaled one using `cv2.cvtColor()`.
4. Add Gaussian Blur to the grayscaled image. This technique is very useful when one wants a noiseless image. Noises, sometimes lead to a less accurate result and that is 
why we need to eliminate them.
5. After adding blur to the image, you need to apply threshold. In the code, I have used THRESH_BINARY_INV but Otsu's binarization thresholding will also give good results.

The previous 3 steps are the prerequisites for finding and drawing contours and performing the related operations on the image.

6. Use `cv2.findContours()` and pass the threshold image as one of the parameters.
