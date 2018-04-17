## Description
A simple program that monitors a folder for .DAT files and converts them to ISMRMRD (HDF5) using the [siemens_to_ismrmrd converter ](https://github.com/ismrmrd/siemens_to_ismrmrd)

This will run on most linux systems with docker installed. 

## Usage

Modify the following lines in ```config.env``` to point to the desired folder locations on your system:

```bash
##################################################
#      Specify directories for input/output      #
##################################################
TWIX_INPUT_DIR      = /home/rigied01/test/test_input
DONE_DIR            = /home/rigied01/test/test_done
ISMRMRD_OUTPUT_DIR  = /home/rigied01/test/test_output
#________________________________________________#
```

Then run ```make``` to build the docker image and ```make start``` to run the container. It can also be run in an interactive mode with ```make shell```

Siemens raw MRI data files go in ```TWIX_INPUT_DIR```, and the resulting converted files will end up in ```ISMRMRD_OUTPUT_DIR```. The original .DAT files will be moved to ```DONE_DIR``` after they have been converted.  

## Note

This has not been thoroughly tested. Use at your own risk!
