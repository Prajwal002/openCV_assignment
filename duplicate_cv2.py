import cv2
import os
import numpy as np
from math import *
from sklearn.metrics import mean_squared_error

class detect_duplicate(object):

    def find_duplicate(self, files):
        try:
            file_list = os.listdir(files)
            print("Total images", len(file_list))
        except:
            print("wrong folder")
            exit(0)
        for l in file_list:
            self.file_base = os.path.join(files, l)
            for file in file_list:
                self.file = os.path.join(files, file)
                self.process_image()
        print("Process done")

    def process_image(self):
        if self.file_base != self.file:
            try:
                base_img = np.array(cv2.imread(self.file_base, cv2.IMREAD_GRAYSCALE))
                img = np.array(cv2.imread(self.file, cv2.IMREAD_GRAYSCALE))
                base_img = cv2.resize(base_img, (1200, 1800), interpolation = cv2.INTER_AREA)
                img = cv2.resize(img, (1200, 1800), interpolation = cv2.INTER_AREA)
                val = self.check_similarity(base_img, img)
                if val <= 5:
                    print("Image is similar or duplicate", self.file)
                    os.remove(self.file)
            except:
                pass

    def check_similarity(self, b, i):
        return sqrt(mean_squared_error(b, i))


def main():
    dp = detect_duplicate()
    dp.find_duplicate("/home/sprajwal/work/data/pics")

if __name__ == "__main__":
    main()