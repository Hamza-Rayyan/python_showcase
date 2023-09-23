

def emojis_converter(an_input):

    words = an_input.split(' ')
    emojis ={
        ":)" : "😊",
        ":()":"🤔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emojis_converter(an_input=input()))


