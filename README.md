# Car Price Prediction

This project aims to predict the price of cars using machine learning techniques, specifically the XGBoost algorithm. The model is trained on a dataset containing various features of cars, such as the make, model, year, mileage, fuel type, and other relevant factors.

## Dataset

The dataset used for this project consists of a collection of car listings, each with associated features and the corresponding price. The dataset is preprocessed to handle missing values, categorical variables, and feature scaling, ensuring the data is suitable for training the XGBoost model.

Dataset link: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho?select=car+data.csv 

## XGBoost Algorithm

XGBoost is an optimized gradient-boosting algorithm that has gained popularity in machine learning competitions and has become a popular choice for predictive modeling tasks. It is known for its efficiency, accuracy, and flexibility. XGBoost combines multiple weak prediction models (decision trees) to create a strong ensemble model.

## Dependencies

The following dependencies are required to run the project:

- Python 3.x
- XGBoost
- NumPy
- Pandas
- Scikit-learn
- Streamlit

To install the required dependencies, you can use the following command:

```shell
pip install xgboost numpy pandas scikit-learn streamlit
```

## Usage
Clone the repository:
```shell
git clone https://github.com/your-username/car-price-prediction.git
```

Navigate to the project directory:
```shell
cd car-price-prediction
```

Install the dependencies:
```shell
pip install -r requirements.txt
```

Run the Streamlit app:
```shell
streamlit run app.py
```
Open your browser and go to http://localhost:8501 to access the car price prediction app.  
## Deployment Link:
https://car-price-prediction-model.streamlit.app/ 

## App Workflow
The Streamlit app provides a user-friendly interface to interact with the trained model. The user can input various car features and obtain a predicted price based on the trained XGBoost model. The steps involved in the app workflow are as follows:

1. The user enters the relevant details of the car, such as the make, model, year, mileage, fuel type, etc., in the input fields provided.
2. Upon clicking the "Predict" button, the app sends the entered information to the XGBoost model.
3. The model processes the input features and returns a predicted price for the car.
4. The predicted price is displayed on the app interface, giving the user an estimate of the car's market value.

![car price prediction](https://github.com/shruti-2412/Car-Price-Prediction/assets/99483160/377e1950-c6f4-46dc-bd4d-82b5fbe024ea)


## Disclaimer
The car price predictions provided by this project are based on a machine-learning model and may not always accurately reflect the real market prices. The predictions should be used for reference purposes only, and actual car prices can vary due to various factors.
