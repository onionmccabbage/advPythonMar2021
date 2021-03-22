# special operators

# for example the asterisk can mean mathematical multiply or repeat a string
# __mult__

# overriding the __eq__ built-in operator
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, other_word):
        return self.text.lower() == other_word.text.lower()
    def __add__(self, other_word):
        return '{}{}'.format(other_word.text, self.text)

if __name__ == '__main__':
    w1 = Word('ha')
    w2 = Word('Ha')

    print('ha' == 'Ha') # False
    print(w1 == w2) # True - uses our own __eq__ method
    print(w1+w2) # Haha
