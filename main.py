# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    f = open(filename, "r")
    return f.read()


def count_words():
    text = read_file_content('Reading-Text-Files/story.txt')
    words = (text.split())
    unique_words = set(words)
    theWords = {}
    for word in unique_words:
        theWords.update({word: words.count(word)})
    return theWords

text = read_file_content('Reading-Text-Files/story.txt')

print(text)

print("-----------")
print("-----------")

count = count_words()
print (count)