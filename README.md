# IRC Quote Dataset

Unoffficial of cleaned IRC quotes from [bash.org](http://bash.org)

All rights belong to bash.org.

The numbers missing from the sequence correspond to the quotes that are either
still pending review or have been rejected. However, my dataset is by no means
considered to be proven complete.

Quotes were extracted one at a time by iterating through all quotes using a
modified version of this script. The header and footer of the website were
removed with GNU `sed` commands.

## Project Ideas:
- Fine-Tune GPT model to make funny IRC quotes
- Build a bot that forecasts the bash.org score of an IRC quote
- Compile into a stringfile for GNU fortune

Pull requests for generating pandas DataFrames or exploratory data analysis are
welcome, however the final output files shouldn't be saved here.


