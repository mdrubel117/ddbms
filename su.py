import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.feature_selection import SelectKBest,f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import *
# 1. LOAD
data=pd.read_csv("IRIS.csv")
TARGET="species"
# 2. SHOW + SHAPE
print("FIRST 5 ROWS\n",data.head())
print("\nSHAPE:",data.shape)
# 3. MISSING
print("\nMISSING VALUES\n",data.isnull().sum())
# 4. CLEAN
data=data.drop_duplicates().dropna()
print("\nAFTER CLEANING:",data.shape)
# 5. DISTRIBUTION
print("\nCLASS DISTRIBUTION")
print(data[TARGET].value_counts())
data[TARGET].value_counts().plot(kind="bar")
plt.title("Class Distribution")
plt.show()
# 6. FEATURES + TARGET
X=data.drop(TARGET,axis=1)
y=LabelEncoder().fit_transform(data[TARGET])
X=pd.get_dummies(X,dtype=int)
# 7. SPLIT
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=42,stratify=y)
# 8. SCALING
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
# 9. FEATURE SELECTION
select=SelectKBest(f_classif,k=min(2,X_train.shape[1]))
X_train_selected=select.fit_transform(X_train,y_train)
X_test_selected=select.transform(X_test)
# 10. LOGISTIC REGRESSION
model=LogisticRegression(max_iter=1000)
model.fit(X_train_selected,y_train)
pred=model.predict(X_test_selected)
lr=accuracy_score(y_test,pred)
print("\nLOGISTIC REGRESSION")
print("Accuracy:",lr)
print(classification_report(y_test,pred))
ConfusionMatrixDisplay.from_predictions(y_test,pred)
plt.title("Logistic Regression")
plt.show()
# 11. SVM
model=SVC(kernel="linear")
model.fit(X_train_selected,y_train)
pred=model.predict(X_test_selected)
svm=accuracy_score(y_test,pred)
print("\nSVM")
print("Accuracy:",svm)
print(classification_report(y_test,pred))
ConfusionMatrixDisplay.from_predictions(y_test,pred)
plt.title("SVM")
plt.show()
# 12. RANDOM FOREST
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train_selected,y_train)
pred=model.predict(X_test_selected)
rf=accuracy_score(y_test,pred)
print("\nRANDOM FOREST")
print("Accuracy:",rf)
print(classification_report(y_test,pred))
ConfusionMatrixDisplay.from_predictions(y_test,pred)
plt.title("Random Forest")
plt.show()
# 13. KNN
model=KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_selected,y_train)
pred=model.predict(X_test_selected)
knn=accuracy_score(y_test,pred)
print("\nKNN")
print("Accuracy:",knn)
print(classification_report(y_test,pred))
ConfusionMatrixDisplay.from_predictions(y_test,pred)
plt.title("KNN")
plt.show()
# 14. NAIVE BAYES
model=GaussianNB()
model.fit(X_train_selected,y_train)
pred=model.predict(X_test_selected)
nb=accuracy_score(y_test,pred)
print("\nNAIVE BAYES")
print("Accuracy:",nb)
print(classification_report(y_test,pred))
ConfusionMatrixDisplay.from_predictions(y_test,pred)
plt.title("Naive Bayes")
plt.show()
# 15. DECISION TREE
model=DecisionTreeClassifier(random_state=42)
model.fit(X_train_selected,y_train)
pred=model.predict(X_test_selected)
dt=accuracy_score(y_test,pred)
print("\nDECISION TREE")
print("Accuracy:",dt)
print(classification_report(y_test,pred))
ConfusionMatrixDisplay.from_predictions(y_test,pred)
plt.title("Decision Tree")
plt.show()
# 16. MODEL COMPARISON
result=pd.DataFrame([["LR",lr],["SVM",svm],["RF",rf],["KNN",knn],["NB",nb],["DT",dt]],columns=["Model","Accuracy"])
print("\nMODEL COMPARISON")
print(result)
# 17. ACCURACY GRAPH
result.plot(x="Model",y="Accuracy",kind="bar",ylim=(0,1))
plt.title("Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()
# 18. BEST MODEL
best=result.loc[result["Accuracy"].idxmax()]
print("\nBEST MODEL:",best["Model"])
print("BEST ACCURACY:",best["Accuracy"])
# 19. FEATURE IMPORTANCE
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train_selected,y_train)
print("\nFEATURE IMPORTANCE")
print(model.feature_importances_)
# 20. PCA
pca=PCA(n_components=2)
X_train_pca=pca.fit_transform(X_train)
X_test_pca=pca.transform(X_test)
# 21. LR BEFORE PCA
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
pred=model.predict(X_test)
before=accuracy_score(y_test,pred)
print("\nLR BEFORE PCA")
print("Accuracy:",before)
ConfusionMatrixDisplay.from_predictions(y_test,pred)
plt.title("LR Before PCA")
plt.show()
# 22. LR AFTER PCA
model=LogisticRegression(max_iter=1000)
model.fit(X_train_pca,y_train)
pred=model.predict(X_test_pca)
after=accuracy_score(y_test,pred)
print("\nLR AFTER PCA")
print("Accuracy:",after)
ConfusionMatrixDisplay.from_predictions(y_test,pred)
plt.title("LR After PCA")
plt.show()
# 23. PCA COMPARISON
print("\nPCA COMPARISON")
print("Before PCA:",before)
print("After PCA:",after)
# 24. PCA 2D
Z=PCA(n_components=2).fit_transform(StandardScaler().fit_transform(X))
plt.scatter(Z[:,0],Z[:,1],c=y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA 2D Scatter Plot")
plt.show()