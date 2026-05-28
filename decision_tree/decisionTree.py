import pandas
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("data.csv")

d = {'arab': 0, 'jhud': 1}
df['Nationality'] = df['Nationality'].map(d)

def simple_name_to_numbers(names):
    hebrew_chars = 'אבגדהוזחטיכלמנסעפצקרשת'
    features = []
    
    for name in names:
        # Count each Hebrew character
        counts = [name.count(char) for char in hebrew_chars]
        # Add name length
        counts.append(len(name))
        # Add number of words
        counts.append(len(name.split()))
        features.append(counts)
    
    return np.array(features)

X = simple_name_to_numbers(df['Name'])
y = df['Nationality']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

hebrew_chars = 'אבגדהוזחטיכלמנסעפצקרשת'
feature_names = [f'char_{char}' for char in hebrew_chars] + ['name_length', 'num_words']
plt.figure(figsize=(20, 10))
tree.plot_tree(dtree, feature_names=feature_names)
plt.show()

name =input("enter a name to check  ")
while name != "exit":
    test_features = simple_name_to_numbers([name])
    print("arab" if dtree.predict(test_features) == [0] else "jewish" )
    name =input("enter a name to check")
