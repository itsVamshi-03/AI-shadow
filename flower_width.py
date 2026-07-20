
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay

iris = load_iris()

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df['Target'] = y

print(df.head())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy :", accuracy)

print("\nClassification Report")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.show()

importance = model.feature_importances_

plt.figure(figsize=(8,5))
plt.bar(iris.feature_names, importance)
plt.xticks(rotation=20)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.show()

plt.figure(figsize=(5,5))
plt.bar(["Random Forest"], [accuracy], color="green")
plt.ylim(0,1)
plt.ylabel("Accuracy")
plt.title("Model Accuracy")
plt.show()

plt.figure(figsize=(8,4))
plt.plot(y_test, 'bo-', label="Actual")
plt.plot(y_pred, 'r*-', label="Predicted")
plt.legend()
plt.title("Actual vs Predicted")
plt.xlabel("Sample")
plt.ylabel("Class")
plt.show()

probs = model.predict_proba(X_test)

plt.figure(figsize=(8,5))
plt.plot(np.max(probs, axis=1), marker='o')
plt.title("Prediction Confidence")
plt.xlabel("Test Sample")
plt.ylabel("Confidence")
plt.grid(True)
plt.show()

print("\nFeature Importance")
for name, score in zip(iris.feature_names, importance):
    print(f"{name}: {score:.4f}")