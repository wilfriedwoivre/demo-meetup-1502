# Azure Container Instances Word Count Sample

This repo shows an example of a containerized task that could be run in Azure Container Instances.

## Usage

By default, the container runs a Python script that counts the words in the text of Hamlet and writes the 10 most common words to STDOUT.

### Environment variables

You can configure the following through environment variables:

**NumWords**: The number of words to be emitted.

**MinLength**: The minimum length required for a word to be counted. Choose a higher number to avoid common words like 'a' and 'the'.

### Command line override

To count the words of a different text, you can override the command line for the container. For example, to count the words of Romeo and Juliet instead of Hamlet:

```
wordcount.py http://shakespeare.mit.edu/romeo_juliet/full.html
```