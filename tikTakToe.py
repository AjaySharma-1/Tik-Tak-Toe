# let's try makeing a game ( tik tak toe ) it's gonna be so much fun 
# Name : Ajay Sharma 
# instagram : 
class TikTakToe: 
    def __init__(self) :
        self.user_one = False
        self.user_two = False
        self.choices = [""]*9
        self.choosed_option = []
        self.turn = 0
        self.change_turn = False
        self.isWin= False
        self.winningComninations = [ [1,2,3],[4,5,6],[7,8,9],
                                [1,4,7],[2,5,8],[3,6,9],
                                [1,5,9],        [3,5,7] ]
        self.winningMoves= []
        
        
    def location(self):
        while True:
            try:
                turn= int(input(f"Player-{'2' if self.user_one else '1'} Enter location: "))
                if turn in list(range(1,10)) :
                    self.turn = turn
                    if turn not in self.choosed_option:
                        self.change_turn = True
                    return
                else: 
                    print("Enter only the value within the range 1 to 9.")       
            except ValueError:
                print("Only enter numbers you idiot..!")
            
                    
    def users_input(self):
        return "O" if self.user_one else "X"

        
    def fill_box(self):
        choosed = self.turn
        if choosed not in self.choosed_option:
            self.choices[self.turn-1] = self.users_input()
            self.choosed_option.append(choosed)
    def Win(self):
        
        for moves in self.winningComninations:
            moves_combination = []
            for move in moves:
                moves_combination.append(self.choices[move-1])
            self.winningMoves.append(moves_combination)
            
        if ['X','X','X'] in self.winningMoves or ['O', 'O','O'] in self.winningMoves:
            self.isWin = True
        else: 
            self.isWin= False
            
           
        
            
    def Winner(self):
        if ['X','X','X'] in self.winningMoves:
            print("Player-2 is winner...!!!")
            
        elif ['O', 'O','O'] in self.winningMoves:
            print("Player-1 One is winner.....!!!")
            
        else: 
            print("It's draw....!!! ")
        
                

  
tikTakToe= TikTakToe()   
                  
instruction= f'''    |  1 |  2 | 3  |   
    |  4 |  5 |  6 |  
    |  7 |  8 |  9 |'''
    
print(instruction)

i= 0 
while True: 
    if set(tikTakToe.choosed_option)==(set(range(1,10))):
        break
    tikTakToe.location()
    if i%2== 0:
        tikTakToe.user_one= True
        tikTakToe.user_two = False
    else:
        tikTakToe.user_one= False
        tikTakToe.user_two= True

    
    tikTakToe.users_input()   
    
    tikTakToe.fill_box()
    
    box= f'''    |  {tikTakToe.choices[0]} |  {tikTakToe.choices[1]} |  {tikTakToe.choices[2]} |   
    |  {tikTakToe.choices[3]} |  {tikTakToe.choices[4]} |  {tikTakToe.choices[5]} |  
    |  {tikTakToe.choices[6]} |  {tikTakToe.choices[7]} |  {tikTakToe.choices[8]} |
    
    '''     
    print(box)
    tikTakToe.Win()
    if tikTakToe.isWin:
        break
    if tikTakToe.change_turn:
        i+=1
    tikTakToe.change_turn= False
print(tikTakToe.Winner())
