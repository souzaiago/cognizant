# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:44:03 2019

@author: 748295
"""

from sklearn import tree

x = [[181, 80, 44], [177,70,43], [160, 60, 38], [192, 90, 36]]
y = ['male', 'female', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[180, 80, 38]])

print (prediction)