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
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment
![GitHub Logo](/images/Capture1.PNG)
![GitHub Logo](/images/Capture2.PNG)
![GitHub Logo](/images/Capture3.PNG)
![GitHub Logo](/images/Capture4.PNG)
![GitHub Logo](/images/Capture5.PNG)

![GitHub Logo](/images/Capture6.PNG)
![GitHub Logo](/images/Capture7.PNG)

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
