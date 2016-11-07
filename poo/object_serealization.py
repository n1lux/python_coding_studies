"""
Object Serealization with pickle
Data converter as byte sequence to store in file.
"""

import pickle
data = ['Nilo', 'Alexandre', 32, [1, 2, 3]]

with open('data.txt', 'wb') as fp:
    pickle.dump(data, fp)


with open('data.txt', 'rb') as fp:
    load_data = pickle.load(fp)

print(load_data)


assert load_data == data
