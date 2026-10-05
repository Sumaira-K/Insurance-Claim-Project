# Insurance Claim Risk & Premium Predictor

An end-to-end machine learning project that predicts **insurance premium amounts** and **claim risk** from customer and policy-related information.

The project combines **data generation, exploratory data analysis, preprocessing, supervised machine learning, model evaluation, and a Streamlit-based prediction interface** into a complete ML workflow.

---

## Project Overview

Insurance premium estimation and claim-risk assessment involve multiple customer and policy-related factors. This project demonstrates how supervised machine learning can be used to analyze these factors and generate automated predictions.

The system addresses two machine learning tasks:

1. **Premium Amount Prediction** — A regression model predicts the expected insurance premium amount.
2. **Claim Risk Prediction** — A classification model predicts whether a customer is classified as higher or lower claim risk.

The trained models are integrated into a **Streamlit web interface** where users can enter insurance information and receive predictions without manually running the machine learning workflow.

---

## Key Features

* **Insurance Premium Prediction**
* **Claim Risk Classification**
* End-to-end machine learning workflow
* Exploratory Data Analysis (EDA)
* Numerical and categorical feature preprocessing
* Saved preprocessing pipeline
* Saved trained machine learning models
* Interactive Streamlit prediction interface
* Light and dark theme support
* Dedicated project information page
* Clean and modular application structure

---

## Project Results

### Premium Prediction

The final regression model achieved:

| Metric   |     Result |
| -------- | ---------: |
| R² Score | **0.9590** |

An R² score of 0.9590 indicates that the final model explains a large proportion of the variation in the insurance premium values within the evaluation data.

### Claim Risk Prediction

The final classification model achieved:

| Metric   |     Result |
| -------- | ---------: |
| Accuracy | **72.25%** |
| ROC-AUC  | **0.8023** |

The ROC-AUC score indicates that the model provides useful discrimination between the two claim-risk classes.

---

## Machine Learning Problems

### 1. Premium Amount Prediction — Regression

The first task predicts the expected **insurance premium amount** for a customer.

**Target variable:** `premium_amount`

Since the target is a continuous numerical value, the problem is treated as a **regression task**.

The model uses customer, policy, claim-history, income, and coverage-related information to estimate the expected premium.

---

### 2. Claim Risk Prediction — Classification

The second task predicts the **claim-risk category** of a customer.

**Target variable:** `claim_risk`

Since the target represents discrete classes, the problem is treated as a **classification task**.

The classification model uses customer and policy-related characteristics to identify the predicted claim-risk category.

---

## Dataset

The project uses a **synthetically generated insurance dataset containing 2,000 records and 10 variables**.

The dataset includes:

| Feature         | Description                        |
| --------------- | ---------------------------------- |
| Age             | Age of the customer                |
| BMI             | Body Mass Index                    |
| Dependents      | Number of dependents               |
| Smoker          | Smoking status                     |
| Policy Type     | Type of insurance policy           |
| Claim History   | Previous claim history             |
| Annual Income   | Customer's annual income           |
| Coverage Amount | Insurance coverage amount          |
| Claim Risk      | Target variable for classification |
| Premium Amount  | Target variable for regression     |

The synthetic dataset was generated to provide controlled insurance-related data for demonstrating the complete machine learning workflow.

---

## Project Workflow

```text
Insurance Dataset
       ↓
Data Understanding
       ↓
Exploratory Data Analysis
       ↓
Feature Preparation
       ↓
Feature Encoding & Preprocessing
       ↓
Train-Test Split
       ↓
Model Training
       ↓
Model Evaluation
    ↙          ↘
Regression   Classification
    ↓              ↓
Premium        Claim Risk
Prediction     Prediction
       ↓
Saved Models
       ↓
Streamlit Interface
       ↓
User Predictions
```

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the characteristics and relationships within the insurance dataset.

The analysis included:

* Distribution analysis of numerical variables
* Analysis of categorical variables
* Premium distribution analysis
* Claim-risk distribution
* Correlation analysis
* Relationship analysis between customer characteristics and premium
* Analysis of factors associated with claim risk

The EDA helped identify patterns in the dataset and provided a better understanding of the variables before model training.

---

## Data Preprocessing

The input features were prepared for machine learning using a preprocessing pipeline.

The preprocessing workflow includes:

* Separation of input features and target variables
* Encoding of categorical features
* Transformation of numerical features where required
* Preparation of training and testing data
* Consistent preprocessing of data before prediction

The preprocessing pipeline used during model training is saved as:

```text
preprocessor.pkl
```

This allows the same preprocessing workflow to be applied when new user inputs are passed through the Streamlit application.

---

## Machine Learning Models

### Premium Prediction

A regression model was trained to predict the continuous `premium_amount` target.

The final trained regression model is stored as:

```text
premium_prediction_model.pkl
```

### Claim Risk Prediction

A classification model was trained to predict the `claim_risk` target.

The final trained classification model is stored as:

