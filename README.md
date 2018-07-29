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

