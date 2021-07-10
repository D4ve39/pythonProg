import pandas
import numpy as np
from sklearn.linear_model import LinearRegression

df = pandas.DataFrame({'x': np.array([0, 1, 2, 3, 4]),
                       'f(x)': np.array([1, 0.5, 0.33, 0.25, 0.2])})

# from a numpy array
X = np.array([[0.0, 1.0], [1.0, 0.5], [2.0, 0.33], [3.0,0.25], [4.0, 0.2]])
df = pandas.DataFrame(X, columns=['x', 'f(x)'])

df['f(x)']
