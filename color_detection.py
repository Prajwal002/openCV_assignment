import cv2
import numpy as np

class ColorDetection():
    def detect_color(self):
        img = cv2.VideoCapture("/home/sprajwal/Downloads/dash-cam-traffic-light.mp4")
        while img.isOpened():
            ret, frame = img.read()
            if not ret:
                print("Can't receive frame")
                break
            blurred = cv2.GaussianBlur(frame,(5, 5), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            lower = np.array([0,150, 20])
            upper = np.array([15,255,255])
            mask = cv2.inRange(hsv, lower, upper)
            contours = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
            if len(contours) != 0:
                for contour in contours:
                    if cv2.contourArea(contour) > 500:
                        x, y, w, h = cv2.boundingRect(contour)
                        cv2.rectangle(frame, (x, y),(x+w, y+h), (0,0,255), 2)
            cv2.imshow("merged", frame)
            if cv2.waitKey(9) == ord('q'):
                break
        img.release()
        cv2.destroyAllWindows()

def main():
    cd = ColorDetection()
    cd.detect_color()

if __name__ == "__main__":
    main()
