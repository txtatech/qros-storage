The `qros-dna-encoder.py` script performs the following tasks:

1. **Code Generation:** It generates DNA-like code representations for characters and character combinations ranging from one to four characters long. These generated mappings are used to encode text data.

2. **Text Encoding:** The script reads text data from an input file, applies consistent mappings using the generated DNA-like code, and outputs the mapped data to an output file. This process effectively encodes the text using the DNA-like code representations.

3. **Metadata Handling:** The script also handles metadata for the encoded data, including versioning and author information.

Usage:

Step 1:

python3 qros-dna-encoder.py

Step 2:

python3 qros-dna-decoder.py

qros-dna-encoder:



import cv2
import numpy as np
import qrcode
import gzip
import base64
import os
import json
import time  

def generate_qr_code(data):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERRORscriptORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_cv = np.array(img.convert('RGB'))
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

    
    img_cv = cv2.resize(img_cv, (730, 730))

    return img_cv

def compress_and_generate_base64_qr_images(file_path, chunk_size=1500):
    with open(file_path, 'rb') as f:
        data = f.read()

    compressed_data = gzip.compress(data)
    encoded_data_base64 = base64.urlsafe_b64encode(compressed_data).decode("utf-8")

    print(f"Total size of base64 data before splitting: {len(encoded_data_base64)}")

    chunks = [encoded_data_base64[i:i+chunk_size] for i in range(0, len(encoded_data_base64), chunk_size)]

    
    with open('file-chunks.json', 'w') as json_file:
        json.dump({"chunks": chunks}, json_file)  

    os.makedirs('file-qrs', exist_ok=True)  

    for i, chunk in enumerate(chunks):
        print(f"Size of chunk {i}: {len(chunk)}")

        qr_img = generate_qr_code(chunk)

        cv2.imwrite(f'file-qrs/qr_{i:09d}.png', qr_img)  

img_file_path = 'qros-dna.zip'
compress_and_generate_base64_qr_images(img_file_path)


os.system('ffmpeg -framerate 30 -i file-qrs/qr_%09d.png -vf "scale=730:730,setsar=1" -an -c:v libx264 -pix_fmt yuv420p qros-dna-zip-file.mp4')



import cv2
from pyzbar.pyzbar import decode
import base64
import gzip


video_capture = cv2.VideoCapture('qros-dna-zip-file.mp4')

def safe_base64_decode(data):
    if isinstance(data, str):
        
        return data
    try:
        data = data.decode("utf-8")  
    except UnicodeDecodeError:
        
        return data
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    try:
        return base64.urlsafe_b64decode(data)
    except Exception as e:
        print(f"Exception during decoding: {e}")
        print(f"Data: {data}")
        return None


data_chunks = []
prev_chunk = None

while True:
    
    ret, frame = video_capture.read()

    
    if not ret:
        break

    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    decoded_objects = decode(gray_frame)

    
    for obj in decoded_objects:
        decoded_data = safe_base64_decode(obj.data)
        if decoded_data is not None and decoded_data != prev_chunk:
            data_chunks.append(decoded_data)
            prev_chunk = decoded_data

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Finished processing frames, releasing video capture...")
video_capture.release()

print("Concatenating and decompressing data...")
data = b''.join(data_chunks)

try:
    
    decompressed_data = gzip.decompress(data)
    with open("decoded_qros-dna.zip", "wb") as out_file:
        out_file.write(decompressed_data)
    print("Data decompressed and written to 'decoded_qros-dna.zip'.")
except Exception as e:
    print(f"Exception occurred during decompression: {e}")

print("Finished.")



import re
import ast
import json
import datetime


characters = ['T', 'A', 'C', 'G', 'Z']
combinations = [f"{char}" for char in characters]


generated_mappings = []


generated_mappings.extend(combinations)


generated_mappings.extend([f"{char1}{char2}" for char1 in combinations for char2 in combinations])


generated_mappings.extend([f"{char1}{char2}{char3}" for char1 in combinations for char2 in combinations for char3 in combinations])


generated_mappings.extend([f"{char1}{char2}{char3}{char4}" for char1 in combinations for char2 in combinations for char3 in combinations for char4 in combinations])


word_frequency_filtered = {}


