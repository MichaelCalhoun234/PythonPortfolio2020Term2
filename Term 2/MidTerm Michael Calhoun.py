import sys

def open_file(file_name,mode):
    """Opens file in the given mode"""
    try:
        file = open(file_name, mode)
        return file
    except IOError as e:
        print("You have broken", file_name, "you mortal.\n", e)
        input("\nPress the enter key to exit.\n")
        sys.exit()


def next_line(the_file):
    line = the_file.readline()
    line = line.strip("\n")
    line = line.replace("/","\n")
    return line

def question_block(the_file):
    """ Reads the question block from the file and returns
category, question, answers list, correct answer, and explanation"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range (4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category,question,answers,correct,explanation
        
    
def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to my MidTerm test.\n")
    print("\t\t This test was created by", title, "\n")



def main(file_name):
    file_name = file_choose()
    file = open_file(file_name,"r")
    title = next_line(file)
    name = input("Please enter your full name.")
    questions = 0
    score = 0
    category,question,answers,correct,explanation = question_block(file)
    welcome(title)
    while category:
        print(category)
        print()
        print(question)
        print()
        for i in range(len(answers)):
            print("\t", i + 1, "-", answers[i])
            userAnswer = input("What's your answer?: ")

            if userAnswer == correct:
                score += 1
                questions += 1
                print("Correct")
            else:
                questions += 1
                print("Wrong")
            print()
            print(explanation)
            category,question,answers,correct,explanation = question_block(file)
        report_card(name,questions,score)


def file_choose():
    while True:
        file = input("Please enter in the name of the test file.")
        if ".txt" in file and " " not in file:
            return file
        else:
            print("That's not the file name.")


def write_score(name,score):
    file = open_file("scores.txt","a+")
    pair = name+":   "+score+"\n"
    line = []
    line.append(pair)
    file.writelines(line)
    file.close()



def report_card(name,questions,score):
    percent = score/questions * 100
    A = """  A
            A A
           A   A
          AAAAAAA
         A       A
        A         A"""
    B = """"
        BBBBBBB
        B       B
        B       B
        BBBBBBB
        B       B
        B       B
        BBBBBBBB"""
    C = """
        CCCCCCCC
        C
        C
        C
        C
        CCCCCCCC"""
    D = """
        DDDDDDD
        D       D
        D       D
        D       D
        D       D
        DDDDDDD"""
    F = """
        FFFFFFFFFF
        F
        F
        FFFFFFF
        F
        F
        F"""

    print("That all the questions.")
    if percent  >= 90:
        print(A)
    elif percent >= 80 and percent < 90:
        print(B)
    elif percent >= 70 and percent < 80:
        print(C)
    elif percent >60 and percent < 70:
        print(D)
    elif percent >= 50 and percent < 60:
        print(F)
    writen_score(name,score)


    file.close()
        
        
file_name = ""
main(file_name)
            


    
