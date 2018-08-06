from downloader import clone_repo_to_folder
from ast_maker import get_trees
from word_anlitics import is_noun, is_verb
from helper import dict_uniq_words
from trees_parser import get_list_all_variables_names, get_list_all_function_names, get_list_all_classes_names

import sys
import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def get_trees_analytics(funk, trees, top_size=10):
    list_words = funk(trees)
    list_verbs = is_verb(list_words[0])
    list_noun = is_noun(list_words[0])
    f = '-' * 3
    logging.info(f + list_words[1].upper() + f)
    logging.info('\n All {} {} {}' .format(list_words[1], f, len(list_words[0])))
    logging.info('Unique {} {} {}' .format (list_words[1], f, len(set(list_words[0]))))
    logging.info('Ten most often {} {} \n {}' .format(list_words[1], f, dict_uniq_words(list_words[0])))
    logging.info('Unique verbs {} {}' .format(f, len(set(list_verbs))))
    logging.info('Most often verbs {} \n {}' .format(f, dict_uniq_words(list_verbs)))
    logging.info('Unique noun {} {}' .format(f, len(set(list_noun))))
    logging.info('Most often noun {} \n {} \n\n' .format(f, dict_uniq_words(list_noun)))


def main(url):
    func_names = [get_list_all_variables_names, get_list_all_function_names, get_list_all_classes_names]
    path = clone_repo_to_folder(url)
    trees = get_trees(path)
    for func in func_names:
        get_trees_analytics(func, trees)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        GIT_URL = sys.argv[1]
    else:
        GIT_URL = 'https://github.com/Avderevo/word-statistic'
    main(GIT_URL)
