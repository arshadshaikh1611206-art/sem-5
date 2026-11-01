from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = GaussianNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, predictions))

probabilities = model.predict_proba(X_test[:1])
print("class probabilities ", probabilities)
