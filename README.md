# qros-storage
This is a convergent repository for various qr code data storage projects with the goal of creating a single qr code (and text-based) storage solution.

## Use the following for the latest stable version:

https://github.com/txtatech/qros-storage/tree/main/qros-storage/qros-dna

## NOTE ON QROS-DNA:

# QROS-DNA Project

## What It Does

- Encodes and decodes text like DNA.
- Keeps track of version info and other metadata.
- Cleans and parses code files.
- Stores everything in a JSON file.
- Generates QR codes from encoded data.
- Creates videos from QR codes.

## Features

### Encoding and Decoding

- Maps common words to shorter versions.
- Can reverse the mapping to get original text back.

### Metadata

- Adds version, author, and timestamps to data.

### Code Parsing

- Removes comments from code.
- Stores cleaned code in a JSON file.

### JSON Structure

- Organized like DNA (Genomes > Chromosomes > Genes).
- Saves mappings in 'introns'.
- Can save other data in 'exons'.

### QR Code Generation

- Transforms encoded data into QR codes.
- Allows multiple QR codes for large data.

### Video Creation

- Combines QR codes into a video sequence.
- Can set video duration and transition effects.

### Reversibility

- Can decode data back to its original form.

## Brief description:

Generates DNA-like code representations for characters and character combinations ranging from one to four characters long. These generated mappings are used to encode text data.

It reads text data from an input file, applies consistent mappings using the generated DNA-like code, and outputs the mapped data to an output file. This process effectively encodes the text using the DNA-like code representations.

The main script also handles metadata for the encoded data, including versioning and author information.

## Usage:

Step 1:

~~~
python3 qros-dna-encoder.py
~~~

Step 2:

~~~
python3 qros-dna-decoder.py
~~~

# Example of 'QROS-DNA Encoded' JSON: *Changed since 0.0.2-alpha to have more entries.*
~~~
{
    "dna_structure": {
        "Genomes": {
            "Chromosomes": {
                "Genes": {
                    "Nucleotide Sequences": {
                        "code": "The `qros-_CTZA-encoder.py` _C _G _T<--...This is 'dna' encoded from a text file that creates the mappings."
                    }
                }
            }
        },
        "introns": {
            "mappings": "{'the': '_T', 'qrosdnaencoderpy': '_A',,<--...This is where the mappings are stored."
        },
        "exons": {
            "code": "var req_data = null;\nvar refreshTimeout = 0;<--...This is the un-encoded (as is) content of the 'web.js' javascript file.",
            "metadata": {
                "metadata": {
                    "version": "1.0",
                    "author": "AI",
                    "description": "DNA strand with metadata and versioning",
                    "timestamp": "2023-09-30T15:49:26.463244"
                }
            }
        },
        "files": {
            "code": "{\"chunks\": [\"H4sIAMF7GGUC_32a<--...This is the gziped, base64 encoded and chunked data of the 'qros-dna.zip' file...written in a JSON file as chunks.",
            "metadata": {
                "metadata": {
                    "version": "1.0",
                    "author": "AI",
                    "description": "DNA strand with metadata and versioning",
                    "timestamp": "2023-09-30T15:49:26.463244"
                }
            }
        }
    },
    "initial_strand": {
        "code": "# Begin _TAC _TTG\n\n_AAZ _ACT\n_AAZ<--...This is a 'dna encoder' python script that encodes this JSON",
        "metadata": {
            "metadata": {
                "version": "1.0",
                "author": "AI",
                "description": "DNA strand with metadata and versioning",
                "timestamp": "2023-09-30T15:49:26.463244"
            }
        }
    },
    "second_strand": {
        "code": "# Begin _TTCC _CT _CGZT _GAC _ACAA<--...This is a 'dna decoder' python script that decodes this JSON",
        "metadata": {
            "metadata": {
                "version": "1.0",
                "author": "AI",
                "description": "DNA strand with metadata and versioning",
                "timestamp": "2023-09-30T15:49:26.463244"
            }
        }
    }
}
~~~
The example JSON file, `encoded_dna_data-EXAMPLE.json`, has a complex nested structure. Below is a breakdown of its structure and what each part does:

### Root Level:

1. **dna_structure**: Encapsulates the core data structure meant to mimic a DNA structure.
    - **Genomes**: A further categorization within `dna_structure`.
        - **Chromosomes**: Another level of categorization.
            - **Genes**: The lowest level of this hierarchy.
                - **Nucleotide Sequences**: Contains the encoded code, which is a representation of another file's content in an encoded form.
                
2. **introns**: Stores the mappings used for encoding and decoding the code present in `dna_structure` and other strands. The mappings are stored as a string representation of a Python dictionary.

3. **exons**: Contains un-encoded JavaScript code (from the file `web.js`) and associated metadata.
    - **code**: The raw JavaScript code.
    - **metadata**: Additional information about this strand like version, author, description, and timestamp.

