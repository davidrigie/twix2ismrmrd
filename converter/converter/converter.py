#!/usr/bin/env python

import glob
import shutil
import os
import subprocess
import datetime
import shutil
import traceback


CONVERTED_FILES = dict()

def eprint(*args, **kwargs):
    tprint(*args, file=sys.stderr, **kwargs)

def tprint(value, *args, **kwargs):

    now = datetime.datetime.now().strftime("%m-%d %H:%M")
    value = '[{}] - {}'.format(now, value)
    print(value, *args, **kwargs)

def convert_one_file(inputpath, outputpath, opts=[]):
    
    # Create output folder structure if necessary
    d = os.path.dirname(outputpath)
    if not os.path.isdir(d):
        os.makedirs(d)

    measNum = int(1)
    while True:
        try:
            p,ext = os.path.splitext(outputpath)
            new_outputpath = '{}_{}{}'.format(p, measNum, ext)
            cmd = ['siemens_to_ismrmrd', '-f', inputpath, '-o', new_outputpath, '-z', str(measNum)] + opts
            print(cmd)
            process = subprocess.check_call(cmd)
            measNum += 1
        except subprocess.CalledProcessError:
            break
                
    return measNum

def form_output_path(inputpath, inputdir, outputdir, ext):

    relpath    = os.path.relpath(inputpath, inputdir)
    outputpath = os.path.join(outputdir, relpath)
    outputpath = os.path.abspath(outputpath)
    outputpath = os.path.splitext(outputpath)[0] + ext

    return outputpath

def is_valid_input_file(filepath):
    if "FBAI" in os.path.dirname(filepath):
        return True

    return False

def convert_all_files(inputdir, outputdir,  **kwargs):

    pattern  = os.path.join(inputdir, '**', '*.dat')
    filelist = glob.glob(pattern, recursive=True)

    for inputpath in filelist:

        if not is_valid_input_file(inputpath):
            continue

        if (inputpath, os.stat(inputpath)) in CONVERTED_FILES:
            continue

        try:
            outputpath = form_output_path(inputpath, inputdir, outputdir, '.h5')
            
            if os.path.exists(outputpath):
                tprint('HDF File already exists. Skipping...')
                continue

            tprint('Converting {}'.format(inputpath))
            numMeasRead = convert_one_file(inputpath, outputpath, **kwargs)
            tprint('\nDone.\n')

            CONVERTED_FILES[(inputpath, os.stat(inputpath))] = True
        except Exception as exc:
            eprint('Problem with file{}'.format(inputpath))
            eprint(traceback.format_exc())


        
    return True
 
