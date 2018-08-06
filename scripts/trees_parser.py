import ast
from helper import get_all_words_in_listnames, cuts_off_special_names


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

