# train_model.py
import os
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from utils import clean_text

def load_data(positive_path: str = "data/positive.txt", negative_path: str = "data/negative.txt"):
    """
    Carrega os dados positivos e negativos de arquivos texto.
    Retorna listas de textos e suas respectivas labels (1 para positivo, 0 para negativo).
    """
    texts = []
    labels = []

    # Carrega positivos
    if os.path.exists(positive_path):
        with open(positive_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    texts.append(line)
                    labels.append(1)

    # Carrega negativos
    if os.path.exists(negative_path):
        with open(negative_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    texts.append(line)
                    labels.append(0)

    return texts, labels

def train_model():
    texts, labels = load_data()
    texts = [clean_text(t) for t in texts]

    # Cria o vetorizador e transforma os dados
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)

    # Treina um modelo simples de regressão logística
    model = LogisticRegression()
    model.fit(X, labels)

    # Salva o modelo e o vetorizador
    joblib.dump(model, "model.joblib")
    joblib.dump(vectorizer, "vectorizer.joblib")
    print("Modelo treinado e salvo com sucesso!")

if __name__ == "__main__":
    train_model()
