# IRC Quote Dataset

Unoffficial of cleaned IRC quotes from [bash.org](http://bash.org)

All rights belong to bash.org.

The numbers missing from the sequence correspond to the quotes that are either
still pending review or have been rejected. However, my dataset is by no means
considered to be proven complete.

Quotes were extracted one at a time by iterating through all quotes using a
modified version of this script. The header and footer of the website were
removed with GNU `sed` commands. That cleanup work is not documented here in 
this repo.

## Aggregate data into TSV

For your convenience, I have included a small Python script `parser.py` 
which aggregates the extracted snippets of rendered HTML into a single 
file of tab-separated values (TSV) with three columns:
- Quote ID: The Identifier for the quote used on the website.
- Score: Indicator of whether readers on Bash.org liked or disliked the quote
- Quote: The actual text of the quote, with new lines as `\n` symbols.
I am using tabs instead of commas since many of the quotes themselves contain 
commas.

The intended use of `parser.py` is like so:
```
find cleaned/ -name "*.txt" | xargs python3 parser.py > compiled.tsv
```

The `find` and `xargs` are needed on my machine because the argument list is too long otherwise.

## Simple Exploratory Data Analysis
What are the most common words that are at least two letters long?
```
$ find cleaned -name "*.txt" | xargs cat | egrep -o "(\w){2,}" | sort | uniq -c | sort -k1nr | head
20140 the
15016 to
13624 and
12376 you
10062 it
8610 of
8087 in
7641 my
7561 is
7501 that
```

Which IRC usernames appear in the most unique quotes? 
```
find cleaned -name "*.txt" | parallel "egrep -o '<(\w){2,}>' {} | sort | uniq" | sort | uniq -c | sort -k1nr | head
  64 <Guilty>
  52 <blazemore>
  42 <timmo>
  35 <DigDug>
  29 <mightyflo>
  27 <hypr>
  26 <kisama>
  26 <maff>
  25 <Kevyn>
  25 <McMoo>
```

What is the relationship between quote length and score look like?
[test](img/len_vs_score.png "")
_(See more in `eda.ipynb`. The IPython notebook depends on matplotlib and pandas. For your convenience I have included a Pipfile)_

## Project Ideas:
- Build a model that forecasts the bash.org score of an IRC quotes.
- Compile into a stringfile for GNU fortune

Pull requests for generating pandas DataFrames or exploratory data analysis are
welcome, however the final output files shouldn't be saved here.


