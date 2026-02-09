# NLP_2026_ex1

## Dependencies

The code requires the following Python libraries:

| Library | Purpose |
|---------|---------|
| `re` | Regular expressions for text cleaning |
| `requests` | Downloading the lyrics from GitHub |
| `pandas` | For data manipulation |
| `matplotlib` | For plotting results |
| `seaborn` | For visualizations |
| `math` | Provides mathematical functions like `log` |
| `collections.Counter` | Counting tokens or entities |
| `spacy` | NLP processing and loading the language models |


### Additional Required Resources

1. **Lyrics Text Files**

The lyrics are loaded dynamically from:
- **Welsh lyrics**: https://raw.githubusercontent.com/bethancunningham/nlp_2026/refs/heads/main/welsh_lyrics_adwaith_large.txt
- **English lyrics**: https://raw.githubusercontent.com/bethancunningham/nlp_2026/refs/heads/main/english_lyrics_ldp_large.txt

2. **spaCy Language Models**

- **Welsh model**: `cy_techiaith_tag_lem_ner_lg`
    - Instructions for downloading Welsh package (scroll down for English): https://github.com/techiaith/spacy_cy_tag_lem_ner_lg
- **English model**: `en_core_web_sm`
