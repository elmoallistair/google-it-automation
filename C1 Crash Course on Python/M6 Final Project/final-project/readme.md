# Final Project Help

## Project goal 
Create a dictionary with words and word frequencies that can be passed to the generate_from_frequencies function of the WordCloud class.

Once you have the dictionary, use this code to generate the word cloud image:

```
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")
```

## Things to remember 
* Before processing any text, you need to remove all the punctuation marks. To do this, you can go through each line of text, character-by-character, using the **isalpha()** method. This will check whether or not the character is a letter.
* To split a line of text into words, you can use the **split()** method.
* Before storing words in the frequency dictionary, check if they’re part of the "uninteresting" set of words (for example: "a", "the", "to", "if"). Make this set a parameter to your function so that you can change it if necessary.

## Input file
For the input file, you need to provide a file that contains text only. For the text itself, you can copy and paste the contents of a website you like. Or you can use a site like [Project Gutenberg](https://www.gutenberg.org/) to find books that are available online. You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen.

## Jupyter Notebooks Help
Remember that if you need help with Jupyter Notebooks, you can check out [this help page.](https://learner.coursera.help/hc/en-us/articles/360004995312-Solve-problems-with-Jupyter-Notebooks)