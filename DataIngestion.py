import pandas as pd

class DataIngestion:
    def __init__(self, file_path, sheet_name=None):
        self.file_path = file_path
        self.sheet_name = sheet_name

    def load_data(self, sheet_name=None):
        try:
            if self.sheet_name:
                data = pd.read_excel(self.file_path, sheet_name=self.sheet_name, index_col=0)
            else:
                data = pd.read_excel(self.file_path, index_col=0)
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            return None
        