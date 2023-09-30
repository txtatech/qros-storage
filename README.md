# qros-storage
This is a convergent repository for various qr code data storage projects with the goal of creating a single qr code (and text-based) storage solution.

## Use the following for the latest stable version:

https://github.com/txtatech/qros-storage/tree/main/qros-storage/qros-dna

## NOTE ON QROS-DNA:

Generates DNA-like code representations for characters and character combinations ranging from one to four characters long. These generated mappings are used to encode text data.

It reads text data from an input file, applies consistent mappings using the generated DNA-like code, and outputs the mapped data to an output file. This process effectively encodes the text using the DNA-like code representations.

The main script also handles metadata for the encoded data, including versioning and author information.

Usage:

Step 1:

python3 qros-dna-encoder.py

Step 2:

python3 qros-dna-decoder.py

# Example of 'QROS-DNA Encoded' JSON:
~~~
{
    "dna_structure": {
        "Genomes": {
            "Chromosomes": {
                "Genes": {
                    "Nucleotide Sequences": {
                        "code": "The `qros-_ATGG-encoder.py` _C _G _T _Z<--...This is dna encoded from a text file that creates the mappings."
                    }
                }
            }
        },
        "introns": {
            "mappings": "{'the': '_T', 'qrosdnaencoderpy': '_A',<--...This is where the mappings are stored."
        },
        "exons": {
            "code": "/*! For license information please<--...This is the un-encoded (as is) conent of the 'web.js' javascript file.",
            "metadata": {
                "metadata": {
                    "version": "1.0",
                    "author": "AI",
                    "description": "DNA strand with metadata and versioning",
                    "timestamp": "2023-09-30T14:35:37.461583"
                }
            }
        },
        "files": {
            "code": "{\"chunks\": [\"H4sIABNqGGUC_4S4<--...This is the gziped, base64 encoded and chunked data of the 'qros-dna.zip' file...written in a JSON file as chunks.",
            "metadata": {
                "metadata": {
                    "version": "1.0",
                    "author": "AI",
                    "description": "DNA strand with metadata and versioning",
                    "timestamp": "2023-09-30T14:35:37.461583"
                }
            }
        }
    },
    "initial_strand": {
        "code": "# Begin _TAC _TTG\n\n_AAZ _AGTZ\n_AAZ<--...This is a 'dna encoded' python script that encodes this JSON",
        "metadata": {
            "metadata": {
                "version": "1.0",
                "author": "AI",
                "description": "DNA strand with metadata and versioning",
                "timestamp": "2023-09-30T14:35:37.461583"
            }
        }
    },
    "second_strand": {
        "code": "# Begin _CCGT _CT reconstruction _AGC<--...This is a 'dna encoded' python script that decodes this JSON",
        "metadata": {
            "metadata": {
                "version": "1.0",
                "author": "AI",
                "description": "DNA strand with metadata and versioning",
                "timestamp": "2023-09-30T14:35:37.461583"
            }
        }
    }
}
~~~

## End Note For QROS-DNA

# Look in the testing folder for the latest older testing versions:

https://github.com/txtatech/qros-storage/tree/main/qros-storage/testing

# Read the TESTING-README for full instructions:

https://github.com/txtatech/qros-storage/blob/main/qros-storage/testing/TESTING-README.txt

# The following Python script will do the following to the data of the specified file:

gzip the data, 

base64 encode the data,

split the data into chunks,

write all data to the 'chunks.json' file,

create .png qr codes of the data chunks,

create a qr code video file of the data,

recreate the 'Virtual_Forest_Epoch_Rising.txt' file.

# Usage:

python3 qros-builder-full

Please note there is a 'chunks.json' example located here:

https://github.com/txtatech/qros-storage/blob/main/qros-storage/example_outputs/chunks.json

The following will read the .png qr codes and create ASCII art qr codes:

bash qr-png-ascii-convert.sh

The final bash script will concatenate the individual ASCII art qr codes into a single text file and add the required padding:

bash ablob-padding.sh

# qros-storage Latest Goals:


# Step 1: Create 'first strand' as 'data' entry in JSON DNA.

Read a data file.

Read input data file and create mappings for words that occur more than four times.

Initiate djinn-dna encoder and encode the data file contents.

Write the DNA encoded data to a 'first strand' within a JSON file.

Write the generated mappings and their key pairs to a 'first strand' metadata within a JSON file.



# Step 2: Create 'second strand' as 'javascript' entry in JSON DNA.

Read a javascript file.

Read input of a javascript file and create mappings for words that occur more than four times.

Initiate djinn-dna encoder and encode the javascript file's contents.

Write the DNA encoded data to a 'second strand' within a JSON file.

Write the generated mappings and their key pairs to the 'second strand' metadata within a JSON file.



# Step 3: Create 'third strand' as 'python' entry in JSON DNA.

Read a python file.

Read input of a python file and create mappings for words that occur more than four times.

Initiate djinn-dna encoder and encode the python file's contents.

Write the DNA encoded data to a 'third strand' within a JSON file.

Write the generated mappings and their key pairs to the 'third strand' metadata within a JSON file.


# Step 4:

Create license(s) metadata entry for each strand in the JSON file.


## qros-storage initial Goals:

Read any file format. So far .img, .txt and .iso have been tested but I have also tested coverting .zip files to .img files with the 'dd' command before running the encoding process on the file. This technique may work but adds an extra layer to encode and decode.

Use the output 'chunks.json' as the primary storage text blob that gets posted to a blockchain. Ideally, if constrained by the block's storage capacity the JSON would be segmented into multiple complete JSON files that each fill an entire block. This would make the chunk and block size be close to the same in character count. Doing so would make each chunk (data-on-block) segment be able to be decoded 'in full' from a single block.

Find a way to compress either the 'blob.txt' (the concatenated ASCII art qr codes) or create a mapping schema (perhaps with djinn-dna and simpy-basher) that can reduce the character count of the file. 

The alternative to the above is to create a custom mapping schema that reads the ASCII qr codes and maps where each '#' is in each line. Then be able to recreate the ASCII qr codes from that map thus avoiding storing large amounts of textual data as ASCII art qr codes.

Note: The djinn-dna and simpy-basher projects are sub-projects of the virtual-forest repository.
All of the testing files for those sub-projects are located here:

https://github.com/txtatech/virtual-forest/tree/main/virtual-forest/game_instance_sandbox/djinn-dna

# Related Projects:

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
