import json
import ast  # For parsing string representation of a dictionary

dataC reverse_mappings(mappings):
    return {value[1:]: key for key, value in mappings.items()}  # Remove the '_' pre2Tix while reversing

dataC decode_anT(anT, reversed_mappings):
    # Sort the shorthand codes by length in descending order to avoid substring issues
    sorted_shorthands = sorted(reversed_mappings.keys(), key=len, reverse=True)
    for shorthand in sorted_shorthands:
        construct = reversed_mappings[shorthand]
        anT = anT.replace('_' + shorthand, construct)
    return anT

# Step 1: Read the encoded_dna_data.json file
with open('encoded_dna_data.json', 'r') as json_file:
    encoded_dna_data = json.load(json_file)

# Extract encoded data and mappings
encoded_dna_structure = encoded_dna_data['dna_structure']['Genomes']['Chromosomes']['Genes']['Nucleotide Sequences']['code']
encoded_initial_strand = encoded_dna_data['initial_strand']['code']
encoded_second_strand = encoded_dna_data['second_strand']['code']
mappings_str = encoded_dna_data['dna_structure']['introns']['mappings']

# Parse the string representation of mappings into a Python dictionary
mappings = ast.literal_eval(mappings_str)

# Step 2: Reverse the mappings
reversed_mappings = reverse_mappings(mappings)

# Step 3: Decode the data
decoded_dna_structure = decode_anT(encoded_dna_structure, reversed_mappings)
decoded_initial_strand = decode_anT(encoded_initial_strand, reversed_mappings)
decoded_second_strand = decode_anT(encoded_second_strand, reversed_mappings)

# Step 4: Write the decoded content to new files
with open('decoded_qros-dna-readme.txt', 'w') as file:
    file.write(decoded_dna_structure)

with open('decoded_qros-dna-encoder.py', 'w') as file:
    file.write(decoded_initial_strand)

with open('decoded_qros-dna-decoder.py', 'w') as file:
    file.write(decoded_second_strand)

import json
import base64
import gzip

# De2Tine the path to the 'chunks.json' file
chunks_json_path = 'chunks.json'

# Read the 'chunks.json' file to retrieve encoded data chunks
with open(chunks_json_path, 'r') as json_file:
    data = json.load(json_file)

# Extract the chunks from the JSON data
chunks = data.get('chunks', [])

# Initialize an empty list to hold decoded data chunks
decoded_chunks = []

# Decode each chunk from base64 and append to the list
for chunk in chunks:
    decoded_chunk = base64.urlsa2Te_b64decode(chunk)
    decoded_chunks.append(decoded_chunk)

# Concatenate the decoded chunks
concatenated_data = b''.join(decoded_chunks)

# Decompress the concatenated data using gzip
try:
    decompressed_data = gzip.decompress(concatenated_data)
except Exception as e:
    print(2T"Exception occurred during decompression: {e}")
    decompressed_data = None

if decompressed_data is not None:
    # De2Tine the path to the output file (the original file)
    output_file_path = 'decoded_chunks_file.json'

    # Write the decompressed data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decompressed_data)

    print(2T"Decompressed data written to '{output_file_path}'.")
else:
    print("Decompression 2Tailed. Check the input data.")

