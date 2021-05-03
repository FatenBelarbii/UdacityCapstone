from sklearn.linear_model import LogisticRegression
import argparse
import os
import joblib
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from azureml.core.run import Run
import numpy as np
from azureml.data.dataset_factory import TabularDatasetFactory

def Impute_missing_values(df):
    df.drop(columns=['id'],inplace=True)
    
    #fill na
    df['age'].fillna(df['age'].median(), inplace=True)
    df['hypertension'].fillna(df['hypertension'].median(), inplace=True)
    df['heart_disease'].fillna(df['heart_disease'].median(), inplace=True)
    df['avg_glucose_level'].fillna(df['avg_glucose_level'].median(), inplace=True)
    
    #non categorical data
    from sklearn.preprocessing import OrdinalEncoder
    ord_enc = OrdinalEncoder()
    df["gender"] = ord_enc.fit_transform(df[["gender"]])
    df["ever_married"] = ord_enc.fit_transform(df[["ever_married"]])
    df["work_type"] = ord_enc.fit_transform(df[["work_type"]])
    df["Residence_type"] = ord_enc.fit_transform(df[["Residence_type"]])
    df["bmi"] = ord_enc.fit_transform(df[["bmi"]])
    df["smoking_status"] = ord_enc.fit_transform(df[["smoking_status"]])
    
    return df

def clean_data(df):
    df = Impute_missing_values(df)
    df.head()
    x_df = df
    y_df = x_df.pop("stroke")
    return x_df, y_df

#Load dataset
# df = pd.read_csv('https://github.com/FatenBelarbii/UdacityCapstone/blob/main/data/healthcare-dataset-stroke-data.csv')
from azureml.core import Workspace, Dataset

subscription_id = 'fa3dfb7e-5583-41a5-b60c-022e3fcc2942'
resource_group = 'mlops-rg-templateml'
workspace_name = 'mlops-aml-ws-templateml'

workspace = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(workspace, name='HealthCareDataset_StrokeData')
df = dataset.to_pandas_dataframe()

#Clean the dataset
x, y = clean_data(df)

#Split the dataset into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

run = Run.get_context()

def main():
    #Add arguments to script
    parser = argparse.ArgumentParser()
    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")
    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))
    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    run.log("accuracy", np.float(accuracy))
   
   #Dump the model using joblib
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=model, filename='outputs/model.pkl')

if __name__ == '__main__':
    main()
