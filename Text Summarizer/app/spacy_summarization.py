# NLP Pkgs
import spacy 
# Pkgs for Normalizing Text
from spacy.lang.en.stop_words import STOP_WORDS
# Import Heapq for Finding the Top N Sentences
from heapq import nlargest


nlp = spacy.load('en_core_web_sm')

def text_summarizer(raw_docx):
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Build Word Frequency # word.text is tokenization in spacy
    word_frequencies = {}
    for word in docx:  
        if word.text not in stopwords:
            if word.text in word_frequencies:
                word_frequencies[word.text] += 1
            else:
                word_frequencies[word.text] = 1
    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies:  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]

    # Sentence Scores
    sentence_scores = {}
    for sent in sentence_list:  
        for word in sent:
            if (
                word.text.lower() in word_frequencies
                and len(sent.text.split(' ')) < 30
            ):
                if sent in sentence_scores:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]


                else:
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    return ' '.join(final_sentences)
    