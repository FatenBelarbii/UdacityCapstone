# Stroke Predicition on Azure

In this project, we will create two models: 
- one using Automated ML;
- one customized model whose hyperparameters are tuned using HyperDrive. 
We will then compare the performance of both the models and deploy the best performing model.

![GitHub Logo](/images/capstone-diagram.png)

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset
We used the [Stroke Prediction Dataset from Kaggle](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) (11 clinical features por predicting stroke events) 

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.
This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relavant information about the patient.

### Overview: Attribute Information
1) id: unique identifier
2) gender: "Male", "Female" or "Other"
3) age: age of the patient
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6) ever_married: "No" or "Yes"
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8) Residence_type: "Rural" or "Urban"
9) avg_glucose_level: average glucose level in blood
10) bmi: body mass index
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
12) stroke: 1 if the patient had a stroke or 0 if not
*Note: "Unknown" in smoking_status means that the information is unavailable for this patient


### Task
It's a classification task that will help us predict if a patient has a high risk of having a stroke or no.

### Access
The dataset is external to the Azure ML ecosystem so we added it to our registered datasets as you can see in the following screenshots:

![GitHub Logo](/images/1.PNG)
![GitHub Logo](/images/2.PNG)

Now we can copy that code and use it to access our data and even improve it in the future (For example, add more data and versions)
![GitHub Logo](/images/3.PNG)

### Exploratory Data Analysis

Only 4.9% of people are affected by stroke so the data available to us is imbalanced and we need to balance it before giving to our machine learning algorithms.
Also, we have missing values so we added a function to prepare the data.

![GitHub Logo](/images/train.PNG)

## Automated ML
The screenshot below gives an overview of the `automl` settings and configuration used for this experiment
![GitHub Logo](/images/Capture1.PNG)
And here are the results and the details of the run
![GitHub Logo](/images/Capture2.PNG)
![GitHub Logo](/images/Capture3.PNG)
![GitHub Logo](/images/Capture4.PNG)
![GitHub Logo](/images/Capture5.PNG)

The results of the best run, of the best model
![GitHub Logo](/images/Capture6.PNG)
![GitHub Logo](/images/Capture7.PNG)

In future we can improve the best model by choosing different primary metrics and different classification methods and calculating and comparing the values of mean_squared_error, to study how our predictions have deviated from actual values and, we study mean absolute percent error (MAPE) in detail. All these could help us in reducing error in our model and help us to study the model much faster. We can also add more data to the model, or we can add more columns. Also, we can make new columns with existing ones with feature engineering and by applying our domain knowledge and obtain better results. Also, we can provide a more user-friendly user interface wile consuming the api’s and the swager documentation. Lot of steps run on command-line can be ran directly from Jyupiter notebook or could be automated in a single script.

## Hyperparameter Tuning

First the data was loaded into dataset and proper compute infra was created to run with suitable hyperdrive configuration.
Here are the run details:
![GitHub Logo](/images/Capture12.PNG)
![GitHub Logo](/images/Capture13.PNG)
These screenshots rpresent the model chosen for this experiment:
![GitHub Logo](/images/Capture14.PNG)
![GitHub Logo](/images/Capture15.PNG)

In future we can improve the best model by choosing different primary metrics and different classification methods and calculating and comparing the values of mean_squared_error, to study how our predictions have deviated from actual values and, we study mean absolute percent error (MAPE) in detail. All these could help us in reducing error in our model and help us to study the model much faster. We can also add more data to the model, or we can add more columns. Also, we can make new columns with existing ones with feature engineering and by applying our domain knowledge and obtain better results. Also, we can provide a more user-friendly user interface wile consuming the api’s and the swager documentation. Lot of steps run on command-line can be ran directly from Jyupiter notebook or could be automated in a single script. We also do have room to select more hyperparameters to tune.

## Model Deployment
Active Endpoint for Depoloyed Model:
![GitHub Logo](/images/Capturefghj.PNG)

Active Endpoint for Depoloyed Model Tested:
![GitHub Logo](/images/Capture8.PNG)
![GitHub Logo](/images/Capture9.PNG)
![GitHub Logo](/images/Capture10.PNG)
![GitHub Logo](/images/Capture11.PNG)

## Screen Recording
Full recording: https://www.youtube.com/watch?v=m0Qa34vFsmM

## Standout Suggestions
Application Insights Were Enlabled and a .onnx model was generated for AutoML Method.
