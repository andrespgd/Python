mydict = {
    'hello' : 'hola',
    'house' : 'casa',
}

def replace_all(text, mydict):
    for english, spanish in mydict.items():
        text = text.replace(english, spanish)
    return text

with open('text_replace_dictionary_output.txt', 'w') as new_file:
    with open('text_replace_dictionary_input.txt', 'r') as f:
        for line in f:
            new_line = replace_all(line, mydict)
            new_file.write(new_line)
            print(line.strip('\n'), '->', new_line)