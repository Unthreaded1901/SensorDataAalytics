import cv2 as cv
import numpy as np

video= 'sequence_gray.mpg'

v_name = video[video.rindex('') + 1 : video.rindex('.')]

cap = cv.VideoCapture(video)

feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.01,
                       minDistance = 7,
                       blockSize = 3)
#lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)

#creating VideoWriter object and defining the codec
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(v_name+'.avi',fourcc, 1.0, size)

# Creating a mask image for drawing purposes
mask = np.zeros_like(old_frame)
while(1):
    ret,frame = cap.read()

    if not ret:
        break

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # calculate optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    if p1 is None or p0 is None:
        break

    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]
    # drawing the tracks
    for i,(new,old) in enumerate(zip(good_new, good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        # mask = cv.line(mask, (a,b),(c,d), (255,255,255), 2)
        frame = cv.circle(frame,(a,b),5,(0,255,0),-1)
    img = cv.add(frame,mask)
    cv.imshow('frame',img)
    out.write(img)
    k = cv.waitKey(1) & 0xff
    if k == 27:
        break
    # Updating the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

cap.release()
out.release()
cv.destroyAllWindows()
