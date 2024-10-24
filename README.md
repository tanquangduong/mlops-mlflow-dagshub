# Mini MLOps project with MLFlow and Dagshub
* Hyperparameter tuning for Logistic Regression for prediction of wine production use case
* Tracking ML experiments with MLFLow
* Loading MLFLow tracking to Dagshub server
* Register model
* Serving model as REST API

# Serving registed model from MLFLow model registry in Dagshub server
* Build a Docker containter from register model
```
!mlflow models build-docker --name lr_model_2 --model-uri "models:/best_lr/1"
```
