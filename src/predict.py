import joblib
import numpy as np

# Load models
rf = joblib.load("models/random_forest.pkl")
svm = joblib.load("models/svm.pkl")
pca = joblib.load("models/pca.pkl")

def predict_traffic(features):

    features = np.array(features).reshape(1,-1)

    features_pca = pca.transform(features)

    rf_pred = rf.predict(features_pca)[0]
    svm_pred = svm.predict(features_pca)[0]

    # Average prediction
    density = (rf_pred + svm_pred) / 2

    if density < 0.3:
        level = "Low Traffic"
        signal_time = 30
    elif density < 0.6:
        level = "Medium Traffic"
        signal_time = 60
    else:
        level = "High Traffic"
        signal_time = 90

    return {
        "traffic_density": float(density),
        "traffic_level": level,
        "recommended_signal_time": signal_time
    }