with open('qros-dna-readme.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word = re.sub(r'[^\w\s]', '', word).lower()  
            if word.strip():  
                word_frequency_filtered[word] = word_frequency_filtered.get(word, 0) + 1


words_four_or_more_times_filtered = {word: count for word, count in word_frequency_filtered.items() if count >= 2}


with open('mappings.txt', 'w') as file:
    file.write("{\n")
    for word, code in zip(words_four_or_more_times_filtered, generated_mappings):
        file.write(f"  '{word}':'_{code}',\n")
    file.write("}\n")


with open('mappings.txt', 'r') as file:
    mapping = eval(file.read())


reverse_mapping = {v.strip("'_"): k for k, v in mapping.items()}


with open('reverse-mappings.txt', 'w') as file:
    file.write("{\n")
    for code, word in reverse_mapping.items():
        file.write(f"  '_{code}':'{word}',\n")
    file.write("}\n")



import re
import ast
import json
import datetime


def read_and_process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines = [line.strip().lower() for line in lines if line.strip()]
    return ' '.join(lines)


class RNA_DNA_Mapper:
    def __init__(self, generated_mappings, word_frequency_filtered):
        self.mapping = {word: f"_{code}" for word, code in zip(word_frequency_filtered.keys(), generated_mappings)}

    def map_body(self, body):
        original_body = body
        for construct, shorthand in self.mapping.items():
            replaced_body = re.sub(r'\b' + re.escape(construct) + r'\b', shorthand, body)
            if replaced_body != body:
                print(f"Replaced: {construct} -> {shorthand}")
            body = replaced_body
        if original_body == body:
            print("All mappings used. Appending remaining content as-is.")
        return body


rna_dna_mapper = RNA_DNA_Mapper(generated_mappings, word_frequency_filtered)

class CodeParser:
    def __init__(self, file_path, output_path, rna_dna_mapper):
        self.file_path = file_path
        self.output_path = output_path
        self.rna_dna_mapper = rna_dna_mapper

    def read_and_clean_file(self):
        cleaned_code_lines = []
        in_block_comment = False
        with open(self.file_path, 'r') as file:
            for line in file:
                if '"""' in line or "'''" in line:
                    in_block_comment = not in_block_comment
                    cleaned_code_lines.append(line)
                    continue
                if in_block_comment:
                    cleaned_code_lines.append(line)
                    continue
                cleaned_line = re.sub(r'#.*$', '', line)
                cleaned_code_lines.append(cleaned_line)
        return ''.join(cleaned_code_lines)

    def create_code_entry(self):
        code_string = self.read_and_clean_file()
        if self.rna_dna_mapper:
            code_string = self.rna_dna_mapper.map_body(code_string)
            code_entry = {'code': code_string}
        return code_entry

    def write_code_entry_to_json(self, code_entry):
        with open(self.output_path, 'w', encoding='utf-8') as json_file:
            json.dump(code_entry, json_file, ensure_ascii=False, indent=4)

# Initialize CodeParser
file_path = 'qros-dna-readme.txt'
output_path = 'encoded_dna_data.json'
parser = CodeParser(file_path, output_path, rna_dna_mapper)

# Process initial_strand
initial_strand_code_entry = parser.create_code_entry()
initial_strand_code = initial_strand_code_entry['code']
initial_strand_code = rna_dna_mapper.map_body(initial_strand_code)

# Metadata
current_timestamp = datetime.datetime.now().isoformat()
initial_strand_metadata = {
    'metadata': {
        'version': '1.0',
        'author': 'AI',
        'description': 'DNA strand with metadata and versioning',
        'timestamp': current_timestamp
    }
}

initial_strand = {
    'code': initial_strand_code,
    'metadata': initial_strand_metadata
}

# Process dna_structure
dna_structure_code_entry = parser.create_code_entry()
dna_structure_code = dna_structure_code_entry['code']
dna_structure_code = rna_dna_mapper.map_body(dna_structure_code)

dna_structure = {
    'Genomes': {
        'Chromosomes': {
            'Genes': {
                'Nucleotide Sequences': {'code': dna_structure_code}
            }
        }
    }
}

# Final JSON Data
final_json_data = {
    'dna_structure': dna_structure,
    'initial_strand': initial_strand
}

# Add mappings as introns
mappings_line = ', '.join([f"'{key}': '{value}'" for key, value in rna_dna_mapper.mapping.items()])
mappings_entry = {
    'mappings': f'{{{mappings_line}}}'
}
dna_structure['introns'] = mappings_entry

# Handle second_file_path
second_file_path = 'qros-dna-encoder.py'
def read_and_encode_second_file(file_path, rna_dna_mapper):
    with open(file_path, 'r') as file:
        code_string = file.read()
    encoded_code = rna_dna_mapper.map_body(code_string)
    return encoded_code

encoded_second_file = read_and_encode_second_file(second_file_path, rna_dna_mapper)
initial_strand['code'] = encoded_second_file

# Handle third_file_path
third_file_path = 'qros-dna-decoder.py'
with open(third_file_path, 'r') as file:
    code_string = file.read()
encoded_third_file = rna_dna_mapper.map_body(code_string)

second_strand = {
    'code': encoded_third_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

final_json_data['second_strand'] = second_strand

# Handle fourth_file_path
fourth_file_path = 'web.js'  # Replace with the actual path to your fourth file

def read_fourth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the fourth file
plain_fourth_file = read_fourth_file(fourth_file_path)

# Add the content of the fourth file to the 'exons' entry in 'dna_structure'
dna_structure['exons'] = {
    'code': plain_fourth_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

# Begin file addition

# Handle fourth_file_path
fifth_file_path = 'file-chunks.json'  # Replace with the actual path to your fourth file

def read_fifth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the fourth file
plain_fifth_file = read_fifth_file(fifth_file_path)

# Add the content of the fifth file to the 'exons' entry in 'dna_structure'
dna_structure['files'] = {
    'code': plain_fifth_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

# Write to JSON
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(final_json_data, json_file, ensure_ascii=False, indent=4)

# Begin generating .png qr codes, 'chunks.json' and creating a qr code .mp4 video from 'encoded_dna_data.json'

import cv2
import numpy as np
import qrcode
import gzip
import base64
import os
import json
import time  # For adding delay

def generate_qr_code(data):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERRORscriptORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_cv = np.array(img.convert('RGB'))
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

    # Resize the image to 730x730
    img_cv = cv2.resize(img_cv, (730, 730))

    return img_cv

def compress_and_generate_base64_qr_images(file_path, chunk_size=1500):
    with open(file_path, 'rb') as f:
        data = f.read()

    compressed_data = gzip.compress(data)
    encoded_data_base64 = base64.urlsafe_b64encode(compressed_data).decode("utf-8")

    print(f"Total size of base64 data before splitting: {len(encoded_data_base64)}")

    chunks = [encoded_data_base64[i:i+chunk_size] for i in range(0, len(encoded_data_base64), chunk_size)]

    # Write chunks to a JSON file
    with open('chunks.json', 'w') as json_file:
        json.dump({"chunks": chunks}, json_file)  # Save the chunks as an array within a JSON object

    os.makedirs('qrs', exist_ok=True)  # Create the directory if it doesn't exist

    for i, chunk in enumerate(chunks):
        print(f"Size of chunk {i}: {len(chunk)}")

        qr_img = generate_qr_code(chunk)

        cv2.imwrite(f'qrs/qr_{i:09d}.png', qr_img)  # Save each QR code as a PNG file

img_file_path = 'encoded_dna_data.json'
compress_and_generate_base64_qr_images(img_file_path)

# Add ffmpeg command to generate the video
os.system('ffmpeg -framerate 30 -i qrs/qr_%09d.png -vf "scale=730:730,setsar=1" -an -c:v libx264 -pix_fmt yuv420p encoded_dna_data.mp4')

# Begin decoding video file and generating 'decoded_encoded_dna_integrity.json'

import cv2
from pyzbar.pyzbar import decode
import base64
import gzip

# Open the video capture
video_capture = cv2.VideoCapture('encoded_dna_data.mp4')

def safe_base64_decode(data):
    if isinstance(data, str):
        # If data is already a string, it doesn't need to be decoded
        return data
    try:
        data = data.decode("utf-8")  # Decode the bytes to a string
    except UnicodeDecodeError:
        # If data is not valid UTF-8, it's probably already decoded
        return data
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    try:
        return base64.urlsafe_b64decode(data)
    except Exception as e:
        print(f"Exception during decoding: {e}")
        print(f"Data: {data}")
        return None

# Initialize an empty list to hold the data from each QR code in the video
data_chunks = []
prev_chunk = None

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode QR codes from the frame
    decoded_objects = decode(gray_frame)

    # Process the decoded data and append to data_chunks
    for obj in decoded_objects:
        decoded_data = safe_base64_decode(obj.data)
        if decoded_data is not None and decoded_data != prev_chunk:
            data_chunks.append(decoded_data)
            prev_chunk = decoded_data

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Finished processing frames, releasing video capture...")
video_capture.release()

print("Concatenating and decompressing data...")
data = b''.join(data_chunks)

try:
    # Decompress the full data
    decompressed_data = gzip.decompress(data)
    with open("decoded_encoded_dna_integrity.json", "wb") as out_file:
        out_file.write(decompressed_data)
    print("Data decompressed and written to 'decoded_encoded_dna_integrity.json'.")
except Exception as e:
    print(f"Exception occurred during decompression: {e}")

print("Finished.")

qros-dna-decoder:

# Begin decoding and reconstruction of original files from encoded_dna_data.json

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
with open('encoded_dna_data.json', 'r') as json_file:
    encoded_dna_data = json.load(json_file)

# Extract encoded data and mappings
encoded_dna_structure = encoded_dna_data['dna_structure']['Genomes']['Chromosomes']['Genes']['Nucleotide Sequences']['code']
encoded_initial_strand = encoded_dna_data['initial_strand']['code']
encoded_second_strand = encoded_dna_data['second_strand']['code']
mappings_str = encoded_dna_data['dna_structure']['introns']['mappings']
non_encoded_fourth_file = encoded_dna_data['dna_structure']['exons']['code']  # New line for fourth file
non_encoded_fifth_file = encoded_dna_data['dna_structure']['files']['code']  # New line for fourth file

# Parse the string representation of mappings into a Python dictionary
mappings = ast.literal_eval(mappings_str)

# Step 2: Reverse the mappings
reversed_mappings = reverse_mappings(mappings)

# Step 3: Decode the data
decoded_dna_structure = decode_body(encoded_dna_structure, reversed_mappings)
decoded_initial_strand = decode_body(encoded_initial_strand, reversed_mappings)
decoded_second_strand = decode_body(encoded_second_strand, reversed_mappings)

# Step 4: Write the decoded content to new files
with open('decoded_qros-dna-readme.txt', 'w') as file:
    file.write(decoded_dna_structure)

with open('decoded_qros-dna-encoder.py', 'w') as file:
    file.write(decoded_initial_strand)

with open('decoded_qros-dna-decoder.py', 'w') as file:
    file.write(decoded_second_strand)

with open('decoded_web.js', 'w') as file:
    file.write(non_encoded_fourth_file)

with open('decoded_file-chunks.json', 'w') as file:
    file.write(non_encoded_fifth_file)

# Begin chunks.json decoder
 
import json
import base64
import gzip

# Define the path to the 'chunks.json' file
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
    output_file_path = 'decoded_chunks_file.json'

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
with open('decoded_chunks_file.json', 'r') as json_file:
    encoded_dna_data = json.load(json_file)

# Extract encoded data and mappings
encoded_dna_structure = encoded_dna_data['dna_structure']['Genomes']['Chromosomes']['Genes']['Nucleotide Sequences']['code']
encoded_initial_strand = encoded_dna_data['initial_strand']['code']
encoded_second_strand = encoded_dna_data['second_strand']['code']
non_encoded_fourth_file = encoded_dna_data['dna_structure']['exons']['code']  # New line for fourth file
mappings_str = encoded_dna_data['dna_structure']['introns']['mappings']
non_encoded_fifth_file = encoded_dna_data['dna_structure']['files']['code']  # New line for fourth file

# Parse the string representation of mappings into a Python dictionary
mappings = ast.literal_eval(mappings_str)

# Step 2: Reverse the mappings
reversed_mappings = reverse_mappings(mappings)

# Step 3: Decode the data
decoded_dna_structure = decode_body(encoded_dna_structure, reversed_mappings)
decoded_initial_strand = decode_body(encoded_initial_strand, reversed_mappings)
decoded_second_strand = decode_body(encoded_second_strand, reversed_mappings)

# Step 4: Write the decoded content to new files
with open('decoded_qros-dna-chunks-readme.txt', 'w') as file:
    file.write(decoded_dna_structure)

with open('decoded_qros-dna-chunks-encoder.py', 'w') as file:
    file.write(decoded_initial_strand)

with open('decoded_qros-dna-chunks-decoder.py', 'w') as file:
    file.write(decoded_second_strand)

with open('decoded_chunks-web.js', 'w') as file:
    file.write(non_encoded_fourth_file)

with open('decoded_chunks-file-chunks.json', 'w') as file:
    file.write(non_encoded_fifth_file)

# Begin final file extraction

import json
import base64
import gzip

# Define the path to the 'chunks.json' file
chunks_json_path = 'decoded_chunks-file-chunks.json'

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
    output_file_path = 'decoded_chunks_qros-dna.zip'

    # Write the decompressed data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decompressed_data)

    print(f"Decompressed data written to '{output_file_path}'.")
else:
    print("Decompression failed. Check the input data.")