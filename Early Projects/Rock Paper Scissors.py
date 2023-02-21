from random import randint

def play_again():
    choice = str(input("""Continue?
Enter 'Y' for 'Yes', or anything else for 'No'"""))
    if choice.lower() != "y":
        return False
    else:
        return True

class Rock_paper_scissors:
    def __init__(self, rounds, round_number,player_wins,computer_wins):
        self.rounds=rounds
        self.round_number=round_number
        self.player_wins=player_wins
        self.computer_wins=computer_wins
        self.score_tracker = []
        
    def computer_choice(self):
        self.computer_number=randint(1,3)
        if self.computer_number==1:
            print('Computer is Rock')
        elif self.computer_number==2:
            print('Computer is Paper')
        else:
            print('Computer is Scissors')
        
    
    def player_choice(self, number):
        self.player_number = number
        if self.player_number == 1:
            print('You are Rock')
        elif self.player_number == 2:
            print('You are Paper')
        else:
            print('You are Scissors')
    
    def who_won_round(self):
        s = "You Win"
        t = "You Lose"
        if self.player_number==self.computer_number:
            self.score_tracker.append('tie')
            print("Tie")
        else:
            if self.player_number ==2 :
                if self.player_number>self.computer_number:
                    self.score_tracker.append('p win')
                    print(s)
                else:
                    self.score_tracker.append('c win')
                    print(t)
            elif self.player_number==1:
                if self.computer_number==3:
                    self.score_tracker.append('p win')
                    print(s)
                else:
                    self.score_tracker.append('c win')
                    print(t)
            else:
                if self.computer_number==2:
                    self.score_tracker.append('p win')
                    print(s)
                else:
                    self.score_tracker.append('c win')
                    print(t)
                    
    def round_complete(self):
            self.rounds-=1
            
    def who_won_game(self):
        if self.score_tracker.count('p win')==self.score_tracker.count('c win'):
            print('The Game Was a Tie!')
        elif self.score_tracker.count('p win')>self.score_tracker.count('c win'):
            print('You Won the Game!')
        else:
            print('You Lost the Game!')

print("""
Rock! Paper! SCISSORS!
----------------------
You will play first.
Enter '1' for Rock, '2' for Paper, and '3' for scissors.
Good luck!""")
run=True
while run:
    game=Rock_paper_scissors(rounds=3,round_number=1,player_wins=0,computer_wins=0)
    while game.rounds>0:
        try:
            x=eval(input('Please enter a number: '))
        except:
            x = 3
        game.player_choice(x)
        game.computer_choice()
        print()
        game.who_won_round()
        game.round_complete()
        print()
    game.who_won_game()
    print()
    run = play_again()
print("Thanks for Playing")

    
    

    