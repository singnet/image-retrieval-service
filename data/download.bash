#!/usr/bin/env bash
if [ ! -f class-descriptions-boxable.csv ]; then
    wget https://datasets.figure-eight.com/figure_eight_datasets/open-images/class-descriptions-boxable.csv
    else
    echo "Class Description csv exists."
fi

if [ ! -f validation-images.csv ]; then
    wget https://datasets.figure-eight.com/figure_eight_datasets/open-images/validation-images.csv
    else
    echo "Validation images csv exists."
fi

if [ ! -f validation-annotations-bbox.csv ]; then
    wget https://datasets.figure-eight.com/figure_eight_datasets/open-images/validation-annotations-bbox.csv
    else
    echo "Validation annotation bounding boxes file exists."
fi

if [ ! -f validation.zip ]; then
    wget https://datasets.figure-eight.com/figure_eight_datasets/open-images/zip_files_copy/validation.zip
    else
    echo "Validation Description file exists."
fi

if [ ! -d validation ]; then
    unzip validation.zip
    else
    echo "Validation Folder has been unzipped"
fi

