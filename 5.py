#!/usr/bin/env python3

import pickle 


with open('banner.p', 'rb') as f:
    data = pickle.load(f)
    print(data)
    
for item in data:
    print("".join(i[0] * i[1] for i in item))
