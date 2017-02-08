
def words(text):
 
    # removing tabs and newlines
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    words = text.split(" ") #separating into an array of words

    # converting digits to ints`
    for i, word in enumerate(words):
        if word.isdigit():
            words[i] = int(word)
        

    results = {}
    for word in words:
        if word in results:
            results[word] += 1
        else:
            if word:
                results[word] = 1

    return results


