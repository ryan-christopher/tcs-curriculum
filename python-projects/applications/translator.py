

#translator project

english = {
    "hello":"hello"
}

french = {
    "hello":"bonjour"
}

spanish = {
    "hello":"hola"
}


translate_lang = input("Which language are you translating to? ")
print()
start_lang = input("What language are you translating from? ")
print()
word = input("What word do you want to translate? ")

print("""
Starting language: """ + start_lang + """

Target language: """ + translate_lang + """

""" + word + """ translates to: """ + spanish[word]
)