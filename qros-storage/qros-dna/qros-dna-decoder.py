# Begin decoding and reconstruction of original files from encoded_dna_data.json

import os
import json
import ast  # For parsing string representation of a dictionary

os.makedirs('outputs/decoded', exist_ok=True)  # Create the directory if it doesn't exist

def reverse_mappings(mappings):
    return {value[1:]: key for key, value in mappings.items()}  # Remove the '_' prefix while reversing

def decode_body(body, reversed_mappings):
    # Sort the shorthand codes by length in descending order to avoid substring issues
    sorted_shorthands = sorted(reversed_mappings.keys(), key=len, reverse=True)
    for shorthand in sorted_shorthands:
        construct = reversed_mappings[shorthand]
        body = body.replace('_' + shorthand, construct)
    return body

# Step 1: Read the encoded_dna_data.json file
with open('outputs/encoded_dna_data.json', 'r') as json_file:
    encoded_dna_data = json.load(json_file)

# Extract encoded data and mappings
encoded_dna_structure = encoded_dna_data['dna_structure']['Genomes']['Chromosomes']['Genes']['Nucleotide Sequences']['code']
encoded_initial_strand = encoded_dna_data['initial_strand']['code']
encoded_second_strand = encoded_dna_data['second_strand']['code']
mappings_str = encoded_dna_data['dna_structure']['introns']['mappings']
non_encoded_fourth_file = encoded_dna_data['dna_structure']['exons']['js']  # New line for fourth file
non_encoded_fifth_file = encoded_dna_data['dna_structure']['files']['code']  # New line for fifth file
non_encoded_sixth_file = encoded_dna_data['dna_structure']['profusion']['code']  # New line for sixth file
encoded_third_strand = encoded_dna_data['third_strand']['encoded-encoder']
encoded_third_strand = encoded_dna_data['third_strand']['encoded-decoder']
non_encoded_ninth_file = encoded_dna_data['third_strand']['js-shell']
non_encoded_tenth_file = encoded_dna_data['third_strand']['decoder']
non_encoded_eleventh_file = encoded_dna_data['dna_structure']['emu']['libv86']
non_encoded_twelfth_file = encoded_dna_data['dna_structure']['emu']['v86wasm']
non_encoded_thirteenth_file = encoded_dna_data['dna_structure']['exons']['shell']  # New line for fourth file
non_encoded_fourteenth_file = encoded_dna_data['dna_structure']['exons']['html']  # New line for fourth file

# Parse the string representation of mappings into a Python dictionary
mappings = ast.literal_eval(mappings_str)

# Step 2: Reverse the mappings
reversed_mappings = reverse_mappings(mappings)

# Step 3: Decode the data
decoded_dna_structure = decode_body(encoded_dna_structure, reversed_mappings)
decoded_initial_strand = decode_body(encoded_initial_strand, reversed_mappings)
decoded_second_strand = decode_body(encoded_second_strand, reversed_mappings)
decoded_third_strand = decode_body(encoded_second_strand, reversed_mappings)

# Step 4: Write the decoded content to new files
with open('outputs/decoded/decoded_qros-dna-readme.txt', 'w') as file:
    file.write(decoded_dna_structure)

with open('outputs/decoded/decoded_qros-dna-combos.sh', 'w') as file:
    file.write(decoded_initial_strand)

with open('outputs/decoded/decoded_qros-dna-txt-split.sh', 'w') as file:
    file.write(decoded_second_strand)

with open('outputs/decoded/decoded_web0.js', 'w') as file:
    file.write(non_encoded_fourth_file)

with open('outputs/decoded/decoded_file-qros-dna-zip.json', 'w') as file:
    file.write(non_encoded_fifth_file)

with open('outputs/decoded/decoded_html-index.html', 'w') as file:
    file.write(non_encoded_sixth_file)

with open('outputs/decoded/decoded_qros-dna-encoder.py', 'w') as file:
    file.write(decoded_third_strand)

with open('outputs/decoded/decoded_qros-dna-decoder.py', 'w') as file:
    file.write(decoded_third_strand)

with open('outputs/decoded/decoded_js-shell.html', 'w') as file:
    file.write(non_encoded_ninth_file)

with open('outputs/decoded/decoded_qros-dna-decoder1.py', 'w') as file:
    file.write(non_encoded_tenth_file)


with open('outputs/decoded/decoded_libv86.js', 'w') as file:
    file.write(non_encoded_eleventh_file)

