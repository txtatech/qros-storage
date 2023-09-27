The 'step1-djinnfluxer2a.py' script will read the 'Virtual_Forest_Epoch_Rising.txt' and encode it with the djinn-dna encoding method and produce a encoded_dna.json file:

python3 step1-djinnfluxer2a.py

The 'step2-qros-builder-full.py' script will read the encoded_dna.json file and gzip, base64 encode, split into chunks and write to the chunks.json file.
The script also produces .png qr codes of the data and produces a qr code video file.

python3 step2-qros-builder-full.py

Notes:

From this point the 'chunks.json' file can be read to reconstruct its data. 

Next step:

Build final decoder that reads 'chunks.json', translates the DNA encoding via a reverse map and creates the 'Virtual_Forest_Epoch_Rising.txt' file.  .
