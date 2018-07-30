from downloader import clone_repo_to_folder
from ast_parser import *
from words_anlitics import *


def get_trees_analytics(funk, trees, top_size=10):
    list_words = funk(trees)
    list_verbs = is_verb(list_words[0])
    list_noun = is_noun(list_words[0])
    f = '-' * 15
    print(f + list_words[1].upper() + f)
    print('\n All %s %s %s' % (list_words[1], f, len(list_words[0])))
    print('Unique %s %s %s' % (list_words[1], f, len(set(list_words[0]))))
    print('Ten most often %s %s \n %s' % (list_words[1], f, dict_uniq_words(list_words[0])))
    print('Unique verbs %s %s' % (f, len(set(list_verbs))))
    print('Most often verbs %s \n %s' % (f, dict_uniq_words(list_verbs)))
    print('Unique noun %s %s' % (f, len(set(list_noun))))
    print('Most often noun %s \n %s \n\n' % (f, dict_uniq_words(list_noun)))


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
