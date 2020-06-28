import pandas as pd, numpy as np
import pickle 

# ////////////////////// Loading the datasets ( here it is the Diabetes datesets ) //////////////////////////////
data = pd.read_csv('datasets_23663_30246_diabetes.csv')
data.head()

# //////////////////// Training the dataset ////////////////////////
from sklearn.model_selection import  train_test_split

x = data.drop('Outcome',axis=1)
y = data['Outcome']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=101)

# /////////////////////// Model creation //////////////////
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)

# ///////////////////// Predicting the values ////////////////////////
pred = knn.predict(x_test)



pickle.dump(knn,open('model.pkl','wb'))