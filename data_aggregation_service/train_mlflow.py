import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression

X, y = [[1], [2], [3]], [0, 1, 0]

with mlflow.start_run():
    model = LogisticRegression()
    model.fit(X, y)

    acc = model.score(X, y)

    mlflow.log_param("model", "logistic")
    mlflow.log_metric("accuracy", acc)

    mlflow.sklearn.log_model(model, "model")

