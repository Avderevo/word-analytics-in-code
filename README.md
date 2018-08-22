<h1>Analysis and statistics of words in the code</h1>

<p><b>Written on the python version 3.5.2 in OS ubuntu 16.4</b></p>

<p>The script creates a directory and clones the repository from the githab.
 Then creates Abstract Syntax Trees of all python files from the repository.</p>

<p>The ast module extracts function names, class names, variable names. Breaks them into separate words and cuts off names with   double underscore.</p>
 
<p>Generates statistics of the most frequently used:</p>

<ul>
  <li>function names</li>
  <li>class names</li>
  <li>variable names</li>
</ul>


<p>Module NLTC analyzes the most frequent verbs and nounes in names.</p>


<h4>Install modules:</h4>

```
$ pip install --upgrade -r requirements.txt
```

<h4>Run main.py with an argument in the form of a link to the repository</h4>

```
$ python3 main.py https://github.com/Avderevo/word-statistic
```
