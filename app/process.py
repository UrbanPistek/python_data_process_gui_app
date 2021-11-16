import pandas as pd

class Process:
    def __init__(self):
        pass

    def set_data(self, data_path):
        self.df = pd.read_csv(data_path)
        print(self.df)