with open('outputs/decoded/decoded_file-v86wasm.json', 'w') as file:
    file.write(non_encoded_twelfth_file)

with open('outputs/decoded/decoded_shell.html', 'w') as file:
    file.write(non_encoded_thirteenth_file)

with open('outputs/decoded/decoded_index0.html', 'w') as file:
    file.write(non_encoded_fourteenth_file)

# Begin chunks.json decoder
 
import json
import base64
import gzip

# Define the path to the 'chunks.json' file
chunks_json_path = 'outputs/chunks.json'

# Read the 'chunks.json' file to retrieve encoded data chunks
with open(chunks_json_path, 'r') as json_file:
    data = json.load(json_file)

# Extract the chunks from the JSON data
chunks = data.get('chunks', [])

# Initialize an empty list to hold decoded data chunks
decoded_chunks = []

# Decode each chunk from base64 and append to the list
for chunk in chunks:
    decoded_chunk = base64.urlsafe_b64decode(chunk)
    decoded_chunks.append(decoded_chunk)

# Concatenate the decoded chunks
concatenated_data = b''.join(decoded_chunks)

# Decompress the concatenated data using gzip
try:
    decompressed_data = gzip.decompress(concatenated_data)
except Exception as e:
    print(f"Exception occurred during decompression: {e}")
    decompressed_data = None

if decompressed_data is not None:
    # Define the path to the output file (the original file)
    output_file_path = 'outputs/decoded/decoded_chunks_file.json'

    # Write the decompressed data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decompressed_data)

    print(f"Decompressed data written to '{output_file_path}'.")
else:
    print("Decompression failed. Check the input data.")

# Begin reconstruction of original files from decoded_chunks_file.json

import json
import ast  # For parsing string representation of a dictionary

def reverse_mappings(mappings):
    return {value[1:]: key for key, value in mappings.items()}  # Remove the '_' prefix while reversing

def decode_body(body, reversed_mappings):
    # Sort the shorthand codes by length in descending order to avoid substring issues
    sorted_shorthands = sorted(reversed_mappings.keys(), key=len, reverse=True)
    for shorthand in sorted_shorthands:
        construct = reversed_mappings[shorthand]
        body = body.replace('_' + shorthand, construct)
    return body

# Step 1: Read the encoded_dna_data.json file
with open('outputs/decoded/decoded_chunks_file.json', 'r') as json_file:
    encoded_dna_data = json.load(json_file)

# Extract encoded data and mappings
encoded_dna_structure = encoded_dna_data['dna_structure']['Genomes']['Chromosomes']['Genes']['Nucleotide Sequences']['code']
encoded_initial_strand = encoded_dna_data['initial_strand']['code']
encoded_second_strand = encoded_dna_data['second_strand']['code']
non_encoded_fourth_file = encoded_dna_data['dna_structure']['exons']['js']  # New line for fourth file
mappings_str = encoded_dna_data['dna_structure']['introns']['mappings']
non_encoded_fifth_file = encoded_dna_data['dna_structure']['files']['code']  # New line for fifth file
non_encoded_sixth_file = encoded_dna_data['dna_structure']['profusion']['code']  # New line for sixth file
encoded_third_strand = encoded_dna_data['third_strand']['encoded-encoder']
encoded_third_strand = encoded_dna_data['third_strand']['encoded-decoder']
non_encoded_ninth_file = encoded_dna_data['third_strand']['js-shell']
non_encoded_tenth_file = encoded_dna_data['third_strand']['decoder']
non_encoded_eleventh_file = encoded_dna_data['dna_structure']['emu']['libv86']
non_encoded_twelfth_file = encoded_dna_data['dna_structure']['emu']['v86wasm']
non_encoded_thirteenth_file = encoded_dna_data['dna_structure']['exons']['shell']  # New line for fourth file
non_encoded_fourteenth_file = encoded_dna_data['dna_structure']['exons']['html']  # New line for fourth file

# Parse the string representation of mappings into a Python dictionary
mappings = ast.literal_eval(mappings_str)

# Step 2: Reverse the mappings
reversed_mappings = reverse_mappings(mappings)

# Step 3: Decode the data
decoded_dna_structure = decode_body(encoded_dna_structure, reversed_mappings)
decoded_initial_strand = decode_body(encoded_initial_strand, reversed_mappings)
decoded_second_strand = decode_body(encoded_second_strand, reversed_mappings)
decoded_third_strand = decode_body(encoded_third_strand, reversed_mappings)

