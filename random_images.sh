#!/bin/bash
filecount=0
while [ $filecount -lt 10000 ] ; do
    filesize=$RANDOM
    filesize=$(($filesize+1024))
    base64 /dev/urandom | 
    head -c "$filesize" > /tmp/file${filecount}.JPG
    ((filecount++))
done
