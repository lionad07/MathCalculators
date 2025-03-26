def main():
   L = float(input("Enter length (meters): "))
   W = float(input("Enter width (meters): "))
   D = float(input("Enter depth (meters): "))
   
   V = L * W * D
   
   print(f"So, you need {V:,.2f} cubic meters of concrete.")
   

if __name__ == "__main__":
    main()