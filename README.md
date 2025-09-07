# MLOps Projects Collection

This repository contains multiple Machine Learning Operations (MLOps) projects demonstrating different aspects of ML lifecycle management, experiment tracking, and model deployment using modern MLOps tools and practices.

## Projects Overview

### 🏠 [House Price Prediction](./House-Price-Prediction/)
**Focus**: Basic MLOps with Classification
- **Algorithm**: Logistic Regression on Iris Dataset
- **MLOps Stack**: MLflow for experiment tracking and model registry
- **Key Features**: Parameter logging, model versioning, accuracy tracking
- **Complexity**: Beginner-friendly MLOps implementation

### 🍷 [Wine Quality Prediction](./Wine-quality-Pred/)
**Focus**: Advanced MLOps with Deep Learning
- **Algorithm**: Artificial Neural Networks with hyperparameter optimization
- **MLOps Stack**: MLflow + Hyperopt for automated ML experimentation
- **Key Features**: Bayesian optimization, nested experiment tracking, automated model selection
- **Complexity**: Advanced MLOps pipeline with automated hyperparameter tuning

### 🚀 [NASA APOD Pipeline](./nasa_apod/)
**Focus**: Data Engineering with Apache Airflow
- **Pipeline**: NASA Astronomy Picture of the Day ETL
- **Stack**: Apache Airflow, Docker, Python
- **Key Features**: Automated data extraction, workflow orchestration, containerized deployment
- **Complexity**: Production-ready data pipeline with scheduling and monitoring

## Common MLOps Practices Demonstrated

### 🔬 Experiment Tracking
- Comprehensive parameter and metric logging
- Experiment comparison and analysis
- Reproducible ML workflows
- Version control for datasets and models

### 📊 Model Management
- Model registry for version control
- Artifact storage and retrieval
- Model deployment preparation
- Performance monitoring and comparison

### 🚀 Automation
- Automated hyperparameter optimization
- Continuous model evaluation
- Streamlined ML pipeline execution
- Integrated model validation

## Technology Stack

- **ML Frameworks**: scikit-learn, TensorFlow/Keras
- **MLOps Platform**: MLflow (tracking, registry, deployment)
- **Optimization**: Hyperopt with TPE algorithm
- **Data Engineering**: Apache Airflow, Docker
- **Data Processing**: pandas, NumPy
- **Visualization**: MLflow UI for experiment analysis

## Project Structure
```
Mlops/
├── House-Price-Prediction/     # Basic MLOps with regression
│   ├── main.ipynb
│   ├── mlruns/
│   ├── mlartifacts/
│   └── README.md
├── Wine-quality-Pred/          # Advanced MLOps with deep learning
│   ├── main.ipynb
│   ├── mlruns/
│   └── README.md
├── nasa_apod/                  # Data engineering with Airflow
│   ├── dags/
│   │   └── etl.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── README.md
├── requirements.txt            # Project dependencies
└── README.md                   # This file

```

## Key Learning Outcomes

- Understanding MLflow ecosystem and capabilities
- Implementing experiment tracking in ML projects
- Managing model lifecycle from training to deployment
- Automating hyperparameter optimization
- Building reproducible ML pipelines
- Data pipeline orchestration with Apache Airflow
- Containerized deployment strategies
- Comparing different MLOps approaches and tools
