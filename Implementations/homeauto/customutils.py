import numpy as np

def _getStopWords():
  """
  Private method to get the stop words
  """
  with open('./preprocessing_data/stop_words.txt', 'r') as f:
    stop_words = f.readlines()
    stop_words = [word.replace('\n', '') for word in stop_words]
      
  return stop_words

def getL2Norm(word_vec):
  """
  This method returns the square root of the sum of squares of each element in the vector 
  """
  return np.sqrt(np.sum(word_vec ** 2))

def getL2NormedVector(word_vec):
  """
  This method computes and returns the Normalized version of the word vector
  """
  l2_norm = getL2Norm(word_vec)
  if l2_norm > 0:
    return word_vec * (1.0 / l2_norm)
  else:
    return word_vec

def getSentenceVector(sentence, word_vecs):
  """
  This method computes the sentence embedding for the sentence passed to this function
  """
  sentence_vector = np.zeros(100)  # because the word vectors are 100-dimentional
  for word in sentence.split():
    word_vec = word_vecs[word]
    sentence_vector = np.add(sentence_vector, getL2NormedVector(word_vec))
        
  return np.divide(sentence_vector, len(sentence.split()))