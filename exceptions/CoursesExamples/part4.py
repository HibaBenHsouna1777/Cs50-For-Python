#the main 
def main () :
    x= get_int()
    print(f" x is {x }")

# a function that exxuted the infinite loop 
def get_int():
    while True :
        try :
    
            x= int(input( " what's x ?"))
       
        except ValueError :
            print ( " bro x is an integer ")
    
        else :
        #return is way stornger than break 
            return x


    
