from pathlib import Path
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception ("your data schma is not valied")
        except Exception as e:
            print(e)