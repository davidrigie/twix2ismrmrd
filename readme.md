## Description
A simple program that monitors a folder for .DAT files and converts them to ISMRMRD (HDF5) using the [siemens_to_ismrmrd converter ](https://github.com/ismrmrd/siemens_to_ismrmrd)

This will run on most linux systems with docker installed. 

## Usage

Modify the following lines in ```config.env``` to point to the desired folder locations on your system:

```bash
##################################################
#      Specify directories for input/output      #
##################################################
TWIX_INPUT_DIR      = /media/MRIScan/Working-Temp/TWIX_TO_ISMRMRD/input_twix
ISMRMRD_OUTPUT_DIR  = /media/MRIScan/Working-Temp/TWIX_TO_ISMRMRD/output_ismrmrd
LOG_DIR             = /media/MRIScan/Working-Temp/TWIX_TO_ISMRMRD/logs
#________________________________________________#
```

Then run ```make``` to build the docker image and ```make start``` to run the container. It can also be run in an interactive mode with ```make shell```

Siemens raw MRI data files go in ```TWIX_INPUT_DIR```, and the resulting converted files will end up in ```ISMRMRD_OUTPUT_DIR```.  

## Note

This has not been thoroughly tested. Use at your own risk!
