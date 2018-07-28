import ast
import os

from helper import *


'''************************ast_maker**********************'''


def get_filenames_list(path):

    filenames = []

    for dirname, dirs, files in os.walk(path, topdown=False):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
    print('total %s files' % len(filenames))
    return filenames


def get_trees(path, with_filenames=False, with_file_content=False):
    trees = []
    filenames_list = get_filenames_list(path)

    for filename in filenames_list:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
        if with_filenames:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)
    print('trees generated')
    return trees


'''************************trees_parser**********************'''


def get_list_all_function_names(trees):
    func_str = 'function names'
    list_all_function_names = []
    for tree in trees:
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                list_all_function_names.append(node.name.lower())
    list_all_function_names = cuts_off_special_names(list_all_function_names)
    return get_all_words_in_listnames(list_all_function_names), func_str


def get_list_all_variables_names(trees):
    var_str = 'variables names'
    list_all_variables_names = []
    for tree in trees:
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                list_all_variables_names.append(node.id.lower())
    list_all_variables_names = cuts_off_special_names(list_all_variables_names)
    return get_all_words_in_listnames(list_all_variables_names), var_str


def get_list_all_classes_names(trees):
    class_str = 'classes names'
    list_all_classes_names = []
    for tree in trees:
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                list_all_classes_names.append(node.name.lower())
    list_all_classes_names = cuts_off_special_names(list_all_classes_names)
    return get_all_words_in_listnames(list_all_classes_names), class_str

