from tensorflow import keras
import re 
# Importing our translations
data_path = "span-eng.txt"
# Defining lines as a list of each line
with open(data_path, 'r', encoding='utf-8') as f:
  lines = f.read().split('\n')

# Building empty lists to hold sentences
input_docs = []
target_docs = []
# Building empty vocabulary sets
input_tokens = set()
target_tokens = set()

for line in lines:
  # Input and target sentences are separated by tabs
  input_doc, target_doc = line.split('\t')
  # Appending each sentence to input_docs
  input_docs.append(input_doc)
  # Splitting words from punctuation
  target_doc = " ".join(re.findall(r"[\w']+|[^\s\w]", target_doc))