```text
claim_risk_model.pkl
```

The final models were selected based on their evaluation performance during the model development process.

---

## Model Evaluation

### Regression

The premium prediction model was evaluated using regression performance measures, including:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

The final model achieved an **R² score of 0.9590**.

### Classification

The claim-risk model was evaluated using classification performance measures including:

* Accuracy
* ROC-AUC

The final classification model achieved:

* **Accuracy: 72.25%**
* **ROC-AUC: 0.8023**

These metrics were used to assess the model's predictive performance on the evaluation data.

---

## Streamlit Application

The trained machine learning models are integrated into a Streamlit application.

The application provides two main sections:

### Prediction

The prediction interface allows the user to enter the required insurance-related information and obtain:

* Predicted insurance premium
* Predicted claim risk

The application loads the saved preprocessing pipeline and trained models to generate predictions.

### About Project

The About Project section provides information about:

* Project purpose
* Machine learning approach
* Dataset
* Technologies used
* Project workflow

### Light & Dark Mode

The application includes a complete **light/dark theme system**.

The theme changes consistently across the interface, including:

* Backgrounds
* Cards
* Text
* Input fields
* Buttons
* Borders
* Navigation elements
* Prediction results

---

## Technology Stack

| Technology           | Purpose                                      |
| -------------------- | -------------------------------------------- |
| **Python**           | Core programming and ML workflow             |
| **Pandas**           | Data manipulation and analysis               |
| **NumPy**            | Numerical computing                          |
| **Matplotlib**       | Data visualization                           |
| **Seaborn**          | Statistical visualization                    |
| **Scikit-learn**     | Preprocessing, model training and evaluation |
| **Jupyter Notebook** | Data analysis and model development          |
| **Streamlit**        | Interactive prediction interface             |
| **CSS**              | Custom application styling                   |
| **Git & GitHub**     | Version control and project management       |

---

## Project Structure

```text
Insurance-Claim-Project/
│
├── app.py
├── theme.py
├── style.css
├── README.md
├── Insurance_Claim_Risk_Predictor.ipynb
├── insurance_claim_data.csv
├── preprocessor.pkl
├── premium_prediction_model.pkl
├── claim_risk_model.pkl
│
└── pages/
    ├── 1_Predict.py
    └── 2_About_Project.py
```

### Important Files

**`app.py`**
Main entry point of the Streamlit application.

**`theme.py`**
Manages the application's light and dark theme functionality.

**`style.css`**
Contains custom styling used to create the application's visual design.

**`Insurance_Claim_Risk_Predictor.ipynb`**
Contains the data analysis, exploratory analysis, preprocessing, model development and evaluation workflow.

**`insurance_claim_data.csv`**
Contains the synthetic insurance dataset used for model development.

**`preprocessor.pkl`**
Saved preprocessing pipeline used to transform input data before prediction.

**`premium_prediction_model.pkl`**
Saved trained regression model for premium prediction.

**`claim_risk_model.pkl`**
Saved trained classification model for claim-risk prediction.

**`pages/1_Predict.py`**
Contains the prediction interface.

**`pages/2_About_Project.py`**
Contains information about the project and its implementation.

---

## Business Applications

The machine learning concepts demonstrated in this project can support insurance-related use cases such as:

* Premium estimation
* Customer risk assessment
* Underwriting support
* Claim-risk analysis
* Customer profiling
* Data-driven insurance decision support

This project is intended as an **educational and portfolio implementation** and is not designed to replace professional insurance underwriting or claims assessment.

---

## Future Scope

Possible future extensions include:

* Hyperparameter optimization
* Cross-validation for more robust model evaluation
* Advanced ensemble models
* Explainable AI techniques such as SHAP
* Real-world insurance datasets
* Database integration
* Prediction history and analytics
* Cloud deployment
* Model monitoring and performance tracking

These are **future possibilities and are not part of the current implementation**.

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Sumaira-K/Insurance-Claim-Project.git
cd Insurance-Claim-Project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application provides the prediction interface along with the project information page.

The theme control allows users to switch between **light and dark mode**.

### 6. Run the Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
Insurance_Claim_Risk_Predictor.ipynb
```

and execute the notebook cells sequentially.

---

## Learning Outcomes

This project provided practical experience in developing a machine learning solution from dataset generation through deployment-oriented integration.

Key learning outcomes include:

* Translating a real-world problem into regression and classification tasks
* Working with numerical and categorical features
* Performing exploratory data analysis
* Building preprocessing pipelines
* Training supervised machine learning models
* Evaluating regression and classification models
* Saving trained models for reuse
* Integrating machine learning models into a Streamlit application
* Designing a modular and user-friendly ML interface
* Managing a project using Git and GitHub

---

## Author

**Sumaira K**

B.Tech Computer Science and Engineering Student

GitHub: [Sumaira-K](https://github.com/Sumaira-K)

---

## License

This project is developed for **educational and portfolio purposes**.
