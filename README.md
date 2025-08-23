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
- **Data Processing**: pandas, NumPy
- **Visualization**: MLflow UI for experiment analysis

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Mlops
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start MLflow Tracking Server**
   ```bash
   mlflow server --host 127.0.0.1 --port 5000
   ```

4. **Explore Projects**
   - Navigate to individual project folders
   - Follow project-specific README instructions
   - Run Jupyter notebooks to see MLOps in action

## Project Structure
```
Mlops/
├── House-Price-Prediction/     # Basic MLOps with classification
│   ├── main.ipynb
│   ├── mlruns/
│   ├── mlartifacts/
│   └── README.md
├── Wine-quality-Pred/          # Advanced MLOps with deep learning
│   ├── main.ipynb
│   ├── mlruns/
│   └── README.md
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## Learning Path

1. **Start with House Price Prediction** for basic MLOps concepts
2. **Progress to Wine Quality Prediction** for advanced techniques
3. **Compare approaches** to understand different MLOps strategies
4. **Experiment with modifications** to deepen understanding

## Key Learning Outcomes

- Understanding MLflow ecosystem and capabilities
- Implementing experiment tracking in ML projects
- Managing model lifecycle from training to deployment
- Automating hyperparameter optimization
- Building reproducible ML pipelines
- Comparing different MLOps approaches and tools

## Contributing

Feel free to contribute by:
- Adding new MLOps projects
- Improving existing implementations
- Enhancing documentation
- Sharing best practices and lessons learned

---

*This repository serves as a practical guide to MLOps implementation, showcasing both fundamental and advanced techniques for managing machine learning workflows in production environments.*