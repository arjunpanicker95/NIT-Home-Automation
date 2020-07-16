import fasttext
import pandas as pd
import numpy as np

class Pipeline():
  '''
  Creates a list of methods that must be executed in order as provided
  and executes them.
  '''

  def __init__(self, funcs = [], args = []):
    self.funcs = funcs
    self.args = args


if __name__ == "__main__":
    knnPipeline = Pipeline()