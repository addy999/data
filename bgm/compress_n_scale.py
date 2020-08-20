import sys,os
from subprocess import Popen
from PIL import Image

def compress(script_path, src_path, dest_path):
    
    '''
    Call img4web.py script on images in src_pth and places them in dest_path
    '''
    process = Popen(['python3', script_path, '-s' + str(src_path), '-d' + str(dest_path)])
    
    while process.poll() is None:
        print(process.stdout.readline()) # This blocks until it receives a newline.

def resize_img(img_dir):

    # outfile = os.path.splitext(infile)[0] + ".thumbnail"
    for infile in os.listdir(img_dir):
        try:
            if '.jpg' in infile:
                im = Image.open(img_dir + '/' + infile)
                im.thumbnail([i/3 for i in im.size], Image.ANTIALIAS)
                im.save(img_dir + '/' + infile, "JPEG")
                print('Resized ', infile)
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)

if __name__ == "__main__":
    
    # cwd = os.getcwd()   
    # cwd = os.path.dirname(os.path.realpath(__file__))
    
    # 1. Compress images  
    
    src_path = './'
    # compress(cwd + '../docs/css/assests/raw', src_path, dest_path)
    
    # 2. Scale + overwrite images
    
    resize_img(src_path)