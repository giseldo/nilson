import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np
import spacy
from spacy.lang.en import STOP_WORDS

df = pd.read_csv("fakenews.csv")

# remover as stopwords
nlp = spacy.load('en_core_web_sm')
def remover_stop_word(text):
	doc = nlp(text)
	tokens = [token.text for token in doc if token.text not in STOP_WORDS and token.text.isalpha()]
	return ' '.join(tokens)

# lemmatization
df["title"] = df["title"].apply(remover_stop_word)

X = df["title"]
vectorizer = TfidfVectorizer()
bow_matiz = vectorizer.fit_transform(X)

print(bow_matiz.shape)

X = bow_matiz
y = df["label"]

scores = []
for i in range(1, 100):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
	reg = DecisionTreeClassifier()
	reg.fit(X_train, y_train)
	scores.append(reg.score(X_test, y_test))

print(" Acurácia média: {}".format(np.mean(scores)))


