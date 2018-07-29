<h2>Analysis and statistics of words in the code</h2>

<h4>Written on the python version 3.5.2 in OS ubuntu 16.4</h4>

The script creates a directory and clones the repository from the githab.
Then creates <b>Abstract Syntax Trees</b> of all python files from the repository.

The ast module extracts function names, class names, variable names. Breaks them into separate words and cuts off names with double underscore.
 
Generates statistics of the most frequently used words in names.

Module <b>NLTC</b> analyzes the most frequent verbs and nouns in names.

Statistics are output to the terminal

<h3>Running</h3>

<b>Install modules:</b>

$ pip3 install requirements.txt

<b>Run main.py with an argument in the form of a link to the repository</b>

$ python3 main.py https://github.com/Avderevo/word-statistic


<h3>Example statistics:</h3>


---------------VARIABLES NAMES---------------

All variables names --------------- 419

Unique variables names --------------- 74

Ten most often variables names --------------- [('list', 55), ('words', 26), ('names', 26), ('all', 21), ('word', 14), ('trees', 13), ('print', 12), ('name', 11), ('tree', 11), ('folder', 10)]

Unique verbs --------------- 1

Most often verbs --------------- 
 [('get', 9)]
 
Unique noun --------------- 63

Most often noun --------------- [('list', 55), ('words', 26), ('names', 26), ('word', 14), ('trees', 13), ('print', 12), ('name', 11), ('tree', 11), ('folder', 10), ('f', 10)


 


---------------FUNCTION NAMES---------------

 All function names --------------- 48
 
Unique function names --------------- 28

Ten most often function names --------------- [('get', 7), ('list', 4), ('all', 4), ('names', 4), ('trees', 2), ('folder', 2), ('words', 2), ('repo', 2), ('is', 2), ('verb', 1)]

Unique verbs --------------- 1

Most often verbs --------------- [('get', 7)]

Unique noun --------------- 19

Most often noun --------------- [('list', 4), ('names', 4), ('trees', 2), ('folder', 2), ('words', 2), ('repo', 2), ('variables', 1), ('classes', 1), ('clone', 1), ('dict', 1)]



---------------CLASSES NAMES---------------

 All classes names --------------- 0
 
Unique classes names --------------- 0

Ten most often classes names --------------- []

Unique verbs --------------- 0

Most often verbs --------------- []

Unique noun --------------- 0

Most often noun --------------- []



