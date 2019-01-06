# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:44:03 2019

@author: 748295
"""

import numpy as np
from lightfm.databases import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['tests\']))

model = LightFM(loss='warp')

model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
    
    n_user, n_items = data['train'].shape
    
    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[user_ide].indices]
        
        score = model.predict(user_id, np.arrange(n_items))
        
        top_items = data['item_labels'][np.argsort(-scores)]
        
        print("User %s" % user_id)
        print("     Known positives:")
        
        for x in known_positives[:3]:
            print("             %s" % x)
            
        print("             Recommended:")
        
        for x in top_items[3]:
            print("             %s" % x)
            
sample_recommendation(model, data, [3,25,450])