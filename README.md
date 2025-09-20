# 🏡 California Housing Price Prediction

This project predicts median house prices for California districts using machine learning.  
We start from **data preprocessing** → **model experimentation** → **hyperparameter tuning** → **deployment** with a Streamlit web app.

---


---

## 📊 Dataset
The dataset is from the **California Housing** data (via Kaggle: `https://www.kaggle.com/datasets/camnugent/california-housing-prices/data`).  
Key features include:
- 🌍 `longitude`, `latitude`
- 🏠 `housing_median_age`, `total_rooms`, `total_bedrooms`
- 👨‍👩‍👧‍👦 `population`, `households`
- 💵 `median_income`
- 🌊 `ocean_proximity` *(categorical)*

Target: **`median_house_value`**

---
## 📂 Project Structure
```
california-housing/
├─ `app.py` — Streamlit app for deployment  
├─ `Data` — Folder to store data  
    ├─ `housing.csv` — Dataset used    
├─ `requirements.txt` — Dependencies for deployment  
└─ `Housing-Prices.ipynb` — Jupyter notebook with EDA & model training
```

## ⚙️ Preprocessing
* One-hot encoded the `ocean_proximity` column using `ColumnTransformer`.
* Combined numeric and categorical features into a single **`Pipeline`** for clean training and inference.

---

## 🤖 Models Tried & Results

| Model                          | RMSE ↓     | MAE ↓      | Notes |
|---------------------------------|------------|------------|------|
| **Decision Tree Regressor**     | 68,503     | 43,294     | Simple baseline |
| **Random Forest Regressor**     | 49,032     | 31,668     | Big improvement |
| **Random Forest (tuned)**       | **48,537** | **31,591** | After RandomizedSearchCV |
| **XGBoost Regressor**           | **45,463** | **29,507** | Best performance 🎯 |

> 📉 **Lower RMSE/MAE = better**.  
> XGBoost slightly outperformed the tuned Random Forest.

---

## 🛠️ Hyperparameter Tuning
Random Forest was tuned using **`RandomizedSearchCV`** with:
```python
{
 'n_estimators': 800,
 'min_samples_split': 2,
 'min_samples_leaf': 1,
 'max_features': 0.5,
 'max_depth': None
}
```
* **Scoring metric**: negative root mean squared error (neg_root_mean_squared_error).

## 🌟 Feature Importance (Random Forest)

Top predictors (approximate percentages):
* 💰 median_income ~ 42%
* 🏙️ ocean_proximity_INLAND ~ 14%
* 📍 longitude / latitude ~ 11% each
* 🏡 housing_median_age, population, total_rooms ...

## 🧩 Tech Stack
* Python 🐍
* Pandas 🐼, NumPy
* Scikit-learn 🤖
* XGBoost ⚡
* Streamlit 🌐
* Joblib (for model saving)

## 📥 Setup
1. Clone the repo:
``` bash
git clone https://github.com/yourusername/california-housing.git
```
2. Install Dependencies
``` bash
pip install -r requirements.txt
```
3. Run Locally
``` bash
streamlit run app.py
```
## 💡 Key Learnings
* How to build a full ML pipeline combining preprocessing and model.
* The importance of hyperparameter tuning to squeeze out extra performance.
* Hosting a model as a simple interactive web app locally.

### ✨ Enjoy predicting house prices! 🏠💵
