from sys import argv

def read_file():
    filename = argv[1]
    my_file = open(filename)
    text = my_file.read()
    my_file.close()

    text = text.replace("\n"," ")
    words = text.split(" ") 

    new_words = []

    for word in words:

        new_word = word.strip('"')
        new_word = new_word.strip("!:;,.#&/'()*+-?_'\t'")
        new_word = new_word.strip('"')

        new_words.append(new_word)

    return new_words

def fill_dict(words):

    word_dict = {}

    for word in words:
        word = word.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict.setdefault(word,1)

    return word_dict

def main():
    
    words = read_file()

    word_dict = fill_dict(words)

    for word in word_dict:
        print word, word_dict.get(word)

if __name__ == "__main__":
    main()
