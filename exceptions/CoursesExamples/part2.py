# try catch with else   

try :

    x= int(input( " what's x ?"))
   
except ValueError :
    print ( " bro x is an integer ")
#the x is exuted only when try catch succeeded
else :
    print(f"x is {x}")

