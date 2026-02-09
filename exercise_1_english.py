# preparations
import re
import spacy
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import log
from collections import Counter

# reading in the lyrics
url_english = "https://raw.githubusercontent.com/bethancunningham/nlp_2026/main/english_lyrics_ldp_large.txt"
request_2 = requests.get(url_english)
lyrics_english = request_2.text

# cleaning - making text lowercase and removing text in square brackets ([Chorus], [Verse])
cleaned_text = re.sub(r"\[.*?\]", "", lyrics_english)
cleaned_text = cleaned_text.lower()

# loading in the language model in spacy and creating a doc object
nlp = spacy.load("en_core_web_sm")
doc = nlp(cleaned_text)

# tokenising and removing punctuation, white spaces and stop words
words = [token.text
         for token in doc
         if not token.is_punct and not token.is_space and not token == "\u2005" and not token.is_stop]

print("Stop words in English:")
print(sorted(nlp.Defaults.stop_words))

# making dataframe for ranked log word frequencies
df = pd.DataFrame.from_records(list(dict(Counter(words)).items()), columns=['word','frequency'])
df = df.sort_values(by=['frequency'], ascending=False)
df['rank'] = list(range(1, len(df) + 1))
df['logfreq'] = [log(x+1) for x in df['frequency']]
print(df)

# plotting data (log frequency against rank)
sns.relplot(x="rank", y="logfreq", data=df);
plt.show()
plt.close()
