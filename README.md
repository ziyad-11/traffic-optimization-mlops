# Traffic Optimization System using MLOps

## Project Overview
Traffic congestion is a major problem in large cities like Mumbai. This project aims to predict traffic density based on different factors such as day, time, weather conditions, festivals, and vehicle count. Based on the predicted traffic density, the system suggests optimized traffic signal timings to reduce congestion and waiting time.

This project demonstrates the implementation of a complete **MLOps pipeline** including data preprocessing, machine learning models, API deployment, containerization, and CI/CD integration.

---

## Problem Statement
Traffic signals in many cities operate on fixed timers, which often leads to unnecessary waiting and congestion. This project proposes a machine learning based traffic optimization system that dynamically predicts traffic conditions and suggests optimized signal timings.

---

## Dataset
The dataset used in this project contains **5000 records** and includes the following features:

- Day of the week
- Hour of the day
- Festival indicator
- Rain indicator
- Weather condition
- Vehicle count
- Traffic density (target variable)

The dataset was created by integrating traffic-related attributes from multiple online sources and simulated parameters.

---

## Technologies Used

- Python
- Scikit-learn
- FastAPI
- Docker
- Git
- GitHub Actions


## MLOps Tools Used
- Version control using Git
- Repository management on GitHub
- CI/CD pipeline implemented using Jenkins
- Containerization using Docker
- API deployment using FastAPI

---

## Machine Learning Techniques

### PCA (Principal Component Analysis)
Used for dimensionality reduction to remove redundant features and improve model efficiency.

### Random Forest
An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy.

### SVM (Support Vector Machine)
Used to find optimal decision boundaries in the data to predict traffic density.

---

## Project Architecture
```mermaid
flowchart TD
    A["Dataset"] --> B["Data Preprocessing"]
    B --> C["Feature Encoding"]
    C --> D["PCA (Dimensionality Reduction)"]
    D --> E["Model Training (Random Forest + SVM)"]
    E --> F["Prediction System"]
    F --> G["FastAPI Deployment"]
    G --> H["Docker Container"]
    H --> I["GitHub Repository"]
    I --> J["CI/CD Pipeline"]
---

## API Deployment

The model is deployed using **FastAPI**, allowing users to send traffic parameters and receive predicted traffic density and recommended signal timing.

Example output:

Traffic Density: 0.72  
Traffic Level: High  
Recommended Signal Time: 90 seconds

---

## MLOps Components Implemented

- Version control using Git
- GitHub repository management
- Docker containerization
- CI/CD pipeline using GitHub Actions
- API deployment using FastAPI

---

## Future Improvements

- Integration with real-time traffic APIs
- IoT-based vehicle sensors at intersections
- Use of deep learning models for long-term traffic prediction
- Integration with smart city infrastructure

---

## Author

Ziyad Mulla  
MLOps Project – Traffic Optimization System
