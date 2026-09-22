from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__ == "__main__":

    # Data Ingestion
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()

    # Data Transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = (
        data_transformation.initiate_data_transformation(
            train_data,
            test_data
        )
    )

    # Model Training
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(
        train_arr,
        test_arr
    )