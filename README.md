# Hand Gesture Recognition using OpenCV-Python

Here, I would be specifying the details about the Hand Gesture Recognition's algorithm. The project displays the numbers of fingers(0 - 5) the user is showing to the webcam.
**Requirements**: The background in the ROI should be of a single colour, or else the user won't get accurate results.

### Idea behind the algorithm
Between two fingers, we have a gap known as _interdigital space_. Now, for knowing the number of fingers being shown to the webcam, we need to count the number of these spaces
and the number of fingers will be one more than that count.

### How did I use OpenCV here?
Contour is a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape
analysis and object detection and recognition. For getting better accuracy while using contours, use binary images. So before finding contours, apply threshold or canny edge
detection.
