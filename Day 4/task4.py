run = True
while run:
  num = input("\nEnter a number: ")
  try:
    num = int(num)
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
  except ValueError:
    print("Error: Enter a valid number")
  con = input("\nPress y to continue: ").strip().lower()
  if con != 'y':
    run = False