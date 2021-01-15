import cv2
import math

def HandGestureRecognition(img):

    i_temp = img
    image = cv2.imread('shape.png')

    X, Y, f = i_temp.shape
    image = cv2.resize(image , (X, Y))

    gray_i = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray_i, 30, 200)
    c, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c_i = max(c, key=lambda x: cv2.contourArea(x))

    gray = cv2.cvtColor(i_temp, cv2.COLOR_BGR2GRAY)

    kernel = (35, 35)
    blur = cv2.GaussianBlur(gray, kernel, 0)

    _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)

    contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = max(contours, key=lambda x: cv2.contourArea(x))
    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)
    cv2.drawContours(thresh, contours, -1, (0, 255, 0), 3)

    defect_num = 0

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        a = (end[0] - start[0])**2 + (end[1] - start[1])**2
        b = (far[0] - start[0])**2 + (far[1] - start[1])**2
        c = (end[0] - far[0])**2 + (end[1] - far[1])**2
        A = math.sqrt(a)
        B = math.sqrt(b)
        C = math.sqrt(c)

        theta = math.acos((b + c - a)/(2*B*C)) * 57

        if theta <= 90:
            defect_num += 1
            cv2.circle(i_temp, far, 1, [0, 0, 255], -1)
        cv2.line(i_temp, start, end, [0, 255, 0], 2)

    cv2.imshow('threshold', thresh)
    cv2.imshow('Hulled image marked with defects' , img)
    if defect_num==0:
        err = cv2.matchShapes(cnt, c_i,1,0.0 )
        if err <=1.3588:
            defect_num = 404
    return defect_num


cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    image = frame
    cv2.rectangle(image, (50, 50), (300, 300), (0, 0, 255), 3)
    frame_temp = frame.copy()
    img = frame_temp[50:300,50:300]
    cd = HandGestureRecognition(img)

    if cd==1:
        cv2.putText(frame , '2' ,(400,400), cv2.FONT_HERSHEY_SIMPLEX ,1,(0,0,255),2,cv2.LINE_AA)
    elif cd==2:
        cv2.putText(frame, '3', (400, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    elif cd == 3:
        cv2.putText(frame, '4', (400, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    elif cd==4:
        cv2.putText(frame, '5', (400, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    elif cd==404:
        cv2.putText(frame, '1', (400, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, '0', (400, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('image' , image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
