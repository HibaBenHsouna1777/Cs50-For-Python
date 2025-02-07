def main():
    print(get_fuel())

def get_input():
    while True:
        try:
        
            x = int(input("Enter x:  "))
            y = int(input("Enter y:  "))
            return (x/y)
        
   
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        
        

def get_fuel():   
        per= get_input()*100
        if per>99:
          return ("full")
        elif per <1:
            return ("empty")
        
        else :
             return (f"per is : {per} %")

    
    
        
            
        
            
main()
        




