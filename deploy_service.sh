#!/usr/bin/env bash

cd data
bash download.bash
python preprocess.py

cd ..
python generate_hashtable.py

if [ ! -x "$(command -v nvidia-docker)" ]; then
    echo "Building CPU based Image"
    docker build --file Dockerfile . -t singularitynet:image-retrieval-cpu
else
    echo "Building GPU based Image"
    docker build --file Dockerfile.gpu . -t singularitynet:image-retrieval-gpu
fi

