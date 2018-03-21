#!/usr/bin/python
import os
import errno
import sys, getopt

#
# Create base directores
#

# Directory array
pathList = [
    'app',
    'app/assets',
    'app/assets/fonts',
    'app/assets/images',
    'app/pages',
    'app/pages/_includes',
    'app/pages/_layouts',
    'app/scripts',
    'app/styles'
]

# Path creation function
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

# Take path base from command line
def main(argv):
    basepath = ''
    try:
        opts, args = getopt.getopt(argv,"hb:",["basepath="])
    except getopt.GetoptError:
        print('install.py -b <basepath>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('install.py -b <basepath>')
            sys.exit()
        elif opt in ("-b", "--basepath"):
            basepath = arg

    # Create paths including the passed on subpath
    for path in pathList:
        mkdir_p(basepath + path)

if __name__ == "__main__":
   main(sys.argv[1:])
