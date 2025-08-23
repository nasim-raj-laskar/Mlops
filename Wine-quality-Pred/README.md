# Wine Quality Prediction MLOps Project

## Overview
This project implements an advanced MLOps pipeline for wine quality prediction using Artificial Neural Networks (ANN) with automated hyperparameter optimization and comprehensive experiment tracking.

## Features
- **Dataset**: Wine Quality dataset (white wine)
- **Algorithm**: Deep Neural Network with hyperparameter optimization
- **MLOps Tools**: MLflow + Hyperopt for automated ML experimentation
- **Optimization**: Bayesian optimization using Tree-structured Parzen Estimator (TPE)
- **Model Management**: Automated model registration and versioning

## Project Structure
```
Wine-quality-Pred/
├── main.ipynb              # Complete ML pipeline notebook
├── mlruns/                 # MLflow experiment tracking data
└── README.md              # This file
```

## Technical Architecture

### Neural Network Design
- **Input Layer**: 11 features (wine chemical properties)
- **Hidden Layer**: 64 neurons with ReLU activation
- **Output Layer**: 1 neuron (quality score regression)
- **Normalization**: Built-in feature normalization layer
- **Optimizer**: SGD with configurable learning rate and momentum

### Hyperparameter Optimization
- **Framework**: Hyperopt with TPE algorithm
- **Search Space**:
  - Learning Rate: Log-uniform distribution (1e-5 to 1e-0)
  - Momentum: Uniform distribution (0.0 to 1.0)
- **Evaluation Metric**: Root Mean Square Error (RMSE)
- **Optimization Runs**: 4 trials with nested MLflow tracking

### Data Pipeline
- **Train/Test Split**: 80/20 with stratification
- **Validation Split**: 20% of training data for model evaluation
- **Feature Scaling**: Automatic normalization within the neural network
- **Target**: Wine quality scores (continuous values)

## Key Results
- **Best RMSE**: 0.948 (achieved with optimized hyperparameters)
- **Optimal Parameters**:
  - Learning Rate: ~0.0019
  - Momentum: ~0.752
- **Model Architecture**: Successfully handles 11-dimensional input space

## MLflow Integration

### Experiment Tracking
- **Parent Runs**: Track hyperparameter optimization sessions
- **Child Runs**: Individual model training runs with specific parameters
- **Metrics**: RMSE, training/validation loss curves
- **Artifacts**: Complete model serialization with TensorFlow format

### Model Registry
- **Model Name**: "WineQualityModel"
- **Versioning**: Automatic version management
- **Model Format**: TensorFlow/Keras with MLflow wrapper
- **Inference**: Ready for production deployment

## Getting Started

1. **Install Dependencies**
   ```bash
   pip install tensorflow pandas scikit-learn mlflow hyperopt
   ```

2. **Start MLflow Tracking Server**
   ```bash
   mlflow server --host 127.0.0.1 --port 5000
   ```

3. **Run the Pipeline**
   - Open `main.ipynb` in Jupyter
   - Execute cells to run automated hyperparameter optimization
   - Monitor progress in MLflow UI

4. **Model Inference**
   ```python
   import mlflow
   model = mlflow.pyfunc.load_model("models:/WineQualityModel/1")
   predictions = model.predict(test_data)
   ```

## Advanced Features

### Automated Hyperparameter Tuning
- Uses Bayesian optimization for efficient parameter search
- Nested MLflow runs for comprehensive experiment tracking
- Early stopping and convergence detection

### Model Validation
- Comprehensive input validation with serving payload testing
- Model signature inference for production deployment
- Artifact integrity verification

### Production Readiness
- Model registry integration for version control
- Standardized model serving format
- Comprehensive logging and monitoring setup

## Dataset Information
- **Source**: MLflow test datasets (white wine quality)
- **Features**: 11 chemical properties (acidity, sugar, alcohol, etc.)
- **Target**: Quality scores (regression task)
- **Size**: ~4,900 samples with train/validation/test splits

## Experiment Management
Access the MLflow UI to:
- Compare hyperparameter optimization runs
- Analyze model performance trends
- Download trained models and artifacts
- Monitor experiment reproducibility
- Deploy models to production endpoints