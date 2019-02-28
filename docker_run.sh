#!/usr/bin/env bash
sudo docker build --file Dockerfile . -t singularitynet:image-retrieval-cpu
sudo docker run -it -v /etc/letsencrypt:/etc/letsencrypt -v /home/zelalem/Image-retrieval-in-pytorch/data/classed_data:/image-retrieval-in-pytorch/data/classed_data --name image-retrieval-service -d -p 8003:8003 -p 8004:8004 singularitynet:image-retrieval-cpu