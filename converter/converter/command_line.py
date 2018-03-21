import converter
import sys
import time
import os

usage = """
expected 3 arguments

usage: twixconvert [dirpath1] [dirpath2] [dirpath3]
"""

def check_args(arglist):
    if len(arglist) != 4:
        print(usage)
        return False
    
    return True


def main():
    if check_args(sys.argv):
        inputdir  = sys.argv[1]
        outputdir = sys.argv[2]
        donedir   = sys.argv[3]

        while True:
            converter.tprint('Checking for files to convert ... ')
            converter.convert_all_files(inputdir, outputdir, donedir)
            time.sleep(10)
            os.system('clear')



        