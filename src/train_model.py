import joblib
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

from data_preprocessing import load_and_preprocess

# Load data
X,y = load_and_preprocess()

# Train test split
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# Apply PCA
pca = PCA(n_components=3)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Random Forest Model
rf = RandomForestRegressor()
rf.fit(X_train_pca,y_train)

rf_pred = rf.predict(X_test_pca)
rf_error = mean_squared_error(y_test,rf_pred)

print("Random Forest MSE:",rf_error)

# SVM Model
svm = SVR()
svm.fit(X_train_pca,y_train)

svm_pred = svm.predict(X_test_pca)
svm_error = mean_squared_error(y_test,svm_pred)

print("SVM MSE:",svm_error)

# Save models
joblib.dump(rf,"models/random_forest.pkl")
joblib.dump(svm,"models/svm.pkl")
joblib.dump(pca,"models/pca.pkl")

print("Models saved successfully")