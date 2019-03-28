# Anthony Krivonos
# Buddhism-ML
# prepare.py
# March 18th, 2019

import os
import re

# Abstract: Prepares the list of training files into consumable texts for the model.

CONSTANTS = {
    # Name of the directory with training files
    'TRAIN_DIRECTORY': 'train/'
}

# Loop through files, training with the files content
for filename in os.listdir(CONSTANTS['TRAIN_DIRECTORY']):
    # Read the current file's contents
    fileWithDirectory = os.path.join(CONSTANTS['TRAIN_DIRECTORY'], filename)
    f = open(fileWithDirectory, 'r', encoding = 'utf-8', errors = 'ignore')

    # Store file contents into text
    text = f.read()

    # Remove non-UTF-8 characters
    text = text.encode("ascii", errors="ignore").decode()

    # Remove empty lines and tabs
    text = ''.join([s for s in text.splitlines(True) if s.strip("\r\n\t")]).replace('\n', ' ')

    # Remove multiple spaces
    text = re.sub("\s\s+", " ", text)

    # Write sanitized text to output file
    with open(fileWithDirectory, 'w', encoding='utf-8') as f:
        print(text, file=f)
    
    f.close()