# Step 4: Write the decoded content to new files
with open('outputs/decoded/decoded_qros-dna-chunks-readme.txt', 'w') as file:
    file.write(decoded_dna_structure)

with open('outputs/decoded/decoded_qros-dna-chunks-combos.sh', 'w') as file:
    file.write(decoded_initial_strand)

with open('outputs/decoded/decoded_qros-dna-chunks-txt-split.sh', 'w') as file:
    file.write(decoded_second_strand)

with open('outputs/decoded/decoded_chunks-web0.js', 'w') as file:
    file.write(non_encoded_fourth_file)

with open('outputs/decoded/decoded_chunks-file-qros-dna-zip.json', 'w') as file:
    file.write(non_encoded_fifth_file)

with open('outputs/decoded/decoded_chunks-index.html', 'w') as file:
    file.write(non_encoded_sixth_file)

with open('outputs/decoded/decoded_chunks-qros-dna-encoder.py', 'w') as file:
    file.write(decoded_third_strand)

with open('outputs/decoded/decoded_chunks-qros-dna-decoder.py', 'w') as file:
    file.write(decoded_third_strand)

with open('outputs/decoded/decoded_chunks-js-shell.html', 'w') as file:
    file.write(non_encoded_ninth_file)

with open('outputs/decoded/decoded_chunks-qros-dna-decoder1.py', 'w') as file:
    file.write(non_encoded_tenth_file)

with open('outputs/decoded/decoded_chunks-libv86.js', 'w') as file:
    file.write(non_encoded_eleventh_file)

with open('outputs/decoded/decoded_chunks-file-v86wasm.json', 'w') as file:
    file.write(non_encoded_twelfth_file)

with open('outputs/decoded/decoded_chunks-shell.html', 'w') as file:
    file.write(non_encoded_thirteenth_file)

with open('outputs/decoded/decoded_chunks-index0.html', 'w') as file:
    file.write(non_encoded_fourteenth_file)

# Begin final file extractions

import json
import base64
import gzip

# Define the path to the 'chunks.json' file
chunks_json_path = 'outputs/decoded/decoded_chunks-file-qros-dna-zip.json'

# Read the 'chunks.json' file to retrieve encoded data chunks
with open(chunks_json_path, 'r') as json_file:
    data = json.load(json_file)

# Extract the chunks from the JSON data
chunks = data.get('chunks', [])

# Initialize an empty list to hold decoded data chunks
decoded_chunks = []

# Decode each chunk from base64 and append to the list
for chunk in chunks:
    decoded_chunk = base64.urlsafe_b64decode(chunk)
    decoded_chunks.append(decoded_chunk)

# Concatenate the decoded chunks
concatenated_data = b''.join(decoded_chunks)

# Decompress the concatenated data using gzip
try:
    decompressed_data = gzip.decompress(concatenated_data)
except Exception as e:
    print(f"Exception occurred during decompression: {e}")
    decompressed_data = None

if decompressed_data is not None:
    # Define the path to the output file (the original file)
    output_file_path = 'outputs/decoded/decoded_chunks_qros-dna.zip'

    # Write the decompressed data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decompressed_data)

    print(f"Decompressed data written to '{output_file_path}'.")
else:
    print("Decompression failed. Check the input data.")

# Begin final second file extractions

import json
import base64
import gzip

# Define the path to the 'chunks-v86wasm.json' file
chunks_json_path = 'outputs/decoded/decoded_chunks-file-v86wasm.json'

# Read the 'chunks.json' file to retrieve encoded data chunks
with open(chunks_json_path, 'r') as json_file:
    data = json.load(json_file)

# Extract the chunks from the JSON data
chunks = data.get('chunks', [])

# Initialize an empty list to hold decoded data chunks
decoded_chunks = []

# Decode each chunk from base64 and append to the list
for chunk in chunks:
    decoded_chunk = base64.urlsafe_b64decode(chunk)
    decoded_chunks.append(decoded_chunk)

# Concatenate the decoded chunks
concatenated_data = b''.join(decoded_chunks)

# Decompress the concatenated data using gzip
try:
    decompressed_data = gzip.decompress(concatenated_data)
except Exception as e:
    print(f"Exception occurred during decompression: {e}")
    decompressed_data = None

if decompressed_data is not None:
    # Define the path to the output file (the original file)
    output_file_path = 'outputs/decoded/decoded_chunks_v86.wasm'

    # Write the decompressed data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decompressed_data)

    print(f"Decompressed data written to '{output_file_path}'.")
else:
    print("Decompression failed. Check the input data.")