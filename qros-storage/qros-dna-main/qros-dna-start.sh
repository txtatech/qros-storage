#!/bin/bash

# Start
python3 qros_dna_main.py

# Wait
wait

echo Running qros_dna_chunker as a sub-process

# Wait
wait

echo Working... Chunks Created

# Start
python3 qros_dna_squashfs.py

# Wait
wait

echo Working... Created Squashfs

# Wait
wait

# Start
python3 qros_dna_chunksquash.py

# Wait
wait

echo Working... Chunked Squashfs 

# Start
python3 qros_dna_os.py

# Wait
wait

echo Working... Created Live DNA OS

# Start
python3 qros_dna_os_fs.py

# Wait
wait

echo Working... Created Live DNA OS FS

echo Encoding has finished and all files have been generated!

# Wait
wait
