!pip install scikit-learn==1.5.2
!pip install joblib==1.3.2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import KFold,cross_val_score
myfold = KFold(n_splits=5)
import joblib
data = pd.read_csv("/content/crops.csv")
print(data)
sns.heatmap(data.isnull())
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0,shuffle=True)
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100)
rf.fit(x_train,y_train)
from sklearn.metrics import accuracy_score,confusion_matrix
y_pred = rf.predict(x_test)
print(accuracy_score(y_test,y_pred))
cm = confusion_matrix(y_test,y_pred)
print(cm)
inp=[[98,  43,  43,    20.879744,  10.002744,  20.502985,  202.935536]]
yp=rf.predict(inp)
print(yp)
mysc = cross_val_score(rf,x_test,y_test,cv=myfold)
print(mysc)
print("kfold of knn:"+str(mysc.mean()))
joblib.dump(rf,"model.joblib")
