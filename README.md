
# Diabetes Prediction App 🩺📈

![App Screenshot 1](readme_preview_image.png)




## Features

- **User-Friendly Interface**: The app offers a sleek and engaging user interface that allows users to input key health attributes effortlessly.

- **Predictive Power**: Utilizing a trained Support Vector Machine (SVM) model, the app accurately predicts whether a person is likely to have diabetes or not.

- **Real-Time Predictions**: Users can instantly receive predictions by inputting their health attributes and clicking the "Predict" button.

- **Dynamic Results**: Predictions are displayed with visually appealing dynamic messages, adding a touch of interactivity to the prediction process.



## Project Details

### Dataset

The Diabetes Prediction App is powered by a carefully curated dataset containing health attributes of individuals. The dataset includes features such as:

- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age


### Models and Accuracy Summary

The app employs a variety of machine learning models to predict the likelihood of diabetes. The following models were considered:

- Support Vector Machine (SVM)
- Random Forest
- Decision Tree
- k-Nearest Neighbors (KNN)
- Logistic Regression
- Naive Bayes

After testing and evaluation, the Support Vector Machine (SVM) model emerged as the top performer, achieving an impressive accuracy of approximately 77%. This model was trained using a comprehensive set of features from the dataset.

| Model              | Accuracy       |
|--------------------|----------------|
| Support Vector Machine (SVM)   | 77%            |
| Random Forest      | 75%            |
| Decision Tree      | 71%            |
| k-Nearest Neighbors (KNN)       | 73%            |
| Logistic Regression| 75%            |
| Naive Bayes        | 76%            |



## Installation and Usage

Clone the repository:
```bash
git clone https://github.com/minkvirparia/diabetes-prediction-app.git
```


Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```  
## Demo

[Find the Demo here!](https://huggingface.co/spaces/mink-virparia/background-removal-app)
