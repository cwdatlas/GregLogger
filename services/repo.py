import os
import sys

import pandas as pd

from models.MachineLog import MachineLog


class Repo:
    def __init__(self):
        # gathering data from the csv file
        modpath = os.path.dirname(os.path.abspath(sys.prefix))
        self.file_path = modpath + r"/services/machine_logs.csv"
        self.repo = pd.read_csv(self.file_path, skipinitialspace=True)

        # Fix the DataFrame (I did copy this section from chatGPT. I was having some ISSUES
        self.repo.columns = [col if not pd.isna(col) else 'YourNewColumnName' for col in self.repo.columns]
        self.repo = self.repo.loc[:, ~self.repo.columns.str.contains('^Unnamed')]

    def get_all(self):
        json_logs = self.repo.to_dict(orient='records')
        return json_logs

    def set_log(self, log: MachineLog):
        length = len(self.repo)
        self.repo.loc[len(self.repo)] = log.model_dump()
        self.repo.to_csv(self.file_path, mode='w')
        return length < len(self.repo)

    # As logs aren't usually deleted, and this function is for non-log data I am not deleting it for future use
    def delete_log(self, log_index):
        length = len(self.repo)
        self.repo.drop(log_index, inplace=True)
        self.repo.to_csv(self.file_path, mode='w')
        return length > len(self.repo)

    def get_log_list(self):
        return self.repo.values.tolist()
