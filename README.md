# Sensor-Data-Analytics
1. Prewitt edge detector: gradient filter és nonmaxima-suppression (NMS) Output is two images: 
  a. gradient magnitute; 2. final result after NMS.
2. Thresholding algorithm by Otsu Output: thresholded image and obtained threshold value.  
3. Detection of circular object by edge detection and Hough transform for circles Input: 
  a. image containing circular objects, e.g., cells;
  b. range of diameters. Output: 1. accumulator image; 2. input image with objects detected in given range of diameters. 
4. Motion tracking of feature points and dense optical flow Input: 
  a. short video sequence;
  b. maximum displacement. Output: 
    ab. points tracked in the video sequence (for all test sequences); 
    ac. optical flow of the sequence (for motor.mpg only).
