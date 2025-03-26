def main():
   applied_force= float(input("Enter the value of force applied (N): "))
   cross_section_area= float(input("Enter the value of the cross section area (m^2): "))
   
   sigma= applied_force/cross_section_area
   
   print(f"So,the stress on the beam is {sigma:,.2f} Pa")

if __name__ == "__main__":
    main()