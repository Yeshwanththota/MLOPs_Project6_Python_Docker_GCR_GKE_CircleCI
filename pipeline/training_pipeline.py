
from src.data_processing import DataProcessor
from src.model_training import ModelTrainer

if __name__ == "__main__":
    processor = DataProcessor(file_path='artifacts/raw/data.csv')
    processor.run()

    model_trainer = ModelTrainer()
    model_trainer.run()