# qros-storage
This is a convergent repository for various qr code data storage projects with the goal of creating a single data storage solution that encapsulates all the data (and any code) inside a single JSON  file and single qr code video.

The current version encapsulates the following file types within a single 'qr code video' and JSON file: python scripts, an html file, a text file, bash scripts, a javascript file and a zip file.

## Use 'qros-dna-main' for the latest refactored stable testing version:

https://github.com/txtatech/qros-storage/tree/main/qros-storage/qros-dna-main

## Use 'qros-dna' for the latest stable version:

https://github.com/txtatech/qros-storage/tree/main/qros-storage/qros-dna

## Use 'qros-dna-live' for encoding and decoding without qr codes or qr code videos:

https://github.com/txtatech/qros-storage/tree/main/qros-storage/qros-dna-live

## Use 'qros-builder' for standalone file encoding:

https://github.com/txtatech/qros-storage/tree/main/qros-storage/qros-builder

## Use 'qros-builder-lite' for standalone file encoding and decoding without qr codes or qr code video files:

https://github.com/txtatech/qros-storage/tree/main/qros-storage/qros-builder-lite

## NOTE ON QROS-DNA:

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

Generates DNA-like code representations for characters and character combinations ranging from one to five characters long. These generated mappings are used to encode text data.

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

