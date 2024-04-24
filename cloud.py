file_path = '/app/paragraphs.txt'
with open(file_path,"r")as file:
    file_contents=file.read()

file_contents

import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
nltk.download('punkt')

tokens= word_tokenize(file_contents)
tokens

stop_words=set(stopwords.words('english'))
stop_words


filtered_dataset = [word for word in tokens if word.lower() not in stop_words]
filtered_text=" ".join(filtered_dataset)
filtered_text

words_count_before=len(tokens)
words_count_after=len(filtered_dataset)
stopwords_count= (words_count_before)-(words_count_after)
print('the total number of the stop words that have been removed from the text',stopwords_count)


from collections import Counter 
word_frequency = Counter(filtered_dataset)
for word , freq in word_frequency.items():
    print(f"{word}:{freq}")

    







