# Height to Weight Prediction

A beginner-friendly Flask application using Simple Linear Regression.

## Important details about the supplied dataset
- File: `data.csv`
- Columns: `Height`, `Weight`
- Height values are in metres (for example, 1.70 means 170 cm).
- Weight values are in kilograms.
- The observed height range is 1.47 m to 1.83 m.
- The website accepts centimetres and converts them to metres before prediction.

## 1. Create and activate a virtual environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```

## 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 3. Train the model and create the Pickle file
```bash
python train_model.py
```
This prints MAE, RMSE and R-squared on a held-out test split, then trains the final model on all valid rows and saves `linear_regression_model.pkl`.

## 4. Run locally
```bash
python app.py
```
Open http://127.0.0.1:5000

## 5. GitHub
Create a GitHub repository, then run in this folder:
```bash
git init
git add .
git commit -m "Height weight prediction project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Height-Weight-Prediction.git
git push -u origin main
```

## 6. Render deployment
Create a Web Service and connect the GitHub repository.

Build command:
```bash
pip install -r requirements.txt && python train_model.py
```

Start command:
```bash
gunicorn app:app
```

The build command creates the Pickle model from `data.csv` in the Render build environment.

## Limitations
This dataset has only 15 observations. A random 20% test split contains only 3 observations, so evaluation metrics can change substantially depending on the split. The model should be treated as a learning demonstration, not a medically reliable weight estimator. Avoid predicting outside the observed height range.
