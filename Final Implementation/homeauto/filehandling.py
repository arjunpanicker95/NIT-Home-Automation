import _pickle as pickle

def saveToFile(wordVecDict):
  """
  Save the word vectors to a binary file
  """
  with open('./Utilities/Result Vectors/word_vectors.bin', 'wb') as f:
    f.write(pickle.dumps(wordVecDict))

def readFromFile():
  """
  Read the word embeddings from the binary file.
  """
  with open('./Utilities/Result Vectors/word_vectors.bin', 'rb') as f:
    word_vecs = pickle.load(f)
    word_vecs = word_vecs['wordVecDict']