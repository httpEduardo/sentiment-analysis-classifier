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
pip install -r requirements.txt



Thought about projeto em IA com Python por 11 segundos
Abaixo segue um exemplo completo de um projeto Python relacionado a IA (Aprendizado de Máquina) para análise de sentimento de textos curtos. O projeto é dividido em múltiplos arquivos, incluindo um README com explicações, um arquivo main.py para a execução principal, um arquivo train_model.py para treinar o modelo, um model.py para carregar o modelo treinado, um utils.py com funções auxiliares, e um requirements.txt listando as dependências. Também é incluída uma pasta data/ contendo dados de treino simples.

Este exemplo simula um cenário real: você terá um conjunto de dados simples de texto positivo e negativo, treinará um classificador usando scikit-learn e depois utilizará o modelo para classificar o sentimento de uma frase inserida pelo usuário no main.py.

Estrutura do Projeto
css
Copiar código
project/
  ├─ README.md
  ├─ requirements.txt
  ├─ main.py
  ├─ train_model.py
  ├─ model.py
  ├─ utils.py
  └─ data/
       ├─ positive.txt
       └─ negative.txt
Conteúdo do README.md
markdown
Copiar código
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
pip install -r requirements.txt

Uso

Treine o modelo:

python train_model.py

Execute a classificação:

python main.py

Insira uma frase quando solicitado e veja o resultado da análise de sentimento.

Estrutura do Código
data/: Contém os dados de treino (ex: positive.txt e negative.txt).
train_model.py: Responsável por treinar o modelo e salvar o artefato.
model.py: Carrega o modelo e o vetorizador salvos.
utils.py: Funções auxiliares para limpeza e pré-processamento.
main.py: Interface simples de linha de comando para classificar frases inseridas pelo usuário.


---

### Conteúdo do requirements.txt

```txt
scikit-learn==1.3.0
joblib==1.3.2
