
import stemming
from nltk.corpus import stopwords
from stemming.porter2 import stem
import string
import re

# review from RottenTomatoes.com
text = """Some of the sequences are undeniably thrilling but, at about 2-1/2 hours, 
overkill sets in early. Diehard Marvel fans will no doubt lap all this stuff up – 
at the packed screening I attended, even the tiniest Marvel minutiae was greeted with whoops – 
but I was longing for the showdown with Thanos to bring an end to it all. 
And of course, there is no end. That's why they call it "Infinity War." 
Grade: B- (Rated PG-13 for intense sequences of sci-fi violence and action throughout, 
language, and some crude references.)."""

print ("Original:")
print (text)
print ()

# lower case all words
text = text.lower()
print ("Lower Case:")
print (text)
print ()

# remove all punctuation
regex = re.compile('[%s]' % re.escape(string.punctuation))
text = regex.sub('', text)
print ("No Punctuation:")
print (">>>> ", string.punctuation)
print (text)
print ()

# remove all digits
regex = re.compile('[%s]' % re.escape(string.digits))
text = regex.sub('', text)
print ("No Digits:")
print (">>>> ", string.digits)
print (text)
print ()

# only retain words >= 4 characters long
text = ' '.join([word for word in text.split() if (len(word)>=4)])
print ("Only Words >= 4 Chars Long:")
print (text)
print ()

# remove stop words
sw = stopwords.words("english")
text = ' '.join([word for word in text.split() if word not in sw])
print ("No Stop Words:")
print (sw)
print (text)
print ()

# convert to stem words
text = ' '.join([stem(word) for word in text.split()])
print ("Stem Words:")
print (text)
print ()

# only retain unique words
text = ' '.join(set(text.split()))
print ("Unique Words:")
print (text)
print ()



