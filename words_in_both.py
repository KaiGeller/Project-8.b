#Kai Geller
#GitHub Username: KaiGeller
#5/17/2022
#This code will find the words that are present in both strings
def words_in_both(sentence,sentence_2):
    """This will return the common words that are in both sentences"""
    sentence = sentence.lower()
    sentence_2 = sentence_2.lower()
    words = sentence.split()
    words_2 = sentence_2.split()
    common_words= set()
    for word in words:
        if word in words_2:
            common_words.add(word)
    return common_words