#!/bin/bash
# see https://unix.stackexchange.com/questions/199863/create-many-files-with-random-content
dd if=/dev/urandom bs=1024 count=10240 | split -a 4 -b 1k - file.
