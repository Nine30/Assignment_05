#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# NSpellman, 2021-Aug-07, Modified File
# NSpellman, 2021-Aug-08, Modified File and Cleaned Up
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Loading existing data
        objFile = open(strFileName, 'r')   # open file
        for row in objFile:   # read the file into in-memory list
            lstRow = row.strip().split(',')
            dicRow = {'id': lstRow[0], 'album': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()  # close file
        print('Successfully loaded data.\n')  # verify to user the load has occurred
        pass
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'album': strTitle, 'artist': strArtist} # setting up as a dictionary data row
        lstTbl.append(dicRow) # appending new dictionary row to file
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, Album, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ') # unpack the values
        print()
        pass

            
    elif strChoice == 'd':
        # Deleting an entry
        print('Here is what we presently have:\n') # offer context to user
        print()
        for row in lstTbl:
            print(*row.values(), sep = ', ')  # print what is in the dictionary lists
        
        # Gather Input, Remove Chosen ID
        deleteEntry = input('\nWhich ID would you like to delete? ') # get input from user on which ID to remove
        for row in lstTbl:
            if row['id'] == deleteEntry: # search for this id
                del row['id']
                del row['album']
                del row['artist']
                print('\nDelete Successful!') # verify to user it was removed
            while {} in lstTbl:
                lstTbl.remove({}) # remove empty line left in the list

        # Load Remaining Dictionaries, Overwrite File
        print('Here is what we have now:\n') # offer context to user
        print('ID, Album, Artist')
        objFile = open(strFileName, 'w') # open file to overwrite with updates
        for row in lstTbl:
            strRow = ''    
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            print(*row.values(), sep = ', ') # unpack the remaining values in the file
            objFile.write(strRow) #overwriting
        objFile.close() # close file
        print('\nFile updated! No need to save again.') # verify to user
        print()
        pass
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')