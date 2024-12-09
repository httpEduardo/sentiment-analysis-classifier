# main.py
from model import SentimentModel
from utils import clean_text

def main():
    # Carrega o modelo
    sentiment_model = SentimentModel()

    # Solicita input do usuário
    user_input = input("Digite uma frase para análise de sentimento: ").strip()
    user_input = clean_text(user_input)

    # Realiza a predição
    prediction = sentiment_model.predict(user_input)
    print(f"O sentimento da frase é: {prediction}")

if __name__ == "__main__":
    main()
