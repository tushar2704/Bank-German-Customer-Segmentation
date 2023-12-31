import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
import catboost
from catboost import CatBoostClassifier
import os

print("catboost version:", catboost.__version__)
print("Importing Data")
df = pd.read_csv('src\data\german_creditrisk_data.csv')

print("Processing Data")
df.fillna('NaN', inplace=True)
x = df.iloc[:, :-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
print(X_train.head())

print("Train Model")
model = CatBoostClassifier(iterations=2,
                           learning_rate=1,
                           depth=2)

model.fit(X_train, y_train, cat_features=['Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Purpose'] )



new_file_path = './src/model/ml_model.pkl'


os.makedirs(os.path.dirname(new_file_path), exist_ok=True)


print("Creating Pickle File")
pickle.dump(model, open(new_file_path, 'wb'))