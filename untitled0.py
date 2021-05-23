# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hUWrxPXGCOItvfkUGkBQG6W0uPFRM4Nk
"""

import pandas as pd
import numpy as np

df = pd.read_excel('/content/dataset.xlsx')

"""#TFIDF"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

df.head()

!pip install git+https://github.com/laxmimerit/preprocess_kgptalkie.git

import codecs
from nltk.tokenize import word_tokenize
import string
def clean(data):
	stopwords = codecs.open("/content/stopwords.txt", "r", encoding='utf-8', errors='ignore').read().split('\n')
	stopword=[]
	for line in stopwords:
		data1 = line.replace('\r',"")
		stopword.append(data1)
	
	#print(stopword)
	lexicon = []
	
	#tokenization
	all_words = word_tokenize(data)

	#print(all_words)

	#Data Cleaning

	exclude = set(string.punctuation)
	for i in all_words:
		st=''.join(ch for ch in i if ch not in exclude)
		if(st!=''):
			lexicon.append(st)

	#Removing Stop words
	lexicons = []
	for word in lexicon:
		if not word in stopword:
			lexicons.append(word)
	#print(lexicons)
	lexi = ' '.join([str(elem) for elem in lexicons])
	
	return lexi

import nltk
nltk.download('punkt')

df['Reviews'] = df['Reviews'].apply(lambda x: clean(x))
df.head()

tfidf = TfidfVectorizer()
X = df['Reviews']
y = df['Sentiment']

X = tfidf.fit_transform(X)

X

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

clf1 = LinearSVC()
clf2 = LogisticRegression()
clf3 = SGDClassifier()
clf4 = SVC()
clf5 = KNeighborsClassifier()
clf6 = MLPClassifier()
clf7 = DecisionTreeClassifier()
clf8 = MultinomialNB()
clf9 = LinearRegression()
clf10 = GaussianNB()


clf1.fit(X_train, y_train)
#clf2.fit(X_train, y_train)
#clf3.fit(X_train, y_train)
#clf4.fit(X_train, y_train)
#clf5.fit(X_train, y_train)
#clf6.fit(X_train, y_train)
#clf7.fit(X_train, y_train)
#clf8.fit(X_train, y_train)
#clf9.fit(X_train, y_train)
#clf10.fit(X_train.todense(), y_train)

y_pred = clf1.predict(X_test)

print(classification_report(y_test, y_pred))
#clf2.score(y_test, y_pred)

x = 'ಕಡುಕಷ್ಟ ಕಾಲದಲ್ಲಿ ಹಿರಿಯ ಕಲಾವಿದರ ಕೈ ಹಿಡಿದ ಉಪೇಂದ್ರ; ಮನಸಾರೆ ಹರಸಿದ ಜೀವಗಳು'

x = clean(x)

print(x)

vec = tfidf.transform([x])

vec.shape

clf1.predict(vec)