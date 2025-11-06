# MachineLearningProjectWithMLFlow
create template.py - define project structure 
Terminal - python3 template.py

requirements.txt and setup.py
Terminal - python -m pip install -r requirements.txt

build code in commom.py
trials.ipynb (verify imports from common.py)


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py





# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/PUNAMRAMPUKALE/MachineLearningProjectWithMLFlow
```
### STEP 01- Create a virtual environment and activate it after opening the repository 


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python main.py
```

Now,
```bash
open up you local host and port
```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui


### dagshub URI
[dagshub](https://dagshub.com/)


import dagshub
dagshub.init(repo_owner='PUNAMRAMPUKALE', repo_name='MachineLearningProjectWithMLFlow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

Run this to export as env variables:

```bash



