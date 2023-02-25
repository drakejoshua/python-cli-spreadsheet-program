# display a welcome statement showing the name of the program and other info
print("This is the python spreadsheet program built by joshua mabawonku")

# displaying some indentation between the welcome statement and spreadsheet table
print("\n ")


# this function below is used to find the maximum column length in the table's data
# it accepts a list of all the table's value and then, returns the max col length
def findMaxColLength( values ):
    # variable declaration for this function
    maxColumnLength = 0

    # calculating the max col length
    for value in values:
        if len( value ) > maxColumnLength:
            maxColumnLength = len( value )
    
    # return the max col length
    return maxColumnLength



# this function displays the spreadsheet table with the current table data
def displaySpreadsheetTable():
    # global variable declaration for this function
    # the lineString variable which is used to contain all the characters that are to be
    # displayed on one line at a time
    lineString = "    s/n |"
    rowNumber = 0

    # to display the spreadsheet table, we firstly have to display the table headings gotten directly as keys
    # of the dictionary for table data
    for heading in tableData.keys():
        lineString = lineString + " " + heading + " |"

    # print the table headings as generated
    print( lineString )

    # generating and printing the table data line by line until there's none
    # this is done using values gotten directly from the dictionary for the table data
    tableDataValues = tableData.values()

    # finding the highest column length in the table data
    maxColumnLength = findMaxColLength( tableDataValues )

    while rowNumber <= ( maxColumnLength - 1 ):
        # erasing the content of lineString in order to print new content( table row ) on another line
        # also putting the new content( table row ) in it in preparation for 
        lineString = ""
        
        # removing some spaces in order to allow correct alignment and tabulation when the row number is
        # greater than 10
        if rowNumber >= 9:
            lineString = lineString + "     " + str( rowNumber + 1 ) + " |"
        else:
            lineString = lineString + "      " + str( rowNumber + 1 ) + " |"

        # putting the table row for this line into the lineString and then displaying them to the user
        for value in tableDataValues:
            if rowNumber < len( value ):
                lineString = lineString + " " + str( value[rowNumber] ) + " |"
            else:
                lineString = lineString + " " + " " + " |"

        # incrementing the value of rowNumber by 1 in order to allow the generation of a new table row
        # and also prevent an infinite loop
        rowNumber = rowNumber + 1

        # printing the value of the lineString in order to display the generated table row to the user
        print( lineString )



# this function updates all the empty spaces in the spreadsheet table with ""
def updateEmptySpacesInTheTable():
    # variable declaration for this function
    tableDataValues = tableData.values()
    maxColumnLength = findMaxColLength( tableDataValues )
    tableDataHeadings = tableData.keys()

    # update the empty spaces by looking through each key and it's corresponding
    # values, calculating the difference in length ( same as number of empty spaces ) 
    # and then adding the appropriate number of spaces
    for key in tableDataHeadings:
        differenceInLength = maxColumnLength - len( tableData[key] )

        # inserting the spaces using this count-controlled dumb loop
        for i in range( differenceInLength ):
            tableData[key].append(" ")



# this function is used to assign values to a given & valid cell address
def assignValueToCellAddress( cellAddress, valueToAssign ):
    rowNumber = int( re.findall( "[A-Z](\d+)", cellAddress )[0] )
    columnLetter = re.findall( "([A-Z])\d+", cellAddress )[0]

    tableData[columnLetter][ ( rowNumber - 1 ) ] = valueToAssign


# more stuff to do on startup

# the global data for the program
defaultTableHeadings = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J" ]
tableData = dict()
userWantToContinue = "YES"

# adding data to the tableData based on the tableHeadings
for heading in defaultTableHeadings :
    tableData[heading] = [ " ", " ", " ", " ", " ", " " ]



# the program/software loop, always running as far as the user wants to continue with the program
while userWantToContinue == "YES":
    # display and update empty spaces in the spreadsheet table
    updateEmptySpacesInTheTable()
    displaySpreadsheetTable()

    # prompting the user for the action to take
    userAction = input("what do you want to do: ( ANC = add new column, ANR = add new row, input a cell address( e.g. A1 ) to assign content to that cell )  ")

    # taking the appropriate action based on the action selected by the user
    if userAction == "ANC":
        # user wants to add new column to the tableData

        # checking the value of the last column in the tableData against the list of 
        # supported column name and adding a new column based on the check
        # then updating and displaying the spreadsheet table
        listOfSupportedColumnName = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                                      "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
        tableData[ listOfSupportedColumnName[ len( tableData.keys() ) ] ] = [ " ", " ", " ", " ", " " ]
        updateEmptySpacesInTheTable()

    elif userAction == "ANR":
        # user wants to add new row to the tableData

        # looping through all the headings( keys ) of the table data and then
        # adding empty spaces( to represent a new cell for that row )
        for key in tableData.keys():
            tableData[key].append(" ")

        # displaying and updating the spreadsheet table
        updateEmptySpacesInTheTable()
    
    else:
        # user wants to assign a value to a cell using it's address

        # importing the regexp lib to do this and some variable declaration
        import re
        keyFound = False

        # checking if the user entered a correct cell address or bad input
        # then, extracting and validating the row-numbers and column-letters of
        # the entered cell address. then, prompt the user to input the value to be assigned to the
        # cell address and then, assign the inputted value to the cell address
        result = re.findall( "[A-Z]\d+", userAction )

        if result == []:
            print("invalid cell address / input entered ... try again")
        else:
            # validating the column-letter
            result = re.findall( "([A-Z])\d+", userAction )
            
            for key in tableData.keys():
                if key == result[0]:
                    keyFound = True
            
            if keyFound == True:
                # validating the row number
                result = re.findall( "[A-Z](\d+)", userAction )

                maxColumnLength = findMaxColLength( tableData.values() )

                if int( result[0] ) > maxColumnLength:
                    print("invalid row number found in cell address. please check and try again")
                else:
                    # since both info were valid, prompt for a value to assign and assign that value to the
                    # cell address
                    valueToAssign = input("Enter the value you want to assign to this cell   ")

                    assignValueToCellAddress( userAction, valueToAssign )
            else:
                print("invalid column letter found in cell address. please check and try again")


        
    # prompt the user asking if they still want to continue using the program or not in order to stop the loop
    userWantToContinue = input("Do you still want to continue using the program?, type YES to continue  ")


