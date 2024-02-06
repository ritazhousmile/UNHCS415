# this is the string lab assignment

def rephrase_sentence(text):
    # text = "this is a sentence"

    space = text.index(" ")
    first_word = text[0:space]
   # print(first_word)
    last_word_index = text.rindex(" ")
    #print("last word length:",last_word_index)
    last_word = text[last_word_index+1:]
    #print("last word:", last_word)

    mid_sentence = text[space+1:last_word_index]
    #print("mid sentence:", mid_sentence)

    return last_word+" " + mid_sentence + " " + first_word


print('Enter a line of text. No punctuation needed')
sentence = input()

new_sentence = rephrase_sentence(sentence)
print(f"I have rephrased that line to read:\n{new_sentence}")



