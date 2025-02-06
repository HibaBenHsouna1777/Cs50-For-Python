# try catch with while true 

while True :
    try :

        x= int(input( " what's x ?"))
   
    except ValueError :
        print ( " bro x is an integer ")

    else :
        break 
#the loop will be break only if we tape an integer 
print(f"x is {x}")