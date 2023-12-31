# Begin encoding a WASM file to qr code images and qr code video
# Tested file types are ZIP IMG ISO TXT WASM JS HTML but other types may work

import cv2
import numpy as np
import qrcode
import gzip
import base64
import os
import json
import time  # For adding delay

os.makedirs('outputs', exist_ok=True)  # Create the directory if it doesn't exist
os.makedirs('outputs/decoded', exist_ok=True)  # Create the directory if it doesn't exist
os.makedirs('outputs/file-qrs2', exist_ok=True)  # Create the directory if it doesn't exist

def generate_qr_code(data):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
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
    with open('outputs/file-v86wasm.json', 'w') as json_file:
        json.dump({"chunks": chunks}, json_file)  # Save the chunks as an array within a JSON object

    for i, chunk in enumerate(chunks):
        print(f"Size of chunk {i}: {len(chunk)}")

        qr_img = generate_qr_code(chunk)

        cv2.imwrite(f'outputs/file-qrs2/qr_{i:09d}.png', qr_img)  # Save each QR code as a PNG file

img_file_path = 'inputs/emu/v86.wasm'
compress_and_generate_base64_qr_images(img_file_path)

# Add ffmpeg command to generate the video
os.system('ffmpeg -framerate 30 -i outputs/file-qrs2/qr_%09d.png -vf "scale=730:730,setsar=1" -an -c:v libx264 -pix_fmt yuv420p outputs/file-v86.wasm.mp4')

import cv2
from pyzbar.pyzbar import decode
import base64
import gzip

# Open the video capture
video_capture = cv2.VideoCapture('outputs/file-v86.wasm.mp4')

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
    with open("outputs/decoded/decoded_file-v86.wasm", "wb") as out_file:
        out_file.write(decompressed_data)
    print("Data decompressed and written to 'outputs/decoded/decoded_file-v86.wasm'.")
except Exception as e:
    print(f"Exception occurred during decompression: {e}")

print("Finished.")

# Begin encoding a file to qr code images and qr code video
# Tested file types are ZIP IMG ISO TXT but other types may work

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
        error_correction=qrcode.constants.ERROR_CORRECT_M,
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
    with open('outputs/file-qros-dna-zip.json', 'w') as json_file:
        json.dump({"chunks": chunks}, json_file)  # Save the chunks as an array within a JSON object

    os.makedirs('outputs/file-qrs1', exist_ok=True)  # Create the directory if it doesn't exist

    for i, chunk in enumerate(chunks):
        print(f"Size of chunk {i}: {len(chunk)}")

        qr_img = generate_qr_code(chunk)

        cv2.imwrite(f'outputs/file-qrs1/qr_{i:09d}.png', qr_img)  # Save each QR code as a PNG file

img_file_path = 'inputs/files/qros-dna.zip'
compress_and_generate_base64_qr_images(img_file_path)

# Add ffmpeg command to generate the video
os.system('ffmpeg -framerate 30 -i outputs/file-qrs1/qr_%09d.png -vf "scale=730:730,setsar=1" -an -c:v libx264 -pix_fmt yuv420p outputs/file-qros-dna-zip.mp4')

# Begin decoding video file and generating 'decoded_qros-dna.zip'

import cv2
from pyzbar.pyzbar import decode
import base64
import gzip

# Open the video capture
video_capture = cv2.VideoCapture('outputs/file-qros-dna-zip.mp4')

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
    with open("outputs/decoded/decoded_qros-dna.zip", "wb") as out_file:
        out_file.write(decompressed_data)
    print("Data decompressed and written to 'outputs/decoded/decoded_qros-dna.zip'.")
except Exception as e:
    print(f"Exception occurred during decompression: {e}")

print("Finished.")

# Begin reading file 'qros-dna-readme.txt' and generating mappings

import re
import ast
import json
import datetime

# Generating all possible combinations of 'T', 'A', 'C', 'G' and 'Z' ranging from one to five characters long
characters = ['T', 'A', 'C', 'G', 'Z']
combinations = [f"{char}" for char in characters]

# Initialize a list to store mappings
generated_mappings = []

# Generate mappings for single characters
generated_mappings.extend(combinations)

# Generate mappings for combinations of two characters
generated_mappings.extend([f"{char1}{char2}" for char1 in combinations for char2 in combinations])

# Generate mappings for combinations of three characters
generated_mappings.extend([f"{char1}{char2}{char3}" for char1 in combinations for char2 in combinations for char3 in combinations])

# Generate mappings for combinations of four characters
generated_mappings.extend([f"{char1}{char2}{char3}{char4}" for char1 in combinations for char2 in combinations for char3 in combinations for char4 in combinations])

# Generate mappings for combinations of five characters
generated_mappings.extend([f"{char1}{char2}{char3}{char4}{char5}" for char1 in combinations for char2 in combinations for char3 in combinations for char4 in combinations for char5 in combinations])

