def check_bit():
    print("Welcome to te Bit Checker Game")
    print("You  enter a number, and I'll tell you if it's a 0-bit or a 1-bit. \n" )

    while True:
        bit = input("Enter a bit (0 or 1), or type 'exit' to quit: " ).strip()


        if bit.lower() == 'exit' :
            print("Thanks for playing! Bye")
            break
        elif bit== '0':
            print("You enterered 0 That;s called a ** zero bit**!\n")

        elif bit== '1' :
            print(" You entered 1 That's a **one bit**!\n")

        else:
            print("Ooops! That's not a valid bit. Please enter only 0 or 1 \n")

# Run the program
check_bit()
