import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

df_responses = pd.read_csv("responses.csv")
df_actions = pd.read_csv("actions.csv")

vec = CountVectorizer()
bow_matriz = vec.fit_transform(df_actions["entrada"])
X = bow_matriz
y = df_actions["action"]

reg = DecisionTreeClassifier()
reg.fit(X, y)

	
