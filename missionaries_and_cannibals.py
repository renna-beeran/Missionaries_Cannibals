from IPython.display import clear_output

boat_side = "Right"
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0

def disp(bside):
    user_interface = ''

    for i in range(missionaries_on_left):
        user_interface = user_interface + '\U0001f482'

    for i in range(cannibals_on_left):
        user_interface = user_interface + '\U0001f479'
        
    user_interface = user_interface + ' '    
        
    if bside == "Right" :
        for i in range(5):
            user_interface = user_interface + '\U0001f30a'
        user_interface = user_interface + '\U0001f6A2'
    else:
        user_interface = user_interface + '\U0001f6A2'
        for i in range(5):
            user_interface = user_interface + '\U0001f30a'
            
    user_interface = user_interface + ' '    

    for i in range(missionaries_on_right):
        user_interface = user_interface + '\U0001f482'

    for i in range(cannibals_on_right):
        user_interface = user_interface + '\U0001f479'
    
    print(user_interface)
    
#print('M =',missionaries_on_left, 'C =',cannibals_on_left, '|-----B|', 'M =',missionaries_on_right, 'C =',cannibals_on_right)
disp(boat_side)

while True :
    missionaries = int(input("Enter Number of Missionaries : "))
    cannibals = int(input("Enter Number of Cannibals : "))
    
    if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:
        print("Invalid Move")
        continue
    
    '''  
    if boat_side == "Right":
        print("Boat is on right side....")
    else:
        print("Boat is on Left side......")
    '''
    
    if boat_side == "Right":
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals :
            print("INVALID MOVE")
            continue
        
        missionaries_on_right -= missionaries
        cannibals_on_right -= cannibals
        
        missionaries_on_left += missionaries
        cannibals_on_left += cannibals
        
        boat_side = "Left" 
    
    elif boat_side == "Left":
        if missionaries_on_left < missionaries or cannibals_on_left < cannibals :
            print("INVALID MOVE")
            continue
        
        
        missionaries_on_left -= missionaries
        cannibals_on_left -= cannibals
        
        missionaries_on_right += missionaries
        cannibals_on_right += cannibals
        
        boat_side = "Right"
        
    clear_output()
    #print('M =',missionaries_on_left, 'C =',cannibals_on_left, '|-----B|', 'M =',missionaries_on_right, 'C =',cannibals_on_right)
    disp(boat_side)
    
    if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
        print("YOU LOSE")
        break
    
    if missionaries_on_left == 3 and cannibals_on_left == 3:
        print("YOU WIN")
        break