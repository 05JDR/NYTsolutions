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
        self.x = WordFilter("dictionary.txt").get_valid_words()

    def find_least_worst_case_options(self, full_list, past_list=None):
        self.base_value = len(full_list)
        for i in range(len(full_list)):
            self.guess_options = []
            for j in range(1, len(full_list)):
                all_letters = True
                for k in full_list[j]:
                    if k in full_list[i]:
                        all_letters = False
                        break
                if all_letters:
                    self.guess_options.append(full_list[j])
            if len(self.guess_options) < self.base_value:
                self.smallest_list_of_options = self.guess_options.copy()
                self.base_value = len(self.guess_options)
                self.store_word = full_list[i]
        return self.store_word
        
    
    def manage_info(self, prev_word, list_letters_thrown_away=[]):
         dict_confirmed_letters, dict_immovable_letters = {}, {}
         pass_1, pass_2, pass_3 = [], [], []
         x = input(f"Enter your results from '{prev_word}' Key: enter 0 for gray, 1 for yellow, and 2 for green.\n")
         for c in range(len(x)):
             if x[c] == "2":
                 dict_immovable_letters[c] = prev_word[c]
             if x[c] == "1":
                dict_confirmed_letters[c] = prev_word[c]
             if x[c] == "0":
                if prev_word[c] not in dict_immovable_letters.values() and prev_word[c] not in list_letters_thrown_away:
                    list_letters_thrown_away.append(prev_word[c])
         if x == "00000":
            for word in self.smallest_list_of_options:
                check_all_letters = True
                for c in dict_confirmed_letters:
                    if c in word:
                        check_all_letters = False
                        break
                if check_all_letters:
                    pass_1.append(word)
         else:
             for word in self.x:
                 check_all_letters = True
                 for c in word:
                     if c in list_letters_thrown_away:
                        check_all_letters = False
                        break
                 if check_all_letters:
                     pass_1.append(word)

             for word in pass_1:
                 check_all_letters = True
                 for char in dict_confirmed_letters.values():
                    if char not in word:
                        check_all_letters = False
                        break
                 for idx in dict_confirmed_letters.keys():
                     if word[idx] == dict_confirmed_letters[idx]:
                         check_all_letters = False
                 if check_all_letters:
                     pass_2.append(word)

             for word in pass_2:
                 check_all_letters = True
                 for char in dict_immovable_letters.keys():
                     if word[char] != dict_immovable_letters[char]:
                         check_all_letters = False
                 if check_all_letters:
                     pass_3.append(word)
             if x != "22222":
                print(f"Next suggestion: {self.find_least_worst_case_options(pass_3)}")
                self.manage_info(self.find_least_worst_case_options(pass_3), list_letters_thrown_away)
             else:
                print(f"{self.find_least_worst_case_options(pass_3)} is the correct answer yay!")
    
                   

                 
             
                    
                 
                 
             
            




start = time.time()            
Algorithm().manage_info("arose")
end = time.time()
print(f"total time elapsed: {end-start}")