import os
from mlProject import logger
from mlProject.entity.config_entity import (DataValidationCofig)
import pandas as pd

class DataValidation:

    def __init__(self, config: DataValidationCofig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()

            #TODO you can also check data type here
            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e