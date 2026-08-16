import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.cluster import KMeans,DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from sklearn.metrics import *
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster
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
# 7. SCALING
X=StandardScaler().fit_transform(X)
# 8. PCA
Z=PCA(n_components=2).fit_transform(X)
# 9. K-MEANS
model=KMeans(n_clusters=3,n_init=10,random_state=42)
model.fit(X)
pred=model.predict(X)
km=silhouette_score(X,pred)
print("\nK-MEANS")
print("Silhouette:",km)
print("ARI:",adjusted_rand_score(y,pred))
print("NMI:",normalized_mutual_info_score(y,pred))
plt.scatter(Z[:,0],Z[:,1],c=pred)
plt.title("K-Means")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
# 10. GMM
model=GaussianMixture(n_components=3,random_state=42)
model.fit(X)
pred=model.predict(X)
gmm=silhouette_score(X,pred)
print("\nGMM")
print("Silhouette:",gmm)
print("ARI:",adjusted_rand_score(y,pred))
print("NMI:",normalized_mutual_info_score(y,pred))
plt.scatter(Z[:,0],Z[:,1],c=pred)
plt.title("GMM")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
# 11. HIERARCHICAL
model=linkage(X,method="ward")
pred=fcluster(model,3,criterion="maxclust")-1
hier=silhouette_score(X,pred)
print("\nHIERARCHICAL")
print("Silhouette:",hier)
print("ARI:",adjusted_rand_score(y,pred))
print("NMI:",normalized_mutual_info_score(y,pred))
plt.scatter(Z[:,0],Z[:,1],c=pred)
plt.title("Hierarchical")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
dendrogram(model)
plt.title("Hierarchical Dendrogram")
plt.show()
# 12. DBSCAN
model=DBSCAN(eps=.5,min_samples=5)
model.fit(X)
pred=model.labels_
db=silhouette_score(X,pred) if len(set(pred))>1 else 0
print("\nDBSCAN")
print("Silhouette:",db)
print("ARI:",adjusted_rand_score(y,pred))
print("NMI:",normalized_mutual_info_score(y,pred))
plt.scatter(Z[:,0],Z[:,1],c=pred)
plt.title("DBSCAN")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
# 13. MODEL COMPARISON
result=pd.DataFrame([["K-Means",km],["GMM",gmm],["Hierarchical",hier],["DBSCAN",db]],columns=["Model","Silhouette"])
print("\nMODEL COMPARISON")
print(result)
# 14. COMPARISON GRAPH
result.plot(x="Model",y="Silhouette",kind="bar",ylim=(0,1))
plt.title("Model Comparison")
plt.ylabel("Silhouette Score")
plt.show()
# 15. BEST MODEL
best=result.loc[result["Silhouette"].idxmax()]
print("\nBEST MODEL:",best["Model"])
print("BEST SILHOUETTE:",best["Silhouette"])