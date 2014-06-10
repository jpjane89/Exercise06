from sys import argv

def read_file():
    filename = argv[1]
    my_file = open(filename)
    text = my_file.read()
    my_file.close()

    text = text.replace("\n"," ")
    words = text.split(" ") 

    return words

def clean_words(words):

    clean_words = []

    for word in words:

        clean_word = word.strip('"')
        clean_word = clean_word.strip("!:;,.#&/'()*+-?_'\t'")
        clean_word = clean_word.strip('"')

        clean_words.append(clean_word)

    return clean_words

def fill_dict(words):

    word_dict = {}

    for word in words:
        word = word.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict.setdefault(word,1)

    return word_dict

def sort_dict(word_dict):

    dict_as_tuples = word_dict.items()

    sorted_alpha = sorted(dict_as_tuples, key=lambda word : word[0])

    sorted_tuples = sorted(sorted_alpha, key=lambda word : word[1], reverse=True)

    for word, count in sorted_tuples:
        print word, count

def main():
    
    words = clean_words(read_file())

    word_dict = fill_dict(words)

    sort_dict(word_dict)

    #for word in word_dict:
        #print word, word_dict.get(word)

if __name__ == "__main__":
    main()
