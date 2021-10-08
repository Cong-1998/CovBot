import nltk
import re
from nltk.stem import PorterStemmer
import random
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd

def nlp(text):
    stemmer = PorterStemmer()
    nltk.download('averaged_perceptron_tagger')
    sentence = text.lower() #Convert the sentences into lowercase
    tokenizer = RegexpTokenizer(r'\w+') #Tokenize on word charcter
    tokens = tokenizer.tokenize(sentence)
    words = [w for w in tokens if not w in stopwords.words('english')]
#    print('words: ',words)
    tags = nltk.pos_tag(words)
#    print('tags: ',tags)
    extracted_features = []
    for tagged_word in tags:
        word, tag = tagged_word
        if tag=='NN' or tag == 'VBN' or tag == 'NNS' or tag == 'VB' or tag == 'VBP' or tag == 'RB' or tag == 'VBZ' or tag == 'VBG' or tag =='PRP' or tag == 'JJ':
            extracted_features.append(word)
#    print('Extracted features: ',extracted_features)
    stemmed_words = [stemmer.stem(x) for x in extracted_features]
#    print(stemmed_words)
    return stemmed_words

def word_feats(words):
    return dict([(word, True) for word in words])

def nlp_from_doc(data):
    result = []
    corpus = []
    # The responses of the chat bot
    answers = {}
    for (text,answer) in data:
        features = nlp(text)
        corpus.append(features)
        result.append((word_feats(features), text))
        answers[text] = answer
    return (result, sum(corpus,[]), answers)

def split_dataset(data, split_ratio):
    random.shuffle(data)
    data_length = len(data)
    train_split = int(data_length * split_ratio)
    return (data[:train_split]), (data[train_split:])

def train_using_naive_bayes(training_data, test_data):
    classifier = nltk.NaiveBayesClassifier.train(training_data)
    training_set_accuracy = nltk.classify.accuracy(classifier, training_data)
    return classifier, training_set_accuracy

def translate(input_sentence):
    df= pd.read_csv("covid_1.csv")
    data = df.values.tolist()
    features_data, corpus, answers = nlp_from_doc(data)
    split_ratio = 1.0
    training_data, test_data = split_dataset(features_data, split_ratio)
    classifier, training_set_accuracy = train_using_naive_bayes(training_data, test_data)
    #print(training_set_accuracy)
    category = classifier.classify(word_feats(nlp(input_sentence)))
    dist = classifier.prob_classify(word_feats(nlp(input_sentence)))
    #for label in dist.samples():
    #    print("%s: %f" % (label, dist.prob(label)))
    #print(dist.prob(category))
    if dist.prob(category)<0.035:
        return "Sorry, I dont quite understand. Could you rephrase that?"

    else:
        return answers[category]

#print ("\n Welcome to CovBot! How may I help you? \n")
#while (True):
#     question= input()
#     if question== 'quit':
#         break
#     res = translate(question)
#     print(res)
     
