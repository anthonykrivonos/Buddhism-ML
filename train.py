# Anthony Krivonos
# Buddhism-ML
# train.py
# March 18th, 2019

import os
from prepare import CONSTANTS
from textgenrnn import textgenrnn

# Instantiate LSTM neural net
textgen = textgenrnn()

# Create list of training file contents
fileContents = []
for filename in os.listdir(CONSTANTS['TRAIN_DIRECTORY']):
    fileWithDirectory = os.path.join(CONSTANTS['TRAIN_DIRECTORY'], filename)
    with open(fileWithDirectory, 'r', encoding = 'utf-8', errors = 'ignore') as f:
        fileContents.append(f.read())

# Train neural net
textgen.train_on_texts(fileContents, interactive=True, top_n=5, temperature=[0.2, 0.2, 1.0, 1.0], batch_size = 4096, num_epochs = 50, gen_epochs = 10, multi_gpu = False)

# Generate output in the console
textgen.generate()