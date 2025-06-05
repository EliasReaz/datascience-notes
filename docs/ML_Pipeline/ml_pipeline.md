# Production-ready end-to-end layout for a tabular classification ML pipeline

✅ Feature Engineering
✅ Preprocessing (Imputation + Scaling + Encoding)
✅ Handling Imbalanced Data
✅ Pipeline
✅ Cross-Validation
✅ Evaluation Metrics

## 1. Import libraries

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from imblearn.pipeline import Pipeline as ImbPipeline  # For SMOTE
from imblearn.over_sampling import SMOTE
import warnings
warnings.filterwarnings("ignore")
```

## 2. Load data

```python
df = pd.read_csv("your_dataset.csv")  # Replace with your real dataset path
```

## 3. Exploratory Data Aanlysis (EDA)

```python
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df['target'].value_counts())  # replace column name 'target' as needed
```

## 3. Feature Engineering (custom transformation)

```python
def add_custom_features(X):
    X = X.copy()
    if "applicant_income" in X and "loan_amount" in X:
        X["income_to_loan_ratio"] = X["applicant_income"] / (X["loan_amount"] + 1)
    return X

feature_engineering = FunctionTransformer(add_custom_features, validate=False)
```

## 4. Define Features and target: X, y

```python
X = df.drop("target", axis=1)
y = df["target"]
```

## 5. Train-Test Split With Stratify

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

## 6. Separate Numeric and Categorical Features

```python
num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

# Add engineered column name to num_cols if added

if "income_to_loan_ratio" not in num_cols and "income_to_loan_ratio" in X_train.columns:
    num_cols.append("income_to_loan_ratio")
```

## 7. Define Transformer

### Numerical Transformer

```python
num_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])
```

### Categorical Transformer

```python
cat_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])
```

## 8. Combine with ColumnTransformer

```python
preprocessor = ColumnTransformer(transformers=[
    ("num", num_pipeline, num_cols),
    ("cat", cat_pipeline, cat_cols)
])
```

## 9. Model & Hyperparameter Setup

```python
param_grids = {
    "LogisticRegression": {
        "classifier": [LogisticRegression(max_iter=1000, class_weight="balanced")],
        "classifier__C": [0.1, 1, 10]
    },

    "RandomForest": {
        "classifier": [RandomForestClassifier(class_weight="balanced")],
        "classifier__n_estimators": [100, 200],
        "classifier__max_depth": [None, 10, 20]
    },

    "XGBoost": {
        "classifier": [XGBClassifier(use_label_encoder=False, eval_metric="logloss")],
        "classifier__n_estimators": [100, 200],
        "classifier__max_depth": [3, 5],
        "classifier__learning_rate": [0.01, 0.1]
    }
}
```

## 9. Make a full Pipeline

* Define pipeline with a generic "classifier" step (can be any model)
  
```python
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression()) # a generic placeholder
])
```

* Note Pipeline with SMOTE for imbalance handling

```python
# pipeline = ImbPipeline(steps=[
#     ("feature_engineering", feature_engineering),
#     ("preprocessor", preprocessor),
#     ("sampler", SMOTE(random_state=42)),
#     ("classifier", RandomForestClassifier(class_weight='balanced', random_state=42))
# ])
```

## 10. Train with GridSearchCV and Select Best Model

```python
results = {}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for name, param_grid in param_grids.items():
        
    grid = GridSearchCV(estimator = pipeline, param_grid = param_grid, cv = cv, scoring="f1_macro", n_jobs=-1)
    
    # fit each model
    grid.fit(X_train, y_train)
    
    results[name] = {
        "best_score": grid.best_score_,
        "best_estimator": grid.best_estimator_, # Mean cross-validated score
        "best_params": grid.best_params_ # Best hyperparameters
    }

# Print comparison
for model_name, res in results.items():
    print(f"{model_name}: F1 Score = {res['best_score']:.4f}")

# Select best model
best_model_name = max(results, key=lambda k: results[k]['best_score'])
best_model = results[best_model_name]["best_estimator_"]
print(f"Best model: {best_model_name}")

```

## 11. Evaluate on test data - predict and evaluate on test data

```python
y_pred = best_model.predict(X_test)
y_prob = best_model.predict_proba(X_test)[:, 1]

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_prob))
```
