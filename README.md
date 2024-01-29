# Algerian Forest Fire Prediction

## Overview
This repository contains the code for building a machine learning model on the Algerian Forest Fire dataset. The goal of this project is to predict forest fire occurrences in Algeria using regression algorithms.

## Dataset
The dataset used for this project includes information about forest fires in Algeria. The following tasks were performed during the Exploratory Data Analysis (EDA):

- Checked dataset description and information.
- Identified and handled missing values.
- Removed duplicated values.

## Exploratory Data Analysis (EDA)

The EDA process involved exploring the dataset to gain insights into its structure and characteristics. The following steps were taken:

1. Checked dataset description and information.
2. Investigated missing values and handled them appropriately.
3. Removed duplicated values from the dataset.

## Model Training

### Feature Scaling and Extraction

- Performed feature scaling and extraction on the cleaned dataset.
- Utilized standardization on the feature data.

### Regression Algorithms

Trained the model using four regression algorithms:

1. **Linear Regression**
2. **Ridge Regression**
3. **Lasso Regression**
4. **ElasticNet Regression**

### Model Selection

After training the models, the performance metrics (mean absolute error and R2 score) were evaluated for each regression algorithm. The Ridge Regression algorithm demonstrated the best performance, and thus, it was selected for further use.

### Model Serialization

A pickle file was created to save the trained Ridge Regression model and the scaled feature data.

## Web Application

A simple web application was built using Flask and HTML. The application includes a homepage where users can interact with the trained model. The model is loaded, and predictions are made based on user inputs.

## Usage

To run the web application:

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Access the web application through your web browser.

## File Structure

- `Dataset/`: Contains the dataset used for training the model.
- `Model Training/` : Contains two files , in first we performed EDA on Algerian Forest Fire Dataset ,and in second performed Model Training on Cleaned Algerian Foresr Fire Datset
- `Models/`: Includes the saved Ridge Regression model and scaled feature data pickle file.
- `templates/`: Contain files related to the web application.
- `app.py`: Main file for running the Flask application.
- `info.txt`: Contains Information about the Algerian Foresr Fire Dataset

Feel free to explore and contribute to this project. If you have any questions or suggestions, please create an issue.

**Note:** This project was developed as part of a machine learning exploration and may not be suitable for production use without further refinement and testing.
