from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

scores = []

for i in range(1, 100):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
	reg = DecisionTreeClassifier()
	reg.fit(X_train, y_train)
	scores.append(reg.score(X_test, y_test))

print(np.mean(scores))



