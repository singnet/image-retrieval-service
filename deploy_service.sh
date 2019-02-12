#!/usr/bin/env bash

cd data
bash download.bash
python preprocess.py

cd ..
python generate_hashtable.py

if [ ! -x "$(command -v nvidia-docker)" ]; then
    docker build --file Dockerfile . -t singularitnet:image-retrieval-cpu
else
    docker build --file Dockerfile.gpu . -t singularitnet:image-retrieval-gpu
fi

