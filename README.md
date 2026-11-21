# Height to Weight Prediction Using Machine Learning

## Project Overview

This project predicts a person's estimated weight based on their height using Machine Learning.

A **Simple Linear Regression** algorithm is used to train the model using a height and weight dataset. The trained model is saved as a `.pkl` file and integrated into a Flask web application.

Users can enter their height in centimetres on the website and get an estimated weight in kilograms.

## Technologies Used

- **Python** – Programming language
- **Pandas** – Dataset handling
- **NumPy** – Numerical calculations
- **Scikit-learn** – Machine Learning model
- **Flask** – Backend web framework
- **HTML** – Webpage structure
- **CSS** – Frontend styling
- **Google Colab** – Model training
- **PyCharm** – Python development environment
- **GitHub** – Source code hosting
- **Render** – Web application deployment

## Dataset Information

The project uses a dataset named `data.csv`.

The dataset contains two columns:

| Column | Description |
|---|---|
| Height | Person's height in metres |
| Weight | Person's weight in kilograms |

- Total records: 15
- Height range: 1.47 m to 1.83 m
- Target variable: Weight
- Input feature: Height

## Machine Learning Algorithm

**Simple Linear Regression**

Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value.

In this project:
- Input: Height
- Output: Predicted Weight

The model was trained in Google Colab and saved as:

`linear_regression_model.pkl`

The saved model is loaded into the Flask application using Python's Pickle module.

## Project Structure

```text
Height_Weight_Prediction/
│
├── app.py
├── data.csv
├── linear_regression_model.pkl
├── requirements.txt
│
└── templates/
    └── index.html
```

## How the Project Works

1. Collect the height and weight dataset.
2. Load and explore the dataset using Python.
3. Prepare the input and output features.
4. Train a Simple Linear Regression model in Google Colab.
5. Save the trained model as a `.pkl` file.
6. Download the model and place it in the Flask project folder.
7. Create a Flask application using Python.
8. Connect the trained model with Flask.
9. Create a simple frontend using HTML and CSS.
10. Accept height in centimetres from the user.
11. Convert the height from centimetres to metres before passing it to the model.
12. Display the predicted weight in kilograms.
13. Upload the project to GitHub.
14. Deploy the application using Render.

## Installation and Setup

### 1. Clone the GitHub Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Height_Weight_Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open the Website

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

Enter your height in centimetres and click the **Predict Weight** button.

## Deployment

The project can be deployed online using Render.

Deployment steps:

1. Upload the project files to GitHub.
2. Log in to Render.
3. Create a new Web Service.
4. Connect your GitHub repository.
5. Set the build command:

```bash
pip install -r requirements.txt
```

6. Set the start command:

```bash
gunicorn app:app
```

7. Click Deploy.
8. After successful deployment, Render provides a public website URL.

## Project Features

- Predicts estimated weight based on height.
- Uses a trained Linear Regression model.
- Simple and user-friendly interface.
- Flask backend integration.
- HTML and CSS frontend.
- Displays predictions in kilograms.
- Can be deployed online using Render.

## Limitations

- The dataset contains only 15 records.
- The model is trained on heights between 147 cm and 183 cm.
- Predictions outside this range may be unreliable.
- The predicted weight is an estimate, not a medical recommendation.

## Future Improvements

- Use a larger dataset for better model generalization.
- Experiment with different Machine Learning algorithms.
- Improve model evaluation.
- Enhance the website interface.
- Add more input features if suitable data is available.

## Conclusion

This project demonstrates how Machine Learning can be integrated into a web application using Python and Flask.

It provides practical experience in dataset handling, model training, model saving, backend development, frontend design, GitHub version control, and cloud deployment.

---

**Project Name:** Height to Weight Prediction Using Machine Learning

**Algorithm:** Simple Linear Regression

**Developed Using:** Python, Flask, HTML, CSS and Scikit-learn