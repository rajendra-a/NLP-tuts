import nltk
from nltk import PorterStemmer
from nltk.corpus import stopwords

#corpora
paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""

# splitting the paragraph into list of sentences 
sentences = nltk.sent_tokenize(paragraph)
# creating the instance of the classs PorterStemmer
stemmer = PorterStemmer()

#stemming
for i in range(len(sentences)):
    # split the sentnce into list of words of every sentence
    words = nltk.word_tokenize(sentences[i])
    # if the words of sentence not in stopwords then stem the word and return the list of the words
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    # format the the stemmed words into sentence of string
    sentences[i] = ' '.join(words)
print(sentences)

# disavantage of stemming is produce intermediate representation of the word may not have any meaning
# eg: intelligen, fina etc 