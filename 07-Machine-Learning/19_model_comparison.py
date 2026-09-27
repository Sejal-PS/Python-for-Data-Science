# Model Comparison

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier


# ------------------------------------------
# Dataset
# ------------------------------------------

iris = load_iris()

X = iris.data

y = iris.target


# ------------------------------------------
# Train-Test Split
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ------------------------------------------
# Models
# ------------------------------------------

models = {
    "Logistic Regression":
        LogisticRegression(max_iter=200),

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            random_state=42
        ),

    "KNN":
        KNeighborsClassifier()
}


# ------------------------------------------
# Train and Compare
# ------------------------------------------

for name, model in models.items():

    model.fit(
        X_train,
        y_train
    )

    y_pred = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    print(
        name,
        ":",
        accuracy
    )


# ------------------------------------------
# Important
# ------------------------------------------

# Model comparison should consider:
#
# - Appropriate evaluation metrics
# - Dataset characteristics
# - Computational cost
# - Interpretability
# - Generalization
#
# Do not select a model based only
# on one metric from one split.
