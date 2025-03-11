from datasets import load_dataset # type: ignore 
import pandas as pd # type: ignore
import os

raw_data_path = "data/raw/"
processed_data_path = "data/processed/"
dataset_name = "ailsntua/Chordonomicon"

os.makedirs(raw_data_path, exist_ok=True)
os.makedirs(processed_data_path, exist_ok=True)

def fetch_and_save():
    # fetches the dataset and saves it as a csv file 

    print('Fetching dataset...')

    # load dataset from Hugging Face
    dataset = load_dataset(dataset_name)

     # convert to Pandas DataFrame
    df = pd.DataFrame(dataset["train"])

    # store the data as a csv file
    raw_file_path = os.path.join(raw_data_path, "chordonomicon.csv")
    df.to_csv(raw_file_path, index=False) 

    print(f'Dataset fetched and stored at {raw_data_path}')

if __name__ == "__main__":
    fetch_and_save()