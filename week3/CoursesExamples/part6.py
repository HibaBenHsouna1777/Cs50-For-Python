#prompt in the function
#One final refinement that could improve the implementation of this get_int 
#function. Right now, notice that we are relying currently upon the honor system that the
#x is in both the main and get_int functions. We probably want to pass in a prompt that the
#user sees when asked for input. Modify your code as follows.
#the main 
def main () :
    x= get_int("what ' s x ?")
    print(f" x is {x }")

# a function that exxuted the infinite loop 
def get_int(prompt):
    while True :
        try :
    
            return int(input(prompt))
       
        except ValueError :
            pass
        
           
    
        

main()
