
import random
count_h =0
count_c =0
print("__________________________Rock...Paper...Scissors__________________________\n")
print("Hey! Welcome to the game Lets begin...\n")
keep_playing = True
while keep_playing:
    
    h_c=int(input("1.Rock\n2.Paper\n3.Scissors\n"))
    humanchoice=True
    while(humanchoice):
        if(h_c==1):
            h_choice='rock'
            humanchoice=False
        elif(h_c==2):
            h_choice='paper'
            humanchoice=False
        elif(h_c==3):
            h_choice='scissors'
            humanchoice=False
        else:
            print("Give input of numbers from 1 to 3")
            h_c=int(input("1.Rock\n2.Paper\n3.Scissors\n"))
    print('you choose ' + h_choice)
    c_choice = random.choice(['rock', 'paper', 'scissors'])
    print('the computer chooses ' + c_choice)
    

    if((h_choice=='rock' and c_choice=='scissors') or (h_choice=='scissors' and c_choice=='paper') or(h_choice=='paper' and c_choice=='rock')):
        print("you wins")
        count_h += 1
    elif(h_choice == c_choice):
         print("draw")
    else :
        print("computer wins")
        count_c += 1
    answer=""
    answer = input("\nDo you want to play again?(y/n)")
    if answer in "Nn":
        keep_playing = False
        print("\nThanks for playing!")
        print("Computer score is:"+str(count_c))
        print("Your score is :" + str(count_h))

        print("\nOverall results:")
        if count_c>count_h:
            print("Better luck next time!\n")
        elif count_c == count_h:
            print("It is a draw\n")
        else :
            print("You win!\n")
        print("_________________________Rock...Paper...Scissors_________________________")