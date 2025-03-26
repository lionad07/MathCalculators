def main():
    V2 = float(input("Enter value of V2 (L): "))
    C2 = float(input("Enter value of C2 (g/L): "))
    C1 = float(input("Enter value of C1 (g/L): "))
    
    V1= (C2*V2)/C1
    print(f"So, you need {V1:,.2f} liters of the original slurry.")

if __name__ == "__main__":
    main()