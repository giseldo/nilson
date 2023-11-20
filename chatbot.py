import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

df_responses = pd.read_csv("responses.csv")
df_actions = pd.read_csv("actions.csv")

def get_modelo():
	vec = CountVectorizer()
	bow_matriz = vec.fit_transform(df_actions["entrada"])
	X = bow_matriz
	y = df_actions["action"]
	reg = DecisionTreeClassifier()
	reg.fit(X, y)
	return reg, vec
	
def previsao_acao(entrada):
	reg, vec = get_modelo()
	print(entrada)
	bow_matriz_new = vec.transform([entrada])
	resutado = reg.predict(bow_matriz_new)
	return resutado

def respond(entrada):
	resultado = previsao_acao(entrada)
	df_resultado = df_responses.query("entrada == '{}'".format(resultado[0]))
	return df_resultado["resposta"].iloc[0]

#entrada = input("user: ")
#print("bot : {}".format(repond(entrada)))

