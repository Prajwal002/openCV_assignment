import cv2

class MotionDetection:
    def detect_motion(self):
        img = cv2.VideoCapture(0)
        first_frame = None
        while img.isOpened():
            ret, frame = img.read()
            if not ret:
                print("Can't receive frame")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray,(5,5),0)
            if first_frame is None:
                first_frame = blur

            dframe = cv2.absdiff(first_frame,blur)
            thres = cv2.threshold(dframe, 127, 255, cv2.THRESH_BINARY)[1]
            contours = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
            if len(contours) > 0:
                for contour in contours:
                    # cv2.drawContours(frame, contour, -1, (0,255,255),2)
                    x, y, w, h = cv2.boundingRect(contour)
                    box_size = abs((x+w) - x) * abs(y - (y+h))
                    if box_size > 4000:
                        # cv2.rectangle(frame, (x, y),(x+w, y+h),(0,0,255),2)
                        cv2.putText(frame, "Motion detected", (70, 450),
                                    cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255), 2)
            cv2.imshow("image", frame)
            if cv2.waitKey(9) == ord('q'):
                break
        img.release()
        cv2.destroyAllWindows()

def main():
    md = MotionDetection()
    md.detect_motion()

if __name__ == "__main__":
    main()