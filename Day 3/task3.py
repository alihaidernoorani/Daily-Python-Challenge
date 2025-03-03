cal=True
while cal:
  print("""\nChoose operation:

  1. Addition (+)

  2. Subtraction (-)

  3. Multiplication (*)

  4. Division (/)
  """)
  choice = input("Enter choice (1-4): ")
  a = float(input("Enter first number: "))
  b = float(input("Enter second number: "))
  print("Calculating...")

  if choice == '1':
      print(f"{a} + {b} = {a+b:.2f}")
  elif choice == '2':
      print(f"{a} - {b} =  {a-b:.2f}")
  elif choice == '3':
      print(f"{a} * {b} =  {a*b:.2f}")
  elif choice == '4':
     if b == 0:
        print("Error: Division by zero is not allowed")
     else:
        print(f"{a} / {b} =  {a/b:.2f}")
  else:
      print("Invalid choice")
  con = input("\nPress Y to continue...").strip().lower()
  if con != 'y':
    cal = False
    print("Calculator closed.")