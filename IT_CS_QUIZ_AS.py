import pyfiglet
from termcolor import colored
import random


                ### >>> All rights reserverd - Amir Sillam -  ###
                ### "IT and Cyber Security quiz!"  - 2021 <<< ###


## >> Start of the quiz message . << ##
def start_message():
    counter = 0

    print()
    print(f"\n\n\t\t\t\t"
          f"{colored('Welcome to IT and cyber security qu!z.', color= 'green')}")
    print("\t\t\t\t\t\t"
          "Check your Knowledge\n")
    print(f"\t\t\t {colored('*** All rights reserverd - Amir Sillam ***' ,color= 'green' ) }")
    menu(counter)

## >> End of quiz message . << ##
def end_message():
    print("\n\n\t\t\t\t\t"
          "Thanks for using our app.")
    print("\t\t\t"
          "Hope you enjoyed and expanded your knowledge !\n")

    print(f"\n\t\t\t {colored('*** All rights reserverd - Amir Sillam ' , color = 'green')} ")
    print(f"\n\t\t\t {colored(' IT and Cyber Security quiz! - 2021 ***' , color = 'green')} ")


## >> Question iterator . << ##
def menu(counter):
    while counter < 10:
        counter += 1
        print("\n\t\t\t\t\t\t ****************")
        print(f"\n\t\t\t\t\t\tQuestion Number {counter}:")
        question_Depository(counter)
    check_score(total_score)


## >> Bank of the quiz questions. << ##
def question_Depository(question):
    print("\t\t\t\t\t\t\tWho am I ? \n")
    print("\t\t\t\t\t\t ****************")

    if question == 1:
        print(f"\n\n"
              f"I like to flood some resource with a lot of requestes "
              f"and let other users\n"
              f"wait for a long period of time for their "
              f"requestes to get answered.")

    elif question == 2:
        print(f"\n"
              f"I'm controlling who can enter to or get out from your network traffic,"
              f" according to my rules !")

    elif question == 3:
        print(f"\n"
              f"I'm supposed to be long and creative but people"
              f" create me too short and unsecured ! ")

    elif question == 4:
        print(f"\nI like to trick people through email \n"
              f"and steal their personal and confidential\n"
              f"information or get them to download malicious files,\n"
              f"all by clicking on a special hyperlink I created in the message!")

    elif question == 5:
        print(f"\n"
              f"I like exploiting weak software as soon as it get's released !")

    elif question == 6:
        print(f"\n"
              f"I like to interrupt traffic between two parties and "
              f"look to steal and use their data!")

    elif question == 7:
        print(f"\n"
              f"Cyber security experts are using me (in authurized way yes?) \n"
              f"to find vulnerabilities on systems and also exploiting them.")

    elif question == 8:
        print(f"\n"
              f"Im software used on most computers(hopefully :/) and protecting "
              f"your system, "
              f"\nbut don't forget to update and run me periodically, \n"
              f"thanks in advance :)")

    elif question == 9:
        print(f"\nI'm a software that analyzes logs that come from\nvarious communication"
              f" components and software. ")

    elif question == 10:
        print(f"\nPeople uses me to gain high level access to a system "
              f"or part of it which\n"
              f"they shouldn't have access to.")


    answers_for_questions(question)


## >> Check your score << ##
def check_score(total_score):
    if total_score >= 0 and total_score <= 3 :
        print("\n\t\tContinue practicing, greatness is waiting for you !")

    elif total_score > 3 and total_score <= 6 :
        print("\n\t\tGreat knowledge, keep expanding it daily !")

    elif total_score > 6 and total_score <= 9:
        print("\n\t\t\t Expert is your second name, well done !")

    else:
        print("\n\t\tW0W !!! you knew it all , now that score is amazing. \n"
              "\t\t\t "
              "keep working hard, learning and growing !")


# >> Create list of right and wrong answers and combine
    # them to one list of answers. << #