# Example of 'QROS-DNA Encoded' JSON:
~~~
{
    "dna_structure": {
        "Genomes": {
            "Chromosomes": {
                "Genes": {
                    "Nucleotide Sequences": {
                        "code": "The `qros-_CATZ-encoder.py` _C _G _T<--...This is 'dna' encoded from a text file that creates the mappings."
                    }
                }
            }
        },
        "introns": {
            "mappings": "{'the': '_T', 'qrosdnaencoderpy': '_A',,<--...This is where the mappings are stored."
        },
        "exons": {
            "0shell": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<--...This is the 'live component' javascript shell.",
            "0js": "// Simulated JSON containing \"live components\"\n<--...This is the 'live component' javascript backend.",
            "0html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Dynamic<--...This is the 'live component' html frontend.",
            "metadata": {
                "metadata": {
                    "version": "1.0",
                    "author": "AI",
                    "description": "DNA strand with metadata and versioning",
                    "timestamp": "2023-10-02T03:19:08.683209"
                }
            }
        },
        "files": {
            "code": "{\"chunks\": [\"H4sIAOtuGmUC_wvwZmbhYmYAgq-STuFK<--...This is a zip file stored as chunks.",
            "metadata": {
                "metadata": {
                    "version": "1.0",
                    "author": "AI",
                    "description": "DNA strand with metadata and versioning",
                    "timestamp": "2023-10-02T03:19:08.683209"
                }
            }
        },
        "profusion": {
            "code": "<html>\n<head>\n      <style>\n<--...This is the html file for the stable-profusion frontend.",
            "metadata": {
                "metadata": {
                    "version": "1.0",
                    "author": "AI",
                    "description": "DNA strand with metadata and versioning",
                    "timestamp": "2023-10-02T03:19:08.683209"
                }
            }
        },
        "emu": {
            "loader": "<!doctype html>\n<title>Asynchronous loading of disk images<--...This is the html loader file for V86 OS emulation.",
            "libv86": "PLACEHOLDER FOR TESTING SPEED ONLY<--...This is the libV86.js file for OS emulation.",
            "v86wasm": "{\"chunks\": [\"H4sIAOtuGmUC_wvwcXR29fD3c<--...This is the V86.wasm file for OS emulation stored as chunks.",
            "metadata": {
                "metadata": {
                    "version": "1.0",
                    "author": "AI",
                    "description": "DNA strand with metadata and versioning",
                    "timestamp": "2023-10-02T03:19:08.683209"
                }
            }
        }
    },
    "initial_strand": {
        "code": "#!/bin/bash\n\n_AZ=('T' 'A' 'C' 'G' 'Z')\n<--...This is a bash file for a list of possible combinations.",
        "metadata": {
            "metadata": {
                "version": "1.0",
                "author": "AI",
                "description": "DNA strand with metadata and versioning",
                "timestamp": "2023-10-02T03:19:08.683209"
            }
        }
    },
    "second_strand": {
        "code": "#!/bin/bash\n\n# Set _T maximum _ACTC _GGT _AZ<--...This is a bash file for splitting large text files.",
        "metadata": {
            "metadata": {
                "version": "1.0",
                "author": "AI",
                "description": "DNA strand with metadata and versioning",
                "timestamp": "2023-10-02T03:19:08.683209"
            }
        }
    },
    "third_strand": {
        "js-shell": "<!DOCTYPE html>\n<html lang=\"en\">\n<--...This is another javascript shell html file for backend use.",
        "encoded-encoder": "# Begin _TTG _ZTA WASM _TAC _GA<--...This is a dna encoded version of the 'qros-dna-encoder.py' file used to encode and create this JSON.",
        "encoded-decoder": "# Begin _TTCZ _CT _GTCZ _GGT<--...This is a dna encoded version of the 'qros-dna-decoder.py' file used to decode this JSON.",
        "decoder": "# Begin decoding and reconstruction<--...This is a plain text version of the 'qros-dna-decoder.py' file used to decode this JSON.",
        "metadata": {
            "metadata": {
                "version": "1.0",
                "author": "AI",
                "description": "DNA strand with metadata and versioning",
                "timestamp": "2023-10-02T03:19:08.683209"
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

### CURRENT GOALS NUANCES

### web.js - The Logic Layer
1. **Dynamic Data Loading**: Given its asynchronous nature, `web.js` could fetch other parts of the JSON dynamically, updating the UI without a full page reload.
2. **Event Handling**: It could listen for user interactions on the `index.html` elements and execute corresponding functions. For instance, toggling dark mode could change the JSON's state to reflect this user preference.
3. **JS Shell Interactions**: Functions within `web.js` might be invokable from the JS shell, offering a programmatic way to control the interface.

### index.html - The Structure
1. **DOM Elements**: These could be placeholders for data loaded dynamically via `web.js`. For example, a `<div>` could be designated to display decoded text from the JSON.
2. **User Inputs**: Form elements in `index.html` could capture user inputs that influence the JSON's state, like selecting which DNA strand to decode.
  
### JS Shell - The Interactive Terminal
1. **Real-time Execution**: This could offer a more hands-on way to interact with the JSON. For instance, executing a command could trigger a decode operation in `web.js`.
2. **Debugging**: The shell could serve as a real-time debugger, allowing you to check the state of variables or even modify the JSON directly.

### JSON as the Central Hub
1. **State Management**: The JSON could maintain a "live" state of the entire interface, including user preferences, currently displayed data, and even runtime variables.
2. **Dynamic Code Loading**: Beyond data, the JSON could contain the most current versions of `web.js`, `index.html`, and the JS shell. This would allow for seamless updates without requiring a manual refresh.
3. **Modularity**: Each "live component" could be a modular, replaceable part of the system. For example, an entirely new JavaScript logic layer could be swapped in without changing the HTML or shell components.

### Potential Interactions
1. **Initialization**: On loading the web interface, `web.js` fetches `index.html` and the JS Shell from the JSON and initializes them.
2. **User Interaction**: A user selects an option in `index.html`. `web.js` captures this event, updates the JSON's state, and potentially triggers a change in the JS shell.
3. **JS Shell Commands**: A command entered into the JS shell updates the JSON and triggers a corresponding update in `web.js` and `index.html`.

By incorporating these components as "live" elements within a JSON file, you'd essentially have a self-contained, dynamically updatable, and highly modular system. This concept has the potential for high portability, ease of updates, and even real-time collaborative features. 

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
