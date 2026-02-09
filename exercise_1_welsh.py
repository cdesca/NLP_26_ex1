import re
import spacy
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import log
from collections import Counter

#loading in the lyrics
url_welsh = "https://raw.githubusercontent.com/bethancunningham/nlp_2026/main/welsh_lyrics_adwaith_large.txt"
request_1 = requests.get(url_welsh)
lyrics_welsh = request_1.text

#initial text cleaning - removing new lines and making lowercase
text_string = " ".join(lyrics_welsh.splitlines())
text_string = text_string.lower() 

#removing text in square brackets (e.g. [Chorus])
cleaned_text = re.sub(r"\[.*?\]", "", text_string)

#loading in the language model and creating a doc object
nlp = spacy.load("cy_techiaith_tag_lem_ner_lg")
doc = nlp(cleaned_text)

#tokenization - creating a list of words, excluding punctuation and spaces; optional exclusion of stop words
words = [token.text
         for token in doc
         #excludes stop words and punctuation
         if not token.is_punct and not token.is_space]
         #and not token.is_stop]

#printing the stop words 
print("Stop words in Welsh:")
print(sorted(nlp.Defaults.stop_words))

#making the dataframe for the frequency distribution of words, and plotting the log frequency against rank
df = pd.DataFrame.from_records(list(dict(Counter(words)).items()), columns=['word','frequency'])
df = df.sort_values(by=['frequency'], ascending=False)
df['rank'] = list(range(1, len(df) + 1))
df['logfreq'] = [log(x+1) for x in df['frequency']]
print(df)

#visualizing the log frequency against rank
sns.relplot(x="rank", y="logfreq", data=df);
plt.show()
plt.close()
