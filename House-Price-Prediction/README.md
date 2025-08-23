# House Price Prediction MLOps Project

## Overview
This project demonstrates MLOps practices using the California Housing dataset with Random Forest Regressor and MLflow for experiment tracking and model management.

## Features
- **Dataset**: California Housing dataset (20,640 samples)
- **Algorithm**: Random Forest Regressor with hyperparameter tuning
- **MLOps Tools**: MLflow for experiment tracking, model logging, and model registry
- **Model Evaluation**: Mean Squared Error (MSE) and performance tracking

## Project Structure
```
House-Price-Prediction/
|
├── housepriceprediction.ipynb  # main script
├── mlruns/                 # MLflow experiment tracking data
├── mlartifacts/           # MLflow model artifacts
└── README.md              # This file
```

## Key Components

### Model Training
- Uses scikit-learn's California Housing dataset
- Implements Random Forest Regressor with GridSearchCV
- Achieves MSE of ~0.255 on test set

### MLflow Integration
- **Experiment Tracking**: Logs parameters, metrics, and model artifacts
- **Model Registry**: Registers best performing models
- **Model Versioning**: Tracks different model versions
- **Artifact Storage**: Stores trained models with metadata

### Parameters Tracked
- `n_estimators`: Number of trees in the forest (100, 200)
- `max_depth`: Maximum depth of trees (5, 10, None)
- `min_samples_split`: Minimum samples to split a node (2, 5)
- `min_samples_leaf`: Minimum samples in leaf nodes (1, 2)

## Getting Started

1. **Install Dependencies**
   ```bash
   pip install pandas scikit-learn mlflow
   ```

2. **Start MLflow UI**
   ```bash
   mlflow ui --port 5000
   ```

3. **Run the Notebook**
   - Open `main.ipynb` in Jupyter
   - Execute all cells to train and track experiments

4. **View Results**
   - Access MLflow UI at `http://localhost:5000`
   - Compare different experiment runs
   - View model artifacts and metrics

## Model Performance
- **Algorithm**: Random Forest Regressor
- **Test MSE**: 0.255
- **Features**: 8 (median income, house age, rooms, bedrooms, population, occupancy, latitude, longitude)
- **Target**: Median house value (in hundreds of thousands of dollars)

## MLflow Experiments
The project creates experiments with "BestRandomforest Model" registration where you can:
- Compare different hyperparameter configurations via GridSearchCV
- Track model performance with MSE metrics
- Register and version successful models
- Deploy models for house price prediction inference