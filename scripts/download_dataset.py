import kagglehub
from pathlib import Path

# Define the project root and raw data directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

#Function to download the dataset from Kaggle
def download_dataset():
    
    # Create the raw data directory if it doesn't exist
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Download Olist dataset latest version from Kaggle
    path = kagglehub.dataset_download("olistbr/brazilian-ecommerce", output_dir=str(RAW_DATA_DIR))
    print("Path to dataset files:", path)

if __name__ == "__main__":
    download_dataset()