from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

lemmatizer = WordNetLemmatizer()
ps=PorterStemmer()
def stem(tokens):
    t=[]
    for i in tokens:
        temp=lemmatizer.lemmatize(i)
        t.append(ps.stem(temp.lower()))
    return t
word=['abc','processing']
attribute=['processing','adding']

def compare(token,attribute):
    token=set(stem(word))
    attribute=set(stem(attribute))
    if (token & attribute):
        return (token & attribute)
print(compare(word,attribute))
