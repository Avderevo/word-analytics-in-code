from nltk import pos_tag
import nltk

nltk.download('averaged_perceptron_tagger')


'''************nltk_word_extract***************'''


def is_noun(list_words):
    noun_tag = ['NNS', 'NN']
    list_noun = []
    for word in list_words:
        word = pos_tag([word])
        if word[0][1] in noun_tag:
            list_noun.append(word[0][0])
    return list_noun


def is_verb(list_words):
    verb_tag = ['VB', 'VBR']
    list_vb = []
    for word in list_words:
        word = pos_tag([word])
        if word[0][1] in verb_tag:
            list_vb.append(word[0][0])
    return list_vb
