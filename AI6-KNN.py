from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.21, random_state=44
)

scalar = StandardScaler()
X_train, X_test = scalar.fit_transform(X_train), scalar.transform(X_test)
k=4
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred) * 100
report = classification_report(y_test, y_pred, target_names=data.target_names)
metrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}%")
print(f"Report \n {report}")
print(f"metrix \n {metrix}")
