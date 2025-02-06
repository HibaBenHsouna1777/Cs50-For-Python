#the keyboard pass effect "not print the message "
#the main 
def main () :
    x= get_int()
    print(f" x is {x }")

# a function that exxuted the infinite loop 
def get_int():
    while True :
        try :
    
            return int(input( " what's x ?"))
       
        except ValueError :
            pass
        
           
    
        

main()