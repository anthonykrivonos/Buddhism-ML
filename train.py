# Anthony Krivonos
# Buddhism-ML
# train.py
# March 18th, 2019

import os
from textgenrnn import textgenrnn

textgen = textgenrnn()

# Loop through files, training with the files content
# directory = 'train/'
# allText = ""
# for filename in os.listdir(directory):
#     if filename.endswith(".txt"): 
#         f = open(os.path.join(directory, filename), 'r')

#         # Do training here
#         text = f.read()


#         allText += text

#         f.close()
#         continue
#     else:
#         continue

# f = open('training.txt', 'w') 
# f.write(allText)
# f.close() 

textgen.train_from_file('training.txt', temperature=[0.2, 0.2, 1.0, 1.0], new_model = True, batch_size = 30, num_epochs = 10, gen_epochs = 5)
textgen.generate()