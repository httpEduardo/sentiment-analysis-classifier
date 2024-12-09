# model.py
import joblib

class SentimentModel:
    """
    Classe que carrega o modelo e o vetorizador treinados.
    """
    def __init__(self, model_path: str = "model.joblib", vectorizer_path: str = "vectorizer.joblib"):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict(self, text: str) -> str:
        """
        Realiza a predição do sentimento.
        Retorna 'Positivo' ou 'Negativo'.
        """
        X = self.vectorizer.transform([text])
        pred = self.model.predict(X)
        return "Positivo" if pred[0] == 1 else "Negativo"
