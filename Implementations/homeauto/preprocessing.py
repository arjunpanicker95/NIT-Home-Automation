from .customutils import _getStopWords

def to_lower(stringList):
  """
  Converts the passed list of strings into lower case
  """
  strings = [item.lower() for item in stringList]

  return strings


def remove_stop_words(string, stopWords):
  """
  Removes the stop words from the string passed to the function
  """
  new_string = ''
  stop_words = stopWords if len(stopWords) else _getStopWords()
  for word in string.split():
    if word not in stop_words:
      new_string += word + ' '

  return new_string.strip()

def replace_word_vec(ft_model, main_dict, word_list = [], root_word = ''):
  """
  Replace the word vectors for the words found in the dictionary
  with the word vector of the root word.
  """
  for word in word_list:
    main_dict[word] = ft_model.get_word_vector(root_word)

  return main_dict
