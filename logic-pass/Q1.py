def remove_char(word,ch):
    new_word=""
    for w in word :
        if(w!=ch):
          new_word +=w

    return new_word


print(remove_char('safae','e'))