def answers_for_questions(question):

    answers_list = []

    correct_answer = answer_Depository(question, "Correct")
    answers_list.append(correct_answer)
    other_answers = answer_Depository(question, "Wrong")
    answers_list.extend(other_answers)

    rand_list = random.sample(answers_list, len(answers_list))
    correct_index=rand_list.index(correct_answer)
    print_question_options(rand_list)


    # > User input and error handling < #
    user_input = input("\nYour answer is:  ")
    cnt = 1

    while (not user_input.isdigit() ) or \
            (int(user_input) > 4)\
            or (int(user_input) < 1):
        print(colored("\nWe accept only numeric integer values in range of 1-4,\n"
              "please try again!", color="red"))
        if cnt == 5:
            print("Too many wrong attempts, please run the program again!")
            exit(1)

        cnt += 1
        user_input = input("\nYour answer is: \n")
    print("")

    correct = ("\t\t\t\t\t "
               "You are correct, well done !")
    upd_correct = colored(correct, color="green")


    # > Update total score of the user. < #
    if int(user_input) == (correct_index + 1) :
        print(upd_correct)
        global total_score
        total_score +=1
        print(f"\t\t\t\t"
              f" Youre total score is: {total_score} out of 10")

        if question == 5 and total_score == 5 :
            print(colored("\t\t\t\t\t"
                          " You are on fire, amazing !!!", color= "red"))

    else :

        print(f"\t\t\t"
              f"  Youre total score is: {total_score} out of 10")
        message = ["   Better luck next time!" ,
                   "At least your are learning, right?" ,
                   "Next time you will be okay!" ,
                   "Mistakes makes you wiser and stronger !" ,
                   "You are neither the first nor \n"
                   "\t\t the last to make a mistake on this question ! "]
        rand_answer = random.randint(0, 4)
        print(colored("\t\t\t\t\tSorry, wrong answer!" , color= "cyan"))
        print(f"\t\t\t\t{colored(message[rand_answer], color= 'blue')}")


## >> Bank of right and wrong answers. << ##
def answer_Depository(answer, answer_type):

    if answer_type == "Correct" :
        Answers = [
               "Ddos Attack", "Firewall", "Password", "Phishing attack",
               "Zero-Day exploit", "Man in the middle attack",
               "Penetration test", "Anti-Virus" , "SIEM" , "Privilege Escalation " ]
        return Answers [answer - 1]

    else:
        count = 0
        wrong_answer_list = []
        index_list = [num for num in range(0,27)]

        #print(type(rand_answer))

        wrong_answers = [
                     "SQL injection", "Trojan Horse", "Botnet", "Cross Site Scripting - XSS",
                     "Black hat hacker", "White hat hacker", "VPN","Kerberos",
                     "Key Exchange", "Hashing algorithm", "TCP/IP model",
                     "DNS Spoofing" ,"Advanced Persistent Threats" ,
                     "Access Control List", "Wireless access point", "Load Balancer",
                     "Application Layer", "NAT" , "Intrusion Prevention System",
                     "Intrusion Detection System", "SSH", "Nmap", "Steganography" ,
                     "Wireshark", "SSL/TLS" , "Ad-Blocker" , "Ransomware attack"  ]

        # > making sure there will be 3 unique answers. < #
        while count < 3 :
            rand_answer = random.choice(index_list)

            while len(wrong_answer_list) == 0:
                    first_rand = random.choice(wrong_answers)
                    wrong_answer_list.append(first_rand)
                    wrong_answers.remove(first_rand)

                    count += 1

            else:
                other = random.choice(wrong_answers)
                wrong_answer_list.append(other)
                wrong_answers.remove(other)
                count += 1


        return wrong_answer_list


## >> Show user the 4 answer options for each question. << ##
def print_question_options(question_list):

    for quest in question_list :
        print()
        print(f"{question_list.index(quest) + 1}.{quest}")


total_score = 0
start_message()
end_message()


                ### >>> All rights reserverd - Amir Sillam -  ###
                ### "IT and Cyber Security quiz!"  - 2021 <<< ###























