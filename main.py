'''
NAME: Jonathan Argumedo
ASSIGNMENT: Lab 4 (HashTable Anagrams)
CLASS: DATA STRUCTURES 
PROFESSOR: Diego Aguirre
TA: Anindita  Nath 
DATE: November 13, 2018
UPDATED BY: (Your name goes here)
'''
from hashTable import HashTable

'''
'populateTable' is a method that simply takes 2 parameters (hashTable and a file )
it will populate tha hash table with the contents of the file. The insertion method 
of the hashTable always return the number of comperasions that were made in order to
insert a certain word. Therefore, populateTable will return the total number 
of comperasions that were made in total while reading the file. 
'''

def populateTable(theHashTable, file):
    counter = 0 
    for line in file:
        counter += theHashTable.insertWord(line) #insert the line being read (look at 'insertWord' method for more info) 
        #counter is increased because 'insertWord' method returns the number of comperasions done in each word
    return counter #return the number of comperasions that were made in the whole file

'''
'anagrams' method simply generates permutations of a word that is passed as
a parameter, it then cheks if each permutation is found in the hash table
if the word is found then it get's append it into a list. 
The method then resturns the length of a list. 
'''
def anagrams(word, theHashTable, listOfWords, prefix="" ):
    if len(word) <= 1:
        stri = prefix + word
        if theHashTable.search(stri) == True: #searches in HashTable if found the the (search method returns 1)
            listOfWords.append(word)
            print("Found the anagram: %s" % (prefix + word))         
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.
                anagrams(before + after, theHashTable, listOfWords, prefix + cur)
    return len(listOfWords)

'''main method starts here'''
def main():
    #check how many words are found in the file (table size)
    try:
        wordsInFile = 0 #keep count of how many words are in the file
        fileName = input("Enter file name (make sure the extension is provided [.txt]): ")
        file = open(fileName, "r").read().split("\n")
        for line in file:
            wordsInFile += 1
        
        #create table with the size
        theHashTable = HashTable(wordsInFile) #crate a HashTable with the size of how many words are found
        compare = populateTable(theHashTable, file)#will populate the table with each word in the file
        
        print("\n")
        print("****************************Computing Some Stats****************************")
        print("Load Factor is: ", theHashTable.loadFactor(wordsInFile))
        print("The Average Comparison of a word is: ", compare/wordsInFile)
        print("There are [%d] words in the file called '%s' " % (wordsInFile, fileName))
        print("****************************************************************************")
        print("\n")
        userWord = input("Enter the word you want to look for: ")
        
        listOfWords = [] #used by the anagrams method
        print("****************************Computing Anagrams****************************")
        print("\n\nFor the word '%s', I found [%d] valid anagrams" % (userWord, anagrams(userWord, theHashTable, listOfWords)))
        print("**************************************************************************")
        
    except FileNotFoundError:
        print("Oops! File not found. Check your file")
        return
main()