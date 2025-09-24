# Program to print numbers 1 to 10
# This is a simple Python program that demonstrates basic loop functionality
# Author: Copilot
# Course: COMP5241 Software Engineering and Development - Lecture 4

def main():
    """
    Print numbers from 1 to 10 using a for loop
    
    This function demonstrates:
    - Using range() function to generate a sequence of numbers
    - Using a for loop to iterate through the sequence
    - Using print() function to output each number
    """
    # Create a loop that iterates from 1 to 10 (inclusive)
    # range(1, 11) generates numbers from 1 to 10
    # The second parameter (11) is exclusive, so we use 11 to include 10
    for i in range(1, 11):
        # Print each number on a new line
        # The variable 'i' takes each value from the range in sequence
        print(i)

# This is the standard Python idiom to run the main function
# when the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to start the program execution
    main()