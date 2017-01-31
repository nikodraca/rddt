from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
from keras.models import load_model
import numpy as np
import random
import sys
import json
import requests

def get_lyrics():
	model = load_model('my_model.h5')
	path = "txt/output_all.txt"
	text = open(path).read().lower()

	maxlen = 40
	chars = sorted(list(set(text)))
	char_indices = dict((c, i) for i, c in enumerate(chars))
	indices_char = dict((i, c) for i, c in enumerate(chars))

	def sample(preds, temperature=1.0):
			# helper function to sample an index from a probability array
			preds = np.asarray(preds).astype('float64')
			preds = np.log(preds) / temperature
			exp_preds = np.exp(preds)
			preds = exp_preds / np.sum(exp_preds)
			probas = np.random.multinomial(1, preds, 1)
			return np.argmax(probas)

	# train the model, output generated text after each iteration

	start_index = random.randint(0, len(text) - maxlen - 1)

	diversity = 0.15
	print()
	print('----- diversity:', diversity)

	generated = ''
	sentence = text[start_index: start_index + maxlen]
	generated += sentence
	print('----- Generating with seed: "' + sentence + '"')
	sys.stdout.write(generated)

	for i in range(400):
			x = np.zeros((1, maxlen, len(chars)))
			for t, char in enumerate(sentence):
					x[0, t, char_indices[char]] = 1.

			preds = model.predict(x, verbose=0)[0]
			next_index = sample(preds, diversity)
			next_char = indices_char[next_index]

			generated += next_char
			sentence = sentence[1:] + next_char 

	print()	

	return json.dumps(generated.split("\n"))
