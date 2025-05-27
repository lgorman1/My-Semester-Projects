#Luisa Gorman
#Magic 8 Ball
#1/24/25

#Init
import random
magic_list = ["Yes Definetly", "Most Likely", "My Reply is Yes", "Outlook Good", "It is Certain", "Ask Again Later", "Maybe", "Possibly", "I Don't Know", "Unknown", "Don't Count on It", "My Reply is No", "Definetly No", "Outlook Bad", "It Doesnt Look Good"]
#Func
def magic8ball():
    print("Welcome to Magic 8 Ball")
    while True:
        question = input("Enter a yes or no question:")
        print(question)

        if question.endswith("?"):
            print(random.choice(magic_list))
            another_question = input("Do you want to ask another question? (yes/no): ")
            if another_question == "no" or "No" or "N" or "n":
                print("Thank you for playing Magic 8 Ball!")
                break

        else:
            print("Please re-enter the question with a question mark at end!")




#Main
magic8ball()
