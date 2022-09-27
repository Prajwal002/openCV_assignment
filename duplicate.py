import os
import filecmp
import argparse
import tkinter
from tkinter import filedialog

class duplicateFinder(object):

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
                if self.file_base != self.file:
                    try:
                        self.compare_and_delete()
                    except:
                        pass
        print("Process done")

    def compare_and_delete(self):
        if filecmp.cmp(self.file_base, self.file):
            # os.remove(self.file)
            print("duplicate image deleted", self.file)

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--files", required=False,
                    help="folder to be selected")
    args = ap.parse_args()
    return args

def inter():
    tki = tkinter.Tk()
    tki.withdraw()
    files = filedialog.askdirectory()
    return files

def main():
    args = parse_args()
    files = inter()
    dup = duplicateFinder()
    dup.find_duplicate("/media/sprajwal/Prajwal_SSD/mah_derda_06-19-2022_inc")

if __name__ == "__main__":
    main()