# Initialize a dictionary to store word counts
word_frequency_filtered = {}

# Reading the 'qros-dna-readme.txt' file and counting occurrences of non-empty words
# A text file containing all the code and text that are to be encoded will boost the number of generated mappings
# The below can be any file that you want to create mappings from
with open('inputs/dna/qros-dna-readme.txt', 'r') as file: 
    for line in file:
        words = line.split()
        for word in words:
            word = re.sub(r'[^\w\s]', '', word).lower()  # Removing punctuation and converting to lowercase
            if word.strip():  # Excluding empty strings or whitespace
                word_frequency_filtered[word] = word_frequency_filtered.get(word, 0) + 1

# Filtering words that occur two or more times
# The word frequency count can be set to any number but the default is four
words_four_or_more_times_filtered = {word: count for word, count in word_frequency_filtered.items() if count >= 2}

# Writing the generated key-value pairs to 'mappings.txt' for redundancy
with open('outputs/dna-mappings.txt', 'w') as file:
    file.write("{\n")
    for word, code in zip(words_four_or_more_times_filtered, generated_mappings):
        file.write(f"  '{word}':'_{code}',\n")
    file.write("}\n")

# Read the original mappings from 'mappings.txt' and reverse it
with open('outputs/dna-mappings.txt', 'r') as file:
    mapping = eval(file.read())

# Create the reverse mappings
reverse_mapping = {v.strip("'_"): k for k, v in mapping.items()}

# Write the reversed mappings to 'reverse-mappings.txt' for redundancy
with open('outputs/dna-reverse-mappings.txt', 'w') as file:
    file.write("{\n")
    for code, word in reverse_mapping.items():
        file.write(f"  '_{code}':'{word}',\n")
    file.write("}\n")

# Begin applying mappings and writing encoded files to JSON

import re
import ast
import json
import datetime

# Function for consistent text processing
def read_and_process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines = [line.strip().lower() for line in lines if line.strip()]
    return ' '.join(lines)

# RNA_DNA_Mapper class definition
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

# Initialize RNA_DNA_Mapper
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
# Below is the same file that is read to create the mappings
# The text gets written to JSON at 'Nucleotide Sequences': 'code':
file_path = 'inputs/dna/qros-dna-readme.txt'
output_path = 'outputs/encoded_dna_data.json'
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
second_file_path = 'inputs/strands/qros-dna-combos.sh'
def read_and_encode_second_file(file_path, rna_dna_mapper):
    with open(file_path, 'r') as file:
        code_string = file.read()
    encoded_code = rna_dna_mapper.map_body(code_string)
    return encoded_code

encoded_second_file = read_and_encode_second_file(second_file_path, rna_dna_mapper)
initial_strand['code'] = encoded_second_file

# Handle third_file_path
third_file_path = 'inputs/strands/qros-dna-txt-split.sh'
with open(third_file_path, 'r') as file:
    code_string = file.read()
encoded_third_file = rna_dna_mapper.map_body(code_string)

