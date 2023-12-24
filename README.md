# Lany Songs Text Generation and Sentiment Analysis
This repository contains Jupyter Notebooks for text generation, next word prediction using a deep learning model, and sentiment analysis for lyrics from Lany songs.
### Markov.ipynb - Markov Chain-based Text Generator
This notebook implements a text generator using a Markov Chain model. The Markov Chain algorithm is employed to predict the next word in a sequence based on the current word. This simple yet effective method can be used to generate coherent and contextually relevant text.

### Next_Word_Prediction.ipynb - LSTM-based Next Word Prediction
In this notebook, a deep learning model is constructed for predicting the next word in a sequence of lyrics. The model is built using a Sequential architecture with an Embedding layer, LSTM layer, and a Dense layer with softmax activation. The model is trained using categorical cross-entropy loss and the Adam optimizer. This approach leverages the power of recurrent neural networks for more context-aware predictions.

### Sentiment.ipynb - Sentiment Analysis and EDA
This notebook focuses on analyzing the sentiment of each song's lyrics and performing feature engineering to extract meaningful insights. Sentiment scores are computed for each song. Various features are engineered to enhance the understanding of the lyrical content including: # of words, num of lines, average Word Length Per Line, num of uniq_words, lexical_density, views per album
     
