log_file = open("um-server-01.txt") 
    # This line of code is opening the .txt file and assigning it to a varaiable in order to give the .py file access to the data.


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

    # Line 5 is declaring a function called sales_reports that takes in one parameter, the variable declared in line 1.
    # Line 6 begins a for loop to go over the data.
    # line 7 takes the variable, line, declared in the for loop and assigns it the value of an individual row of data without trailing spaces.
    # Line 8 creates a new variable called day and assigns it the value of the position range from 1-3 of each row.
    # Line 9 starts an if statement the evaluate whether or not the value of the day variable is equal to a Tue.
    # Line 10 console logs the row of line where the condition of day = Tue is true. (Changed to Monday)


sales_reports(log_file)
    # Line 20 calls the function and passes in the parameter of the data from the txt file. 
