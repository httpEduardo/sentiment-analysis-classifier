# Sentiment Analysis Classifier

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)

A compact text-classification example that trains a logistic regression model to label short messages as positive or negative. The sample dataset is stored in `data/`.

## Train and classify

Install the dependencies, train the model, and then classify a sentence from the terminal:

```bash
pip install -r requirements.txt
python train_model.py
python main.py
```

Training saves the model and vectorizer in the project root for the inference script to load.
