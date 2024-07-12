import tkinter as tk
from tkinter import messagebox
import random as rd

class RockPaperScissors:
    def __init__(self,root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("700x400")
        self.root.iconbitmap('icon.ico')

        #Title
        self.title_label = tk.Label(root, text="Rock Paper Scissors Game", font=("Berlin Sans FB", 20))
        self.title_label.grid(row=0, column=0, columnspan=5, pady=10, padx=10)
        
        #Choices
        self.userChoice = ''
        self.computerChoice=''
        self.User_Choice_label = tk.Label(root, text=f"User Choice: {self.userChoice}", font=("Berlin Sans FB", 12))
        self.User_Choice_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.Computer_Choice_label = tk.Label(root, text=f"Computer Choice: {self.computerChoice}", font=("Berlin Sans FB", 12))
        self.Computer_Choice_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        
        #Buttons
        buttons = [('Rock',3,1),('Paper',3,2),('Scissors',3,3)]
        for (text,row,col)in buttons:
            btn = tk.Button(root,text=text,width=8,height=3,command=lambda t=text: self.buttonClick(t))
            btn.grid(row=row, column=col, padx=20, pady=5) 
        #Quit button
        self.quit_button = tk.Button(root, text="Quit", command=self.quit_program, font=("Berlin Sans FB", 12))
        self.quit_button.grid(row=7, column=0, columnspan=5, pady=10, padx=10)

        #score
        self.userScore = 0
        self.computerScore = 0
        self.User_Score_label = tk.Label(root, text=f"User Score: {self.userScore}", font=("Berlin Sans FB", 12))
        self.User_Score_label.grid(row=4, column=4, pady=10, padx=10, sticky="e")

        self.Computer_Score_label = tk.Label(root, text=f"Computer Score: {self.computerScore}", font=("Berlin Sans FB", 12))
        self.Computer_Score_label.grid(row=5, column=4, pady=10, padx=10, sticky="e")
        #who won
        self.Who_Won_label = tk.Label(root, text="", font=("Berlin Sans FB", 20))
        self.Who_Won_label.grid(row=6, column=0, columnspan=5, pady=10, padx=10)
    
    def buttonClick(self,value):
        self.userChoice = value
        self.User_Choice_label.config(text=f"User Choice: {value}")
        self.computerChoice = self.randomComputerChoice()
        self.Computer_Choice_label.config(text=f"Computer Choice: {self.computerChoice}")
        self.chooseWinner(self.userChoice,self.computerChoice)
    
    def randomComputerChoice(self):
        choices = ["Rock","Paper","Scissors"]
        self.choice = rd.choice(choices)
        return self.choice
    
    def chooseWinner(self,player,computer): 
        match player:
            case 'Rock':   
                if(computer == 'Rock'):
                    self.Who_Won_label.config(text="Draw!")
                elif(computer == 'Scissors'):
                    self.userScore +=1
                    self.User_Score_label.config(text=f"User Score:{self.userScore}")
                    self.Who_Won_label.config(text="You Win!")
                else:
                    self.computerScore +=1
                    self.Computer_Score_label.config(text=f"Computer Score:{self.computerScore}")
                    self.Who_Won_label.config(text="Computer Wins!")
                    
            case 'Paper':
                if(computer == 'Paper'):
                    self.Who_Won_label.config(text="Draw!")
                elif(computer == 'Rock'):
                    self.userScore +=1
                    self.User_Score_label.config(text=f"User Score:{self.userScore}")
                    self.Who_Won_label.config(text="You Win!")
                else:
                    self.computerScore +=1
                    self.Computer_Score_label.config(text=f"Computer Score:{self.computerScore}")
                    self.Who_Won_label.config(text="Computer Wins!")

            case 'Scissors':
                if(computer == 'Scissors'):
                    self.Who_Won_label.config(text="Draw!")
                elif(computer == 'Paper'):
                    self.userScore +=1
                    self.User_Score_label.config(text=f"User Score:{self.userScore}")
                    self.Who_Won_label.config(text="You Win!")
                else:
                    self.computerScore +=1
                    self.Computer_Score_label.config(text=f"Computer Score:{self.computerScore}")
                    self.Who_Won_label.config(text="Computer Wins!")
                    
    def quit_program(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()    
    app = RockPaperScissors(root)
    root.mainloop()
