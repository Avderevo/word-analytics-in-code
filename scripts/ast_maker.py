import ast
import os


def get_filenames_list(path):
    for dirname, dirs, files in os.walk(path, topdown=False):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(dirname, file)) as filenames:
                    yield filenames.read()


def get_trees(path):
    trees = []
    for filename in get_filenames_list(path):
        tree = ast.parse(filename)
        trees.append(tree)
    return trees
