def main():
   w = float(input("Enter load (N/m): "))
   L = float(input("Enter length (m): "))
   
   F = w * L
   print (f"So, the total load acting on the beam is {F:,.2f} N.")
  
if __name__ == "__main__":
    main()