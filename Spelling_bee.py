class CollectWords(object):
    def __init__(self, textfile, listvalidwords=[]):
        self.listvalidwords = listvalidwords
        with open(textfile) as allwords:
            WORDLIST = allwords.readlines()

        for i, item in enumerate(WORDLIST):
            if len(item.strip()) > 3:
                listvalidwords.append(item.strip())

    def get_stripped_words(self):
        return self.listvalidwords
    
    def collect_letters(self, letters=[]):
        for chars in input("Please enter the letters usable for your spelling bee. Do not separate the letters.\n If any letters are required for each word, capitalize them."):
            letters.append(chars)
        return letters
    
    def return_valid_options_flagless(self, valid_options=[], letters=[], thanksclay=True):
        for word in self.get_stripped_words():
            thanksclay = True
            for letter in word:
                if letter not in letters:
                    thanksclay = False

            if thanksclay:
                valid_options.append(word)
        return valid_options

    def return_valid_options(self, valid_options=[], letters=[], thanksclay=True, flag=None):
        try:
            ensure_lower = []
            for item in letters:
                if item.isupper():
                    flag=item.lower()
                ensure_lower.append(item.lower())
                
            for word in self.get_stripped_words():
                thanksclay = True
                for letter in word:
                    if flag not in word:
                        thanksclay = False
                        
                    if letter not in ensure_lower:
                        thanksclay = False
                if thanksclay:
                    valid_options.append(word)
            return valid_options
        except TypeError:
            print("Exception caught: no flag.\n")
            self.return_valid_options_flagless()

    
somedict = {}

for numbers in range(14):
    #there will likely not be a word with more than 14 characters, and to sort by length I have to prematurely populate the dictionary with lengths
    somedict[numbers] = "None"

try:
    for item in CollectWords("words_alpha.txt").return_valid_options(letters=list(input("Please enter the spelling bee letters for the day, and capitalze the required one.\n\nDO NOT include spaces.\n\n"))):
        if len(somedict[len(item)]) == 1:
            somedict[len(item)] = item
        else:
            somedict[len(item)] += f", {item}"

except TypeError:
    print("It seems there was no flagged letter in your last input. Printing all words containing any of these letters.")
    for item in CollectWords("words_alpha.txt").return_valid_options_flagless(letters=list(input("Please enter the spelling bee letters for the day, and capitalze the required one.\n\nDO NOT include spaces.\n\n"))):
        if len(somedict[len(item)]) == 1:
            somedict[len(item)] = item
        else:
            somedict[len(item)] += f", {item}"    

for item in somedict:
    print(f"{item} letter words: {somedict[item]}\n\n")
    