4. **files**: Contains compressed, base64 encoded, and chunked data (presumably from a ZIP file). It's also accompanied by metadata.
    - **code**: The compressed and encoded data.
    - **metadata**: Similar to the metadata in `exons`.

5. **initial_strand**: Stores encoded Python code and metadata for a Python script that presumably encodes this JSON structure.
    - **code**: The encoded Python code.
    - **metadata**: Metadata similar to that in `exons`.

6. **second_strand**: Similar to `initial_strand`, but this appears to be a Python script for decoding the JSON structure.
    - **code**: The encoded Python code for decoding.
    - **metadata**: Additional metadata similar to other strands.

### Summary of Content Types:

- **Encoded Python Code**: Found in `initial_strand` and `second_strand`.
- **Mappings for Encoding/Decoding**: Found in `introns`.
- **Encoded Text**: Found in `dna_structure`.
- **Raw JavaScript Code**: Found in `exons`.
- **Compressed and Encoded Data**: Found in `files`.

This structure allows the JSON file to act as a multi-layered container that holds various types of information, each with its own purpose and encoding logic. It can be used for:

1. **Data Obfuscation**: Encoded Python code and text.
2. **Data Compression**: Chunked and base64 encoded ZIP data.
3. **Data Integrity**: Through metadata for versioning and timestamping.
4. **Multi-language Support**: Holds Python and JavaScript code.
 
## End Note For QROS-DNA

### CURRENT GOALS

Using the `web.js`, `index.html`, and the JS shell from the JSON file as "live components" within the `encoded_dna_data-EXAMPLE.json` for a live architecture. 

Here's how they could function:

### web.js
This JavaScript file could serve as the "logic layer" for the web interface. It handles asynchronous data fetching and interacts with the DOM elements defined in `index.html`. When this component is "live" inside the JSON, it could be fetched and executed on-the-fly to control the web interface dynamically.

### index.html
This HTML file provides the structural skeleton of the web interface, with elements like a navigation bar and dark mode styles. When embedded as a "live" component in the JSON, it could be fetched and rendered to create the UI, ready to be manipulated by the `web.js`.

### JS Shell
This component might serve as an interactive terminal or command-line interface on the web. It could allow for real-time execution of JavaScript code, perhaps even interfacing with the other two components. When "live" in the JSON, it could be fetched and initialized to offer an interactive shell within the web interface.

### Interactions
These "live components" could be fetched from the JSON dynamically to assemble a working web interface. They would not be static but could interact with each other:

- `web.js` would manipulate the `index.html` DOM elements.
- The JS shell could execute commands that invoke functions from `web.js` or manipulate the `index.html` elements.

The JSON file, in this case, serves not just as a data store but as a dynamic repository that can deploy a fully functional web interface. This approach allows for a highly modular and portable system, encapsulating code and data in a single JSON structure. 

### Related Projects:

# qros-builder-webby 

https://github.com/txtatech/qros-builder-webby

A cross platform linux distribution built with qr code videos that can be loaded in a browser. This is just the base system with all the qr code videos and required scripts to utilize the os in a browser.

# qros-builder-vid

https://github.com/txtatech/qros-builder-vid

Builds KolibriOS from qr codes embedded in a video and launches the small assembly written OS in qemu.

# qros-builder

https://github.com/txtatech/qros-builder-vid

Also builds KolibriOS from qr codes and launches the small assembly written OS in qemu.

# qr-vid-gui

https://github.com/txtatech/qr-vid-gui

GUI version of a method to extract code from qr codes in a video, output it to a live python editor, the terminal and a text file.

# qr-vid

https://github.com/txtatech/qr-vid

A method to extract code from qr codes in a video, output it to a live python editor, the terminal and a text file.

# qr-gif

https://github.com/txtatech/qr-gif

A method to extract code (javascript in this example) from qr codes in an animated gif, print it to the terminal and output it as a text file.

# frac-crawl

https://github.com/txtatech/frac-crawl

A fractal encoding framework written in Python that generates fractal images based on a given text input, builds a central ledger, and updates the metadata of the images. It then builds a JSON lattice with a coordinate mapping system to create a seamless self-referencing fractal terrain.

# fractal-encoder

https://github.com/txtatech/fractal-encoder

A fractal encoding framework for fractal encoding text, lattice structuring, ASCII art qr code generation, 3D QR code and fractal grid generation plus mappings for programmable terrain.

# virtual-forest/game_instance_sandbox/djinn-dna 

This is a sub-project of the [virtual-forest](https://github.com/txtatech/virtual-forest) project.

The DNA encoding framework source files are in 'game_instance_sandbox/djinn-dna':

https://github.com/txtatech/virtual-forest/tree/main/virtual-forest/game_instance_sandbox/djinn-dna

Djinn-DNA Note: The README-DNA.txt explains the steps involved.
