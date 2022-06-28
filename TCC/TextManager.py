import nltk
import string

from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

stopwords = set(stopwords.words('portuguese') + list(punctuation))

class NTools():
#TOOLS
    def tokenizer_txt(txt):
        tokens = nltk.word_tokenize(txt)
        return tokens

    def tokenizer_sent(txt):
        tokens = nltk.sent_tokenize(txt)
        return tokens

    def clean_stop(tk):
        cleaned_text = [w for w in tk if w not in stopwords]
        return cleaned_text

    def get_frequency(tk):
        frequencia = dict(nltk.FreqDist(tk))
        return frequencia

#COMMANDS
    def set_frequency(tk):
        frequency = NTools.get_frequency(tk)
        max_frequency = max(frequency.values())
        for w in frequency.keys():
            frequency[w] = (frequency[w]/max_frequency)
        return frequency

    def get_cleantoken(txt):
        tokens = NTools.clean_stop(NTools.tokenizer_txt(txt))
        return tokens

    def get_scoresent(sent, freq):
        sentences_scr = {}
        for s in sent:
            for w in NTools.tokenizer_txt(s.lower()):
                if w in freq.keys():
                    if s not in sentences_scr.keys():
                        sentences_scr[s] = freq[w]
                    else:
                        sentences_scr[s] += freq[w]
        return sentences_scr
