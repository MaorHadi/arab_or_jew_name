import pandas
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pandas.read_csv("names.csv")

d = {'arab': 0, 'jewish': 1}
df['Nationality'] = df['Nationality'].map(d)

first_name = df[df['Position'] == 0]
last_names = df[df['Position'] == 1]

def simple_name_to_numbers(names):
    hebrew_chars = 'אבגדהוזחטיכלמנסעפצקרשת'
    features = []
    
    for name in names:
        # Count each Hebrew character
        counts = [name.count(char) for char in hebrew_chars]
        # Add name length
        counts.append(len(name))
        features.append(counts)
    
    return np.array(features)

def result(name):
    words = name.split()
    
    if len(words) == 1:
        word = words[0].replace(" ", "")
        test_features = simple_name_to_numbers([word])
        print("onlyword log predicts:",logr_first.predict_log_proba(test_features))
        return 0 if logr_first.predict(test_features) == [0] else 1
    
    elif len(words) > 1:
        first_word = words[0].replace(" ", "")
        remaining_words = " ".join(words[1:]).replace(" ", "")
        
        first_features = simple_name_to_numbers([first_word])
        print("firstwords log predicts:",logr_first.predict_proba(first_features))
        first_prediction = logr_first.predict(first_features)[0]
        
        last_features = simple_name_to_numbers([remaining_words])
        print("lastwords log predicts:",logr_first.predict_proba(last_features))
        last_prediction = logr_last.predict(last_features)[0]
        
        print(f"First word '{first_word}' prediction: {first_prediction}")
        print(f"Remaining words '{remaining_words}' prediction: {last_prediction}")
        
        if first_prediction == 0 and last_prediction == 0:
            return 0 
        elif first_prediction == 1 and last_prediction == 1:
            return 1 
        else:  
            return 2  

X_firstName = simple_name_to_numbers(first_name['Name'])
y_firstName = first_name['Nationality']

logr_first = linear_model.LogisticRegression(max_iter=10000,C=2,class_weight='balanced')

X_train_first, X_test_first, y_train_first, y_test_first = train_test_split(X_firstName, y_firstName, test_size=0.2,train_size=0.8, shuffle=True,stratify=y_firstName)

logr_first = logr_first.fit(X_train_first, y_train_first)




X_lastNames = simple_name_to_numbers(last_names['Name'])
y_lastNames = last_names['Nationality']

logr_last = linear_model.LogisticRegression(max_iter=10000,C=2,class_weight='balanced')

X_train_last, X_test_last, y_train_last, y_test_last = train_test_split(X_lastNames, y_lastNames, test_size=0.2,train_size=0.8, shuffle=True,stratify=y_lastNames)

logr_last = logr_last.fit(X_train_last, y_train_last)


print("first name logistical regression score: " + str(logr_first.score(X_test_first, y_test_first)))

print("last names logistical regression score: " + str(logr_last.score(X_test_last, y_test_last)))

name =input("enter a name to check  ")
while name != "exit":
    prediction = result(name)
    if prediction == 0:
        print("arab")
    elif prediction == 1:
        print("jewish")
    else:
        print("ambigious")
    name =input("enter a name to check")
