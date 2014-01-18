#takes the prediction program, outputs a sentiment
from text.classifiers import NaiveBayesClassifier
from text.blob import TextBlob
import pickle

#Returns: BULLY STATEMENT: TRUE, NOT A BULLY STATMENT: FALSE
class BullySentiment:
	def get_sentiment(self,input_string):
		cl_predict = pickle.load(open("output.p","rb"))
		return cl_predict.classify(input_string)

'''import unittest

class TestSequenceFunctions(unittest.TestCase):

	def test_1(self):
		self.bully = BullySentiment()
		self.assertEqual(self.bully.get_sentiment("fuck you"), "True")


if __name__ == '__main__':
    unittest.main()'''