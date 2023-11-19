import streamlit as st

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

reg = DecisionTreeClassifier()
reg.fit(X, y)

st.sidebar.text("Menu")

st.write("Meu primeiro site")

comp_pet = st.text_input(label="Comprimento da pétala")
lag_pet = st.text_input(label="Largura da pétala")
comp_sep = st.text_input(label="Comprimento da sépala")
lag_sep = st.text_input(label="Largura da  sépala")

if st.button("Prever Tipo Flor"):
	resultado = reg.predict([[comp_pet, lag_pet, comp_sep, lag_sep]])
	st.write("O Tipo da flor é: {}".format(resultado))
