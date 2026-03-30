import numpy as np
import pandas as p
import faker as f
import matplotlib as m

fakeinator = f.Faker()
data = []

for i in range(100): data.append(fakeinator.name())

print(data)