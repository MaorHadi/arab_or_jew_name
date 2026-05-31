# Arab or Jew — Machine Learning

## Setup & Usage

```bash
chmod +x setup.sh
./setup.sh
```

Then run your preferred model:

```bash
py decision_tree/decisionTree.py
# or
py logistic_regression/logisticRegression.py
```

> **Recommendation:** The logistic regression method is preferred — it can break down which parts of a name have stronger Arabic or Jewish connections.

## Dataset Examples

**`names.csv`**
```
Name,Nationality,Position
איהאב,arab,0
אבו לבדה,arab,1
מאור,jewish,0
חדי,jewish,1
...
```

**`data.csv`**
```
Name,Nationality
איהאב אבו לבדה,arab
מאור חדי,jewish
...
```