The `qros-dna-encoder.py` script performs the following tasks:

1. **Code Generation:** It generates DNA-like code representations for characters and character combinations ranging from one to four characters long. These generated mappings are used to encode text data.

2. **Text Encoding:** The script reads text data from an input file, applies consistent mappings using the generated DNA-like code, and outputs the mapped data to an output file. This process effectively encodes the text using the DNA-like code representations.

3. **Metadata Handling:** The script also handles metadata for the encoded data, including versioning and author information.

qros-dna-encoder:
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


words_four_or_more_times_filtered = {word: count for word, count in word_frequency_filtered.items() if count >= 4}


with open('output.txt', 'w') as file:
    file.write("{\n")
    for word, code in zip(words_four_or_more_times_filtered, generated_mappings):
        file.write(f"  '{word}':'_{code}',\n")
    file.write("}\n")


with open('output.txt', 'r') as file:
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

def read_and_process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines = [line.strip().lower() for line in lines if line.strip()]
    return ' '.join(lines)


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
                    cleaned_code_lines.append(line)  # Preserve lines with block comments
                    continue
                if in_block_comment:
                    cleaned_code_lines.append(line)  # Preserve lines within block comments
                    continue
                # Remove inline comments but preserve line
                cleaned_line = re.sub(r'#.*$', '', line)
                cleaned_code_lines.append(cleaned_line)
        return ''.join(cleaned_code_lines)

    def capture_raw_code(self, node, code_lines):
        start_line = node.lineno - 1
        end_line = node.end_lineno
        return "\n".join(code_lines[start_line:end_line]).strip()

    def parse_code_to_string(self, file_path):
        with open(file_path, 'r') as file:
            code_string = file.read()
            return code_string

    def create_code_entry(self):
        code_string = self.read_and_clean_file()
        if self.rna_dna_mapper:
            code_string = self.rna_dna_mapper.map_body(code_string)
            code_entry = {'code': code_string} # You can use any key you prefer instead of 'code'
        return code_entry

    def write_code_entry_to_json(self, code_entry):
        # Write the updated JSON data to the file with UTF-8 encoding
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(final_json_data, json_file, ensure_ascii=False, indent=4)

rna_dna_mapper = RNA_DNA_Mapper(generated_mappings, word_frequency_filtered)
file_path = 'qros-dna-readme.txt'  # Define your file path here
output_path = 'encoded_dna_data.json'  # Define your output path here
parser = CodeParser(file_path, output_path, rna_dna_mapper)

# Apply mappings to the code within initial_strand
initial_strand_code_entry = parser.create_code_entry()  # Create code entry
initial_strand_code = initial_strand_code_entry['code']  # Get the code from the entry
initial_strand_code = rna_dna_mapper.map_body(initial_strand_code)  # Apply mappings here and save

# Define the metadata for the initial strand
current_timestamp = datetime.datetime.now().isoformat()
initial_strand_metadata = {
    'metadata': {
        'version': '1.0',
        'author': 'AI',
        'description': 'Initial DNA strand with metadata and versioning',
        'timestamp': current_timestamp
    }
}

# Create the initial strand entry with code and metadata
initial_strand = {
    'code': initial_strand_code,
    'metadata': initial_strand_metadata
}

# Apply mappings to the code within dna_structure
dna_structure_code_entry = parser.create_code_entry()  # Create code entry
dna_structure_code = dna_structure_code_entry['code']  # Get the code from the entry
dna_structure_code = rna_dna_mapper.map_body(dna_structure_code)  # Apply mappings here and save

# Create the DNA structure entry with metadata
dna_structure = {
    'Genomes': {
        'Chromosomes': {
            'Genes': {
                'Nucleotide Sequences': {'code': dna_structure_code}  # Place mapped code here
            }
        }
    }
}

# Define the metadata for the DNA structure
dna_structure_metadata = {
    'metadata': {
        'version': '1.0',
        'author': 'AI',
        'description': 'DNA-like encoded software structure',
        'timestamp': current_timestamp
    }
}

# Apply mappings to the code within dna_structure
dna_structure_code = parser.create_code_entry()['code']
dna_structure_code = rna_dna_mapper.map_body(dna_structure_code)  # Apply mappings here and save

# Merging dna_structure and existing_json_data
final_json_data = {
    'dna_structure': dna_structure,
    'initial_strand': initial_strand,
    'second_strand': initial_strand_code_entry  # Use initial_strand_code_entry here
}
print("Debug: final_json_data:", final_json_data)

# Convert the mappings dictionary to a comma-separated line with underscore
mappings_line = ', '.join([f"'{key}': '{value}'" for key, value in rna_dna_mapper.mapping.items()])

# Define a dictionary with the mappings line
mappings_entry = {
    'mappings': f'{{{mappings_line}}}'
}

# Update the "dna_structure" dictionary with the "introns" entry
dna_structure['introns'] = mappings_entry

# Update the final JSON data with the modified "dna_structure"
final_json_data['dna_structure'] = dna_structure

# Write the updated JSON data to the file with UTF-8 encoding
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(final_json_data, json_file, ensure_ascii=False, indent=4)

# Define the path to the second file
second_file_path = 'qros-dna-encoder.py'  # Replace with the actual path to your second file

# Function to read and encode the content of the second file
def read_and_encode_second_file(file_path, rna_dna_mapper):
    with open(file_path, 'r') as file:
        code_string = file.read()
    # Apply mappings to the code in the second file
    encoded_code = rna_dna_mapper.map_body(code_string)
    return encoded_code

# Read and encode the content of the second file
encoded_second_file = read_and_encode_second_file(second_file_path, rna_dna_mapper)

# Update the "initial_strand" with the encoded content of the second file
initial_strand['code'] = encoded_second_file

# Ensure that the "Nucleotide Sequences" part remains the same

# Write the updated JSON data to the file with UTF-8 encoding
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(final_json_data, json_file, ensure_ascii=False, indent=4)

# Define the path to the third file
third_file_path = 'qros-dna-decoder.py'  # Replace with the actual path to your third file

# Read and encode the content of the third file
with open(third_file_path, 'r') as file:
    code_string = file.read()

# Apply mappings to the code in the third file
encoded_third_file = code_string
for key, value in rna_dna_mapper.mapping.items():
    encoded_third_file = encoded_third_file.replace(key, value)

# Update the "second_strand" with the encoded content of the third file
second_strand = {
    'code': encoded_third_file,
    'metadata': {
        'version': '1.0',
        'author': 'AI',
        'description': 'Second DNA strand with metadata and versioning',
        'timestamp': current_timestamp
    }
}

# Update the "second_strand" in the encoded_dna_data dictionary
encoded_dna_data = {
    'dna_structure': dna_structure,
    'initial_strand': initial_strand,
    'second_strand': initial_strand_code_entry  # Use initial_strand_code_entry here
}
print("Debug: final_json_data:", encoded_dna_data)

encoded_dna_data['second_strand'] = second_strand  # Define 'encoded_dna_data' before this line

# Write the updated JSON data to 'encoded_dna_data.json'
with open('encoded_dna_data.json', 'w') as json_file:
    json.dump(encoded_dna_data, json_file, indent=4)

qros-dna-decoder:

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
