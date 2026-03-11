import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

X = [[10],[20],[30],[40],[50],[75],[41]]
y = [15,25,35,45,55,11,13]

model = RandomForestRegressor()
model.fit(X,y)

X_marks = [[70]]
print(model.predict(X_marks))