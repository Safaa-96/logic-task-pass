def remove_char(word, ch):
    new_word = ""
    count=0
    for w in word:
        if (w == ch):
           count=count+1

    return count


print(remove_char('safae sameer', 'e'))