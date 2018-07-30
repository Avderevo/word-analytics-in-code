import collections


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def get_all_words_in_listnames(listnames):
    list_words = []
    for name in listnames:
        list_words.append(name.split('_'))
    words = [x for x in flat(list_words) if x != '']
    return words


def cuts_off_special_names(list_items):
    list_names = []
    for name in list_items:
        if not (name.startswith('__') and name.endswith('__')):
            list_names.append(name)
    return list_names


def dict_uniq_words(list_words, top_size=10):
    c = collections.Counter()
    for word in list_words:
        c[word] += 1
    dict_words = c.most_common(top_size)
    return dict_words
