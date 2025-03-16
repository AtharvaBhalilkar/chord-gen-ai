import gdown
import os

file_id = "1QpwFwGbm8xAdTpMfxnBEzFNnoFougW0g"
raw_data_path= "data/raw"
processed_data_path = "data/processed"
output_file = os.path.join(raw_data_path, "chordonomicon.csv")

os.makedirs(raw_data_path, exist_ok=True)
os.makedirs(processed_data_path, exist_ok=True)

def fetch_and_save():

    # download dataset from Google Drive using gdown.

    print('Fetching dataset...')

    # google drive url that contains the dataset
    url = 'https://drive.google.com/uc?id=1QpwFwGbm8xAdTpMfxnBEzFNnoFougW0g'

    # download using gdown with fuzzy option
    gdown.download(url, output_file, quiet=False, fuzzy=True)

    print(f'Dataset fetched and stored at {output_file}')

if __name__ == "__main__":
    fetch_and_save()