# This program inputs the time library and asks the user how many seconds they
# would like to count down from. The input is then stored into a variable names seconds
# and then printed along with the statement, "seconds remaining".

# Importing time
import time

# Asking the user the amount of seconds they would like to count down from
second = int(input('How many seconds would you like to count down from?'))

# Setting up a for loop to count down
for index in range(second):
    print(str(second - index) + " seconds remaining")

    # Calling the sleep function to have the program sleep 1 second between each second
    time.sleep(1)


