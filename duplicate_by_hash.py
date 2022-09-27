import os
import argparse
from hashlib import md5

class Detect_Duplicate(object):

    def __init__(self):
        self.dict_hash = dict()

    def make_hash(self,files):
        try:
            file_list = os.listdir(files)
            print("Total images", len(file_list))
        except:
            print("wrong folder")
            exit(0)
        for i in file_list:
            self.image = os.path.join(files, i)
            hash = md5(open(self.image, "rb").read()).hexdigest()
            self.hash_is = self.find_hash(hash)
            self.delete_duplicate(hash, i)
        print("--Done--")

    def delete_duplicate(self, hash, i):

        if self.hash_is:
            self.dict_hash[hash] = self.image

        else:
            # os.remove(self.image)
            print("duplicate image found & deleted", i)

    def find_hash(self, hash):
        if hash not in self.dict_hash:
            return True

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--files", required=True,
                    help="folder to be selected")
    args = ap.parse_args()
    return args

def main():
    args = parse_args()
    # files = "/home/sprajwal/work/data/pics"
    dd =  Detect_Duplicate()
    dd.make_hash(args.files)


if __name__ == "__main__":
    main()