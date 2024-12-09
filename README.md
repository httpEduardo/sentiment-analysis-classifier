# Análise de Sentimento de Texto usando IA

## Descrição

Este projeto utiliza técnicas de Aprendizado de Máquina (Machine Learning) para análise de sentimento em textos curtos. A aplicação treina um modelo de classificação binária (positivo ou negativo) a partir de um conjunto de dados simples, formado por textos positivos e negativos, e posteriormente utiliza o modelo treinado para inferir o sentimento de novas frases fornecidas pelo usuário.

## Como o Projeto Funciona

1. **Treinamento do Modelo:**  
   Execute o arquivo `train_model.py` para:
   - Ler o conjunto de dados contido na pasta `data/`.
   - Realizar o pré-processamento do texto.
   - Treinar um classificador (Logistic Regression).
   - Salvar o modelo treinado e o vetorizador em disco.

2. **Inferência (Classificação de Sentimento):**  
   Execute o arquivo `main.py` para:
   - Carregar o modelo e o vetorizador previamente treinados.
   - Solicitar ao usuário que insira uma frase.
   - Classificar o sentimento (positivo ou negativo) da frase inserida.

## Utilidade

Esta aplicação é útil em cenários onde seja necessário entender a percepção do usuário sobre um produto, marca ou evento. Por exemplo, pode ser integrada a um bot de atendimento ao cliente para determinar se o feedback fornecido é positivo ou negativo.

## Requisitos

- Python 3.7+
- Pip

Instale as dependências executando:
```bash

