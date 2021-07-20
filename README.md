#  Common Evaluation metrics graph plot for Regression 

## Description
Python implementations for comparing different Regression Models and Plotting with their most common evaluation metrics.

The purpose of this package is to help users plot the graph at ease with different widely used metrics for regression model evaluation for comparing them at a glance 

<p align="center">
    <img src="https://github.com/ajayarunachalam/RegressorMetricGraphPlot/blob/main/regressormetricgraphplot/example_plot.png" width="640"\>
</p>
<p align="center">
    Figure: Model evaluation plot with widely used metrics 
</p>

## Illustration Example

```python
# Importing libraries 
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from regressormetricgraphplot import *
%matplotlib inline
```

```python
#Let's load a simple dataset and make a train & test set :
X, y = make_regression(n_samples=1000, n_features=10, n_informative=7, n_targets=1, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
```

```python
# Train the regressor and predict on test set 
# Fitting training set to linear regression model
lr = LinearRegression(n_jobs=-1)
lr.fit(X_train, y_train)
# Predicting
y_pred = lr.predict(X_test)
```

We can now use ``R2AndRMSE`` to compute & output R-squared, and Root Mean Square Error.

```python
# Metrics
CompareModels.R2AndRMSE(y_test=y_test, y_pred=y_pred)
```

Make object of the class ``CompareModels``

```python
plot = CompareModels()
```

We can now use ``add`` &  ``show`` method to add the built model & plot the graph at ease with all the evaluated metrics.

```python
plot.add(model_name='Linear Regression', y_test=y_test, y_pred=y_pred)
plot.show(figsize=(10, 5))
```

<p align="center">
    <img src="https://github.com/ajayarunachalam/RegressorMetricGraphPlot/blob/main/regressormetricgraphplot/LR_Metric_PLOT.png" width="640"\>
</p>

## Table of Contents
- [Compare Regression Model Metrics Plot](#regressormetricgraphplot)
  * [Installation](#installation)
  * [Examples](#examples)
    + [Demo](#Usage))
  * [Contact](#contact)

## Installation 
    $ pip install regressormetricgraphplot

         OR

    $ git clone https://github.com/ajayarunachalam/RegressorMetricGraphPlot
    $ cd RegressorMetricGraphPlot
    $ python setup.py install

## Notebook
    !pip install regressormetricgraphplot & import as 'from regressormetricgraphplot import *'

         OR

    !git clone https://github.com/ajayarunachalam/RegressorMetricGraphPlot.git
    cd RegressorMetricGraphPlot/

    Just replace the line 'from CompareModels import *' with 'from regressormetricgraphplot import CompareModels' 
Follow the rest as demonstrated in the demo example [here] -- (https://github.com/ajayarunachalam/RegressorMetricGraphPlot/blob/main/regressormetricgraphplot/demo.ipynb) 

## Installation with Anaconda

If you installed your Python with Anacoda you can run the following commands to get started:
```bash

# Clone the repository 
git clone https://github.com/ajayarunachalam/RegressorMetricGraphPlot.git
cd RegressorMetricGraphPlot
# Create new conda environment with Python 3.6
conda create --new your-env-name python=3.6
# Activate the environment
conda activate your-env-name
# Install conda dependencies
conda install --yes --file conda_requirements.txt
# Instal pip dependencies
pip install requirements.txt
```



## Examples
Navigate to the demo example in a form of iPython notebooks: -- [here](https://github.com/ajayarunachalam/RegressorMetricGraphPlot/blob/main/regressormetricgraphplot/demo.ipynb)


### Demo
     * demo.ipynb 

## Contact
If there's some implementation you would like to see here or add in some examples feel free to do so. You can reach me at [email](mailto:ajay.arunachalam08@gmail.com)
