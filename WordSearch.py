import math

word_bank = ("string","print","random","min","max","for i in range","datetime","len","array","global","boolean","variable","comma","data type","\\","str.format","index values","data elements","tuple","import","logical")
ROWS = 20
COLS = 20
puzzle ="""
VFWRXXBTSHEDYRLHFTGSUAOLMDNRSFOYRATUPLETSFLAEAGOWYOIUNHIWZSRWMGUENAPTTBRWGDONUWIDZOLEWRMMINEMEOANDVNPYODVSRIUOXLTASATBEGXOUENOATYPEBPXTICAOXBVHOLAYQPOSAIRLMSYTJDZBGDLRBREJITXICOMMAZQTQAVIXAMIRFLRNTVOYWUIBCETSGCAABBTGTZCFFGOGJLQANQOVELSXUNNTHLHSTNEMELESVGWVHRKBGEUDSZFMGXVSQVIWQUURVTQZKOSJQCSUFLACIGOLTUYECKHSXQVSIJWAIBDIIQBDILJDYZWPYFQDZPHUJIMIONWQKYCPVZEAZSAYEFGFQJEMITETADLCZPEMEFXZYNONYRTESOABLTMO
"""

WORDS = """ARRAY BOOLEAN COMMA DATA DATETIME ELEMENTS FOR FORMAT GLOBAL IMPORT INDEX LEN LOGICAL MAX MIN PRINT RANDOM RANGE STR STRING TUPLE TYPE VALUES VARIABLE
"""
QUESTIONS = ["_____ are immutable. This means that once defined, they cannot be changed.",
             "The ______ function prints the specified message to the screen, or other standard output device.",
             "Generate pseudo ______ numbers. Almost all module functions depend on the basic function random() which generates a random float uniformly in the semi-open range [0.0, 1.0).",
             "returns the smallest item in an iterable",
             "returns the largest item in an iterable",
             "returns a range object",
             "returns the date and time",
             "returns the number of items in an object.",
             "keyword is a keyword that allows a user to modify a variable outside of the current scope",
             "is data type used to represent logic values True and False",
             "A Python is a reserved memory location to store values.",
             "what do you put for a new character in a print",
             "are the classification or categorization of data items.",
             "used so you can put the same line of code on a different line",
             "is one of the string formatting methods in Python3",
             "method searches an element in the list and returns its index.",
             "A expression evaluates to one of two states true or false.",
             "brings in certain stuff",
             "is a sequence of immutable Python objects."]



def display_puzzle(puzzle):
     minIndex = 0
     pHeight = int(input(" How long is the first row 0 - 19 "))
     maxIndex = pHeight +1
     print(maxIndex)
     for i in range(20):
          print(puzzle[minIndex : maxIndex])
          minIndex += 20
          maxIndex += 20


def get_words_questions():
    import random
    while True:
        index = random.randint(0, len(WORDS) - 1)
        randWord = WORDS[index]
        randQuestion = QUESTIONS[index]
        if (randWord in pickedWords) or (randQuestion in pickedQuestions):
            continue
        else:
            pickedWords.append(randWord)
            pickedQuestions.append(randQuestion)
            return randWord, randQuestion

picked = []
def random_question(WORDS,QUESTIONS,picked):
    import random
    while WORDS:
        choice = random.randint(0,len(WORDS))
        if choice not in picked:
            question = QUESTIONS.pop(choice)
            answer = WORDS.pop(choice)
            picked.append(choice)
            return question, answer


def question_answer(puzzle):
    letters = []
    nums = []
    number = ""
    pos = input("Enter the grid position of the word you are looking for\nbe sure to seperate each position with a ,\n")
    for i in pos:
        if i != ",":
        	number = number + i
        else:
            if number.isdigit():
                nums.append(int(number))
                number = ""
    nums.append(int(number))
    print(nums)
    word=""
    for i in nums:
        word = word + puzzle[i]
    print(word)


display_puzzle(puzzle)           
question_answer(puzzle)             
random_question(WORDS,QUESTIONS,picked)             
get_words_questions()
