import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=["Maths", "Science", "English", "Computer"]
)

df["Grade"] = iris.target

print(df.head())

X = df[["Maths","Science","English","Computer"]]
y = df["Grade"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(probability=True)
}

results = []

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)
    pre = precision_score(y_test, pred, average="weighted")
    rec = recall_score(y_test, pred, average="weighted")
    f1 = f1_score(y_test, pred, average="weighted")

    results.append([name, acc, pre, rec, f1])

results_df = pd.DataFrame(
    results,
    columns=["Model","Accuracy","Precision","Recall","F1 Score"]
)

print("\nPerformance Comparison")
print(results_df)

results_df.set_index("Model").plot(kind="bar", figsize=(10,6))
plt.title("All Metrics Comparison")
plt.ylabel("Score")
plt.ylim(0,1.1)
plt.grid(axis="y")
plt.show()

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

cm = confusion_matrix(y_test, rf_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["A","B","C"]
)

disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

prob = rf.predict_proba(X_test)

confidence = np.max(prob, axis=1)

plt.figure(figsize=(8,5))
plt.plot(confidence, marker='o')
plt.title("Confidence Score")
plt.xlabel("Student")
plt.ylabel("Confidence")
plt.grid(True)
plt.show()

importance = rf.feature_importances_

features = ["Maths","Science","English","Computer"]

plt.figure(figsize=(7,5))
plt.bar(features, importance)
plt.title("Feature Importance")
plt.ylabel("Importance Score")
plt.show()

print("\nFeature Importance")
for f, i in zip(features, importance):
    print(f"{f} : {i:.4f}")