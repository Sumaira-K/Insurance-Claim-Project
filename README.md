# Insurance Claim & Premium Prediction

An end-to-end machine learning project that analyzes insurance customer data to **predict insurance premium amounts** and **classify claim risk** using supervised learning techniques.

The project demonstrates a complete machine learning workflow — from data generation and exploratory data analysis to preprocessing, model training, evaluation, and interpretation.

---

## Project Overview

Insurance companies need reliable ways to estimate customer premiums and identify customers who may represent higher claim risk.

This project addresses two related machine learning problems:

1. **Insurance Premium Prediction** — Predict the expected insurance premium amount using regression.
2. **Claim Risk Classification** — Predict whether a customer represents a higher or lower claim risk using classification.

The project follows an end-to-end machine learning pipeline designed to demonstrate practical skills in **Python, data analysis, feature engineering, supervised learning, and model evaluation**.

---

## Objectives

The primary objectives of this project are:

* Analyze insurance customer and policy-related data.
* Identify important factors influencing insurance premiums.
* Build a regression model to predict premium amounts.
* Develop a classification model to predict claim risk.
* Perform exploratory data analysis to identify patterns and relationships.
* Preprocess numerical and categorical features appropriately.
* Evaluate models using suitable machine learning metrics.
* Compare model performance and interpret the results.

---

## Machine Learning Problems

### 1. Premium Amount Prediction — Regression

The first problem is to predict the expected **insurance premium amount** for a customer.

**Target variable:** Insurance Premium

This is treated as a **regression problem** because the target is a continuous numerical value.

The model learns relationships between customer characteristics, policy information, and other relevant features to estimate the expected premium.

---

### 2. Claim Risk Prediction — Classification

The second problem is to determine whether a customer falls into a particular **claim-risk category**.

**Target variable:** Claim Risk

This is treated as a **classification problem** because the model predicts a discrete class.

The classification model can help identify potentially higher-risk customers and support data-driven insurance risk assessment.

---

## Project Workflow

```text
Data Generation / Collection
          ↓
Data Understanding
          ↓
Exploratory Data Analysis
          ↓
Data Cleaning
          ↓
Feature Engineering
          ↓
Feature Encoding & Scaling
          ↓
Train-Test Split
          ↓
Model Training
      ↙         ↘
Regression    Classification
      ↓             ↓
Evaluation      Evaluation
      ↓             ↓
Premium        Claim Risk
Prediction     Prediction
```

---

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) is performed to understand the dataset and discover meaningful relationships between variables.

The analysis includes:

* Distribution analysis
* Missing-value analysis
* Outlier identification
* Correlation analysis
* Categorical feature analysis
* Relationship between customer characteristics and premium
* Analysis of factors associated with claim risk

Visualizations are created using Python's data visualization libraries to make patterns and trends easier to interpret.

---

## Data Preprocessing

Before model training, the dataset is prepared using appropriate preprocessing techniques.

The preprocessing pipeline includes:

* Handling missing values
* Identifying and handling outliers where appropriate
* Encoding categorical variables
* Scaling numerical features when required
* Separating features and target variables
* Splitting the dataset into training and testing sets

Care is taken to ensure that preprocessing is performed without introducing data leakage between training and testing data.

---

## Models

### Regression

The regression component is used to estimate insurance premium amounts.

Potential regression models explored in the project include:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

The final model is selected based on its performance on the evaluation dataset.

### Classification

The classification component is used to predict claim risk.

Models explored include:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

Model selection is based on appropriate classification metrics rather than accuracy alone.

---

## Model Evaluation

### Regression Metrics

Regression models are evaluated using metrics such as:

* **MAE (Mean Absolute Error)**
* **MSE (Mean Squared Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

These metrics help measure how accurately the model predicts insurance premium amounts.

### Classification Metrics

Classification models are evaluated using:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **Confusion Matrix**

Where appropriate, additional metrics such as ROC-AUC can also be considered.

---

## Key Skills Demonstrated

This project demonstrates practical experience with:

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Exploratory Data Analysis
* Data Preprocessing
* Feature Engineering
* Regression
* Classification
* Model Evaluation
* Data Visualization
* Machine Learning Workflow

---

## Tech Stack

| Technology       | Purpose                                |
| ---------------- | -------------------------------------- |
| Python           | Core programming language              |
| Pandas           | Data manipulation and analysis         |
| NumPy            | Numerical computing                    |
| Matplotlib       | Data visualization                     |
| Seaborn          | Statistical visualization              |
| Scikit-learn     | Machine learning and preprocessing     |
| Jupyter Notebook | Experimentation and analysis           |
| Git & GitHub     | Version control and project management |

---

## Project Structure

```text
Insurance-Claim-Project/
│
├── data/
│   └── insurance_data.csv
│
├── notebooks/
│   └── insurance_claim_prediction.ipynb
│
├── models/
│   └── trained_models/
│
├── visualizations/
│   └── plots/
│
├── README.md
└── requirements.txt
```

> The project structure may evolve as additional experiments, models, and deployment components are added.

---

## Results

The project evaluates both machine learning tasks independently.

### Premium Prediction

The regression models are compared using MAE, RMSE, and R² to determine which model provides the most reliable premium predictions.

### Claim Risk Prediction

The classification models are compared using accuracy, precision, recall, F1-score, and confusion matrices to identify the most suitable model for claim-risk prediction.

**Final model performance and visual results will be documented here after model evaluation.**

---

## Business Applications

The concepts demonstrated in this project can be applied to real-world insurance workflows such as:

* Premium estimation
* Customer risk segmentation
* Underwriting support
* Claim-risk assessment
* Customer profiling
* Data-driven insurance decision making

The project is intended as an educational machine learning implementation and does not represent a production insurance underwriting system.

---

## Future Improvements

Possible extensions include:

* Hyperparameter tuning using GridSearchCV or RandomizedSearchCV
* Cross-validation for more robust model evaluation
* Advanced ensemble models such as XGBoost or Gradient Boosting
* Explainable AI using SHAP
* Automated ML pipelines
* Model deployment using Streamlit or FastAPI
* Cloud deployment
* Real-world insurance datasets
* Integration of a database for storing predictions
* Monitoring model performance after deployment

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Sumaira-K/Insurance-Claim-Project.git
cd Insurance-Claim-Project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Jupyter Notebook

```bash
jupyter notebook
```

Open the project notebook and execute the cells sequentially.

---

## Learning Outcomes

Through this project, I developed practical experience in building machine learning solutions from raw data to model evaluation.

The project strengthened my understanding of:

* Translating business problems into machine learning problems
* Choosing regression vs. classification approaches
* Preparing real-world style datasets
* Performing exploratory data analysis
* Building reproducible preprocessing workflows
* Comparing machine learning models
* Selecting evaluation metrics based on the problem
* Interpreting machine learning results

---

## Author

**Sumaira K**

B.Tech Computer Science Engineering Student

GitHub: [Sumaira-K](https://github.com/Sumaira-K)

---

## License

This project is intended for educational and portfolio purposes.
