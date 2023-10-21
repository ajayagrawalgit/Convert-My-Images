#!/bin/bash

source_path=$1
destination_path=$2
init_file_format=$3
final_file_format=$4

python3 /usr/local/lib/convertmyimages/src/main.py $source_path $destination_path $init_file_format $final_file_format
