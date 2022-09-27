import cv2
import numpy as np

class Evaluuation(object):

    ANSWER = {
        1:2,
        2:1,
        3:1,
        4:4,
        5:2
    }

    def process_image(self):
        image = "/home/sprajwal/Pictures/omr11"
        img = cv2.imread(image)
        img = cv2.pyrUp(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        self.bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        canny = cv2.Canny(blur, 70, 200)
        contour = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        self.image_copy = img.copy()
        self.selected = self.get_selection(contour)
        score = self.get_result(self.selected)
        self.print_on_image(score)

    def get_selection(self, cntr):
        self.questionCnts = []
        q1 = 5
        q2 = 5
        q3 = 5
        q4 = 0
        q5 = 0
        d1 = dict()
        d2 = dict()
        d3 = dict()
        d4 = dict()
        d5 = dict()
        for c in cntr:
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)
            if w >= 40 and h >= 20 and ar >= 0.9 and ar <= 1.1:
                M = cv2.moments(c)
                if M['m00'] != 0:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    if 253 <= cy <= 258:
                        self.questionCnts.append(c)
                        x, y, w, h = cv2.boundingRect(c)
                        block = self.bin[y:y+h, x:x+w]
                        white_px = np.sum(block == 255)
                        d1[white_px] = q1
                        q1 -= 1
                    if 404 <= cy <= 406:
                        self.questionCnts.append(c)
                        x, y, w, h = cv2.boundingRect(c)
                        block = self.bin[y:y+h, x:x+w]
                        white_px = np.sum(block == 255)
                        d2[white_px] = q2
                        q2 -= 1
                    elif 552 <= cy <= 554:
                        x, y, w, h = cv2.boundingRect(c)
                        block = self.bin[y:y+h, x:x+w]
                        white_px = np.sum(block == 255)
                        self.questionCnts.append(c)
                        d3[white_px] = q3
                        q3 -= 1
                    elif 697 <= cy <= 700:
                        x, y, w, h = cv2.boundingRect(c)
                        block = self.bin[y:y+h, x:x+w]
                        white_px = np.sum(block == 255)
                        self.questionCnts.append(c)
                        q4 += 1
                        d4[white_px] = q4
                    elif 840 <= cy <= 845:
                        x, y, w, h = cv2.boundingRect(c)
                        block = self.bin[y:y+h, x:x+w]
                        white_px = np.sum(block == 255)
                        self.questionCnts.append(c)
                        q5 += 1
                        d5[white_px] = q5
                    # cv2.circle(self.image_copy, (cx, cy), 7, (0, 0, 255), -1)
        return {1:d1[max(d1)], 2:d2[max(d2)], 3:d3[max(d3)], 4:d4[max(d4)], 5:d5[max(d5)]}

    def get_result(self, selected):
        for k in range(1, 6):
            marks = 0
            if selected[k] == self.ANSWER[k]:
                marks += 1
        return (marks/5)* 100

    def print_on_image(self,score):

        print("Total questions :{}".format(int(len(self.questionCnts)/5)))
        print("Total percentage ->", score)
        cv2.putText(self.image_copy, f"{score}%", (100, 130), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 3)
        cv2.imshow("img", self.image_copy)
        cv2.waitKey(0)




def main():
    eval = Evaluuation()
    eval.process_image()

if __name__ == "__main__":
    main()