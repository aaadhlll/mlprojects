import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv") #defining variables for storing the train,test,raw data sets
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #Initialise the DataIngestionCOnfig inorder to read datas, the 3 paths get saved in this variable
        
    def initiate_data_ingestion(self): #Used ti read the datas from various data sources or databases
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') #Reading datas from any sources
            logging.info('Exported the dataset as df')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) #converting raw data into csv file

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42) #splitting the dataset into train and test

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) #saving into csv format for train

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True) #saving into csv for test

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path, #returning the datapath for the next process of data transformation
                self.ingestion_config.test_data_path,
        
            )
        except Exception as e:
            raise CustomException(e,sys)
        
    
if __name__=="__main__":
    obj= DataIngestion()
    obj.initiate_data_ingestion()