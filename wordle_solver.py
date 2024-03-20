import time
class WordFilter(object):
    def __init__(self, textfile):
        with open(textfile) as unparsed_text:
            parsed_text = unparsed_text.readlines()
        self.list_valid_words = []
        for item in parsed_text:
            if len(item.strip()) == 5:
                self.list_valid_words.append(item.strip())
    def get_valid_words(self):
        return self.list_valid_words
    
class Algorithm(object):
    def __init__(self):
        x = WordFilter("dictionary.txt").get_valid_words()
        self.base_value = len(x)
        print("Calculating best first word, this will take roughly 70 seconds.")
        for i in range(len(x)):
            self.first_guess_options = []
            for j in range(1, len(x)):
                all_letters = True
                for k in x[j]:
                    if k in x[i]:
                        all_letters = False
                        break
                if all_letters:
                    self.first_guess_options.append(x[j])
            if len(self.first_guess_options) < self.base_value:
                self.base_value = len(self.first_guess_options)
                self.store_word = x[i]
    def return_first_word(self):
        return self.store_word


start = time.time()            
print(f"I recommend: {Algorithm().return_first_word()}")
end = time.time()
print(f"total time elapsed: {end-start}")