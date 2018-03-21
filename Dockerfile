FROM ubuntu:16.04

RUN apt-get update --quiet && \
    apt-get install --yes  \
    python3 python3-pip \
    wget build-essential libhdf5-serial-dev cmake git \
    python python-dev python-pip python-virtualenv \
    libboost-all-dev xsdcxx libxerces-c-dev libhdf5-serial-dev \ 
    h5utils hdf5-tools libtinyxml-dev libxml2-dev libxslt1-dev

# ISMRMD
RUN git clone https://github.com/ismrmrd/ismrmrd.git && \
    cd ismrmrd && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install 

# SIEMENS_TO_ISMRMD
RUN git clone https://github.com/ismrmrd/siemens_to_ismrmrd.git && \
    cd siemens_to_ismrmrd && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install

# Python converter wrapper
COPY converter /tmp/converter
RUN  pip3 install --upgrade pip
RUN  pip3 install /tmp/converter

# Set more environment variables in preparation for Gadgetron installation
ENV ISMRMRD_HOME=/usr/local

ENV PATH=$PATH:$ISMRMRD_HOME/bin \
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ISMRMRD_HOME/lib

# Clean up packages.
RUN  apt-get clean && \
rm -rf /var/lib/apt/lists/*

ENTRYPOINT twixconvert /input_data /output_data /processed_data