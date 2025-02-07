
def main () :
  pace = get_pace(50,0)
  print(f"you need to run each mile in {round(pace ,2)} minutes ")
  
  
  
  
  
def get_pace(km , minutes):
   if not minutes >0 :
        raise ValueError("invalid value for minutes ")
   
   
   return km /minutes 


main()