class WordFilter(object):
    def __init__(self, textfile, list_valid_words=[]):
        #word filter is responsible for making sure that the list of words being drawn from is made available
        #to other classes and functions.
        self.valid_words = list_valid_words
        self.word_frequency_container = []
        #make the list of valid words a property of the class
        with open(textfile) as listtext:
            #open text file
            read = listtext.readlines()
            #read each line into an element of a list.
            for item in read:
                #for every line in the text file
                item = item.strip()
                #strip away the newline indicator '\n' 
                list_valid_words.append(item)
    def get_list_valid_words(self):
        return self.valid_words
        

class Bot(object):
    def __init__(self, c, m):
        self.dict_of_lists = {}
        print(f"Compiling words, this may take a moment..., 0%)")
        self.dict_of_lists = WordFilter("words_alpha.txt").get_list_valid_words()


    def list_in_dict(self):
        return self.dict_of_lists
    
    

#print(Bot(13).list_in_dict(12))
    
def m(string=input("Enter the 12 available letters.\n")):   
        try:   
            side1 = string[0:3]
            side2 = string[3:6]
            side3 = string[6:9]
            side4 = string[9:12]
        except IndexError:
            print("Index Error, moving swiftly along.")
        
        print(side1, side2, side3, side4)
        pass_1, pass_2, pass_3, pass_4 = [], [], {}, []
        
        for j in Bot(1, 8).list_in_dict():
                thanksclay = True
                for k in j:
                    if k not in string:
                        thanksclay = False
                if thanksclay:
                    if j not in pass_1:
                        pass_1.append(j)

        print("Pass 1 completed... (25%)\n")
    
        for l in pass_1:
            thanksclay = True
            for m in range(len(l)-1):
                if (l[m] in side1 and l[m+1] in side1 or
                    l[m] in side2 and l[m+1] in side2 or
                    l[m] in side3 and l[m+1] in side3 or
                    l[m] in side4 and l[m+1] in side4):
                    thanksclay = False
                    break                
            if thanksclay:
                pass_2.append(l)
        
        print("Pass 2 completed... (50%)\n")
        
        pass_0 = pass_2.copy()

        for x in range(len(pass_2)):
            set_string = list(string)
            for char in pass_2[x]:
                if char in set_string:
                    set_string.remove(char)
            for y in pass_0:
                knockoff = set_string.copy()
                for c in y:
                    if c in knockoff:
                        knockoff.remove(c)
                if len(knockoff) == 0:
                    pass_3[pass_2[x]] = y

        print("Pass 3 completed... (75%)\n")
        
        for key in pass_3.keys():
            if key[-1] == pass_3[key][0]:
                pass_4.append((key, pass_3[key])) 
            
        print(pass_4)


m()


#l[m] and l[m+1] in side3 or
#l[m] and l[m+1] in side4):
