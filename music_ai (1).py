# -*- coding: utf-8 -*-
"""Music AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eAZKr4tmmWanm1Cj3y_5drHdxMLQersJ
"""

import pandas as pd
data=pd.read_csv('music.csv')
data

"""Removing duplicate

"""

data.isnull()

"""Splitting"""

x=data.drop(columns=['genre'])
x

y=data['genre']
y

from sklearn.tree import DecisionTreeClassifier

"""Model"""

model=DecisionTreeClassifier()
model.fit(x,y)
data

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x_train, x_test, y_train,y_test =train_test_split(x,y,test_size=0.2)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
predictions
score=accuracy_score(y_test,predictions)
score

prediction=model.predict([[21,1],[22,0]])
prediction

"""# New Section"""