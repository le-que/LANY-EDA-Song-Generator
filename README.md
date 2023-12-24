# Lany Songs Text Generation and Sentiment Analysis
This repository contains Jupyter Notebooks for text generation, next word prediction using a deep learning model, and sentiment analysis for lyrics from Lany songs.
### Markov.ipynb - Markov Chain-based Text Generator
This notebook implements a text generator using a Markov Chain model. It utilizes a probabilistic model to predict the next word in a sequence based on the previous words.

### Next_Word_Prediction.ipynb - LSTM-based Next Word Prediction
This notebook employs a sequential model for next word prediction using deep learning. The model architecture includes an Embedding layer, an LSTM layer, and a Dense layer with softmax activation. It is trained on a dataset created from Lany song lyrics.

### Sentiment.ipynb - Sentiment Analysis and EDA
This notebook focuses on analyzing the sentiment of each song's lyrics and performing feature engineering to extract meaningful insights. Sentiment scores are computed for each song. Various features are engineered to enhance the understanding of the lyrical content including: # of words, num of lines, average Word Length Per Line, num of uniq_words, lexical_density, views per album

### Genius.py
This was used to collect Lany song data and create/update lyrics.csv. it can be used on any lyrics page on genius.com and takes in the lyrics website, and the album website.
     
