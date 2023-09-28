Steps:

The '1qros-storage-data.py' script will read the 'Virtual_Forest_Epoch_Rising.txt' file and encode it with the djinn-dna encoding method and produce a file named:

encoded_dna_data.json

Usage:

python3 1qros-storage-data.py


The '2qros-storage-js.py' script will read the 'hive-tx.min.js' file and encode it with the djinn-dna encoding method and produce a file named:

encoded_dna_js.json

Usage:

python3 2qros-storage-js.py

The '3qros-storage-py.py' script will read the '4qros-storage-builder.py' file and encode it with the djinn-dna encoding method and produce a file named:

encoded_dna_py.json

Usage:

python3 3qros-storage-py.py

# At this point I manually create a JSON file with an entry from each of the previously three created JSON files. The file is named:

encoded_dna_full.json

The '4qros-storage-builder.py' script will read the 'encoded_dna_full.json' file then gzip, base64 encode, split into chunks and write all data to an output file named:

chunks.json

Usage:

python3 4qros-storage-builder.py


Notes:

From this point the 'chunks.json' file can be read to reconstruct its data. 

Next steps:

Build final decoder that reads 'chunks.json', and creates the 'encoded_dna_full.json' file from it. Then build a second decoder that translates the DNA encoding via a reverse map and creates all the original scripts from the 'encoded_dna_full.json' file.