second_strand = {
    'code': encoded_third_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

final_json_data['second_strand'] = second_strand

# Handle fourth_file_path
fourth_file_path = 'inputs/exons/0web.js'  # Replace with the actual path to your fourth file

def read_fourth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the fourth file
plain_fourth_file = read_fourth_file(fourth_file_path)

# Add the content of the thirteenth file to the 'exons' entry in 'dna_structure'
dna_structure['exons'] = {
    '0js': plain_fourth_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

# Begin file addition

# Handle fifth_file_path
fifth_file_path = 'outputs/file-qros-dna-zip.json'  # Replace with the actual path to your fifth file

def read_fifth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the fifth file
plain_fifth_file = read_fifth_file(fifth_file_path)

# Add the content of the fifth file to the 'files' entry in 'dna_structure'
dna_structure['files'] = {
    'code': plain_fifth_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

# Handle sixth_file_path
sixth_file_path = 'inputs/profusion/index.html'  # Replace with the actual path to your sixth file

def read_sixth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the sixth file
plain_sixth_file = read_sixth_file(sixth_file_path)

# Add the content of the sixth file to the 'exons' entry in 'dna_structure'
dna_structure['profusion'] = {
    'code': plain_sixth_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

# Handle seventh_file_path
seventh_file_path = 'qros-dna-encoder.py'
def read_and_encode_seventh_file(file_path, rna_dna_mapper):
    with open(file_path, 'r') as file:
        code_string = file.read()
    encoded_code = rna_dna_mapper.map_body(code_string)
    return encoded_code

third_strand = {}

encoded_seventh_file = read_and_encode_seventh_file(seventh_file_path, rna_dna_mapper)
third_strand['encoded-encoder'] = encoded_seventh_file

# Handle eighth_file_path
eighth_file_path = 'qros-dna-decoder.py'
with open(eighth_file_path, 'r') as file:
    code_string = file.read()
encoded_eighth_file = rna_dna_mapper.map_body(code_string)

# Handle ninth_file_path
ninth_file_path = 'inputs/strands/js-shell.html'  # Replace with the actual path to your ninth file

def read_ninth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the ninth file
plain_ninth_file = read_ninth_file(ninth_file_path)

# Handle tenth_file_path
tenth_file_path = 'qros-dna-decoder.py'  # Replace with the actual path to your tenth file

def read_tenth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the tenth file
plain_tenth_file = read_tenth_file(tenth_file_path)

third_strand = {
    'js-shell': plain_ninth_file,
    'encoded-encoder': encoded_seventh_file,
    'encoded-decoder': encoded_eighth_file,
    'decoder': plain_tenth_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

final_json_data['third_strand'] = third_strand

# Handle eleventh_file_path
eleventh_file_path = 'inputs/emu/libv86.js'  # Replace with the actual path to your eleventh file

def read_eleventh_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the eleventh file
plain_eleventh_file = read_eleventh_file(eleventh_file_path)

# Handle twelfth_file_path
twelfth_file_path = 'outputs/file-v86wasm.json'  # Replace with the actual path to your twelfth file

def read_twelfth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the twelfth file
plain_twelfth_file = read_twelfth_file(twelfth_file_path)

# Handle thirteenth_file_path
thirteenth_file_path = 'inputs/exons/0shell.html'  # Replace with the actual path to your thirteenth file

def read_thirteenth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the thirteenth file
plain_thirteenth_file = read_thirteenth_file(thirteenth_file_path)

# Handle fourteenth_file_path
fourteenth_file_path = 'inputs/exons/0index.html'  # Replace with the actual path to your fourteenth file

def read_fourteenth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the fourteenth file
plain_fourteenth_file = read_fourteenth_file(fourteenth_file_path)

# Add the content of the fourteenth file to the 'exons' entry in 'dna_structure'
dna_structure['exons'] = {
    '0shell': plain_thirteenth_file,
    '0js': plain_fourth_file,
    '0html': plain_fourteenth_file,
    'metadata': initial_strand_metadata  # Reusing initial_strand_metadata for example
}

# Handle fifteenth_file_path
fifteenth_file_path = 'inputs/emu/async_load.html'  # Replace with the actual path to your fifteenth file

def read_fifteenth_file(file_path):
    with open(file_path, 'r') as file:
        code_string = file.read()
    return code_string

# Read the content of the fifteenth file
plain_fifteenth_file = read_fifteenth_file(fifteenth_file_path)

# Add the content of the fifteenth file to the 'emu' entry in 'dna_structure'
dna_structure['emu'] = {
    'loader': plain_fifteenth_file,
    'libv86': plain_eleventh_file,
    'v86wasm': plain_twelfth_file
}

# Write to JSON
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(final_json_data, json_file, ensure_ascii=False, indent=4)

# Once the above is complete everything has been written to 'encoded_dna_data.json'

# Begin generating .png qr codes, 'chunks.json' and creating a qr code .mp4 video from 'encoded_dna_data.json'
# All files can be reconstructed independently the reconstruction archives are on the following line
# chunks.json, encoded_dna_data.json, encoded_dna_data.mp4, decoded_encoded_dna_integrity.json and the qr codes in the dna-qrs directory

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
        error_correction=qrcode.constants.ERROR_CORRECT_M,
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
    with open('outputs/chunks.json', 'w') as json_file:
        json.dump({"chunks": chunks}, json_file)  # Save the chunks as an array within a JSON object

    os.makedirs('outputs/dna-qrs', exist_ok=True)  # Create the directory if it doesn't exist

    for i, chunk in enumerate(chunks):
        print(f"Size of chunk {i}: {len(chunk)}")

        qr_img = generate_qr_code(chunk)

        cv2.imwrite(f'outputs/dna-qrs/qr_{i:09d}.png', qr_img)  # Save each QR code as a PNG file

img_file_path = 'outputs/encoded_dna_data.json'
compress_and_generate_base64_qr_images(img_file_path)

# Add ffmpeg command to generate the video
os.system('ffmpeg -framerate 30 -i outputs/dna-qrs/qr_%09d.png -vf "scale=730:730,setsar=1" -an -c:v libx264 -pix_fmt yuv420p outputs/encoded_dna_data.mp4')

# Begin decoding video file and generating 'decoded_encoded_dna_integrity.json'

import cv2
from pyzbar.pyzbar import decode
import base64
import gzip

# Open the video capture
video_capture = cv2.VideoCapture('outputs/encoded_dna_data.mp4')

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
    with open("outputs/decoded/decoded_encoded_dna_integrity.json", "wb") as out_file:
        out_file.write(decompressed_data)
    print("Data decompressed and written to 'outputs/decoded/decoded_encoded_dna_integrity.json'.")
except Exception as e:
    print(f"Exception occurred during decompression: {e}")

print("Finished.")