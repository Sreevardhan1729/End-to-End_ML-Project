from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAMe = "Data Ingestion stage"
try:
    logger.info(f">>> stage {STAGE_NAMe} started< <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAMe} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAMe = "Data Validataion stage"
try:
    logger.info(f">>> stage {STAGE_NAMe} started< <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>> stage {STAGE_NAMe} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAMe = "Data Transformation stage"
try:
    logger.info(f">>> stage {STAGE_NAMe} started< <<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>> stage {STAGE_NAMe} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAMe = "Model Trainer stage"
try:
    logger.info(f">>> stage {STAGE_NAMe} started< <<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>> stage {STAGE_NAMe} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAMe = "Model Evaluation stage"
try:
    logger.info(f">>> stage {STAGE_NAMe} started< <<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>> stage {STAGE_NAMe} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e