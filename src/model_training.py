import joblib
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
from src.logger import get_logger
from src.custom_exception import CustomException
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

logger = get_logger(__name__)
class ModelTrainer:
    def __init__(self, processed_data_path="artifacts/processed"):
        self.processed_data_path = processed_data_path
        self.model_path = "artifacts/model"             
        os.makedirs(self.model_path, exist_ok=True)
        self.model = DecisionTreeClassifier(criterion="gini",max_depth=30,random_state=42)

    def load_data(self):
        try:
            logger.info("Loading processed data")
            X_train = joblib.load(os.path.join(self.processed_data_path, 'X_train.pkl'))
            X_test = joblib.load(os.path.join(self.processed_data_path, 'X_test.pkl'))
            Y_train = joblib.load(os.path.join(self.processed_data_path, 'Y_train.pkl'))
            Y_test = joblib.load(os.path.join(self.processed_data_path, 'Y_test.pkl'))
            logger.info("Data loaded successfully")
            return X_train, X_test, Y_train, Y_test
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise CustomException(f"Error loading data: {e}")

    def train_model(self, X_train, Y_train):
        try:
            logger.info("Training the model")
            self.model.fit(X_train, Y_train)
            joblib.dump(self.model, os.path.join(self.model_path, 'model.pkl'))
            logger.info("Model trained successfully")
        except Exception as e:
            logger.error(f"Error training model: {e}")
            raise CustomException(f"Error training model: {e}")
    def evaluate_model(self, X_test, Y_test):
        try:
            logger.info("Evaluating the model")
            Y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(Y_test, Y_pred)
            precision = precision_score(Y_test, Y_pred, average='weighted')
            recall = recall_score(Y_test, Y_pred, average='weighted')
            f1 = f1_score(Y_test, Y_pred, average='weighted')
            cm = confusion_matrix(Y_test, Y_pred)
            logger.info(f"Model evaluation metrics: Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1 Score: {f1}")
            plt.figure(figsize=(10, 7))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(Y_test), yticklabels=np.unique(Y_test))
            plt.title('Confusion Matrix')
            plt.xlabel('Predicted')
            plt.ylabel('Actual')
            plt.savefig(os.path.join(self.model_path, 'confusion_matrix.png'))
            plt.close()
            logger.info("Confusion matrix saved successfully")
            return accuracy, precision, recall, f1
        except Exception as e:
            logger.error(f"Error evaluating model: {e}")
            raise CustomException(f"Error evaluating model: {e}")
    def run(self):
        try:
            X_train, X_test, Y_train, Y_test = self.load_data()
            self.train_model(X_train, Y_train)
            accuracy, precision, recall, f1 = self.evaluate_model(X_test, Y_test)
            logger.info(f"Model training and evaluation completed with Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1 Score: {f1}")
        except Exception as e:
            logger.error(f"Error in model training process: {e}")
            raise CustomException(f"Error in model training process: {e}")
if __name__ == "__main__":
    model_trainer = ModelTrainer()
    model_trainer.run()
    