def main():
   Rise = float(input("Enter rise (meters): "))
   Run = float(input("Enter run (meters): "))
   
   S = (Rise/Run) * 100
   print (f"So, the slope of the road is {S:,.2f}%.")
  
if __name__ == "__main__":
    main()
    