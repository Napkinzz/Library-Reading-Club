########################################################################################
# ASSIGNMENT 1 
# LUKAS WASCHUK
# Goal: refresher of Python and hands-on experience with file input/output, built-in data 
# structures (especially dictionaries), and string manipulation. 
########################################################################################

def getDate(iteration):
    '''
    Asks the user for a date, iteration is used if the function is called a second time 
    and will print a different string for the user if it is not the first call. Checks 
    if the string enteres is a digit of length 8, then converts the string to integer 
    values and returns them.

    Para: 
            iteration: integer: 1 for first call of funtion
                              2 for subsequent calls

    Returns:
            year: Integer
            month: Integer 
            day: Integer 

    '''
    #some specific causes caused a error when date did not have a value, here is it arbitrary.
    date = "" 

    # if this is the first time the funtion is called it will prompt with a non-error message.
    if iteration == 1:
        date = input("Please enter the club's start date (YYYYMMDD): ")
    accept = False 
    
    while accept == False:
        if date.isdigit() == True and len(date) == 8:
            year = int(date[:4])
            month = int(date[4:6])
            day = int(date[6:8])
            accept = True 
        if accept == False:
            date = input("Invalid date entered. Please enter the club's start date (YYYYMMDD):")
        
    return year, month, day 

def checkYear(year):
    '''
    Deturmines if the integer entered is a leap year or not. 

    Para:
            year: Integer 

    Returns:
            isLeap: Boolean 

    '''
    if year % 4 == 0: 
        if year % 100 == 0 and year % 400 == 0:
            isLeap = True 
        elif year % 100 != 0: 
            isLeap = True 
        else: 
            isLeap = False
    else:
        isLeap = False 
    return isLeap

def checkMonth(month):
    '''
    Checks if the month is in the range of months. ie. 1 to 12.

    Para:   
            Month : Integer 

    Returns:
            Boolean


    '''
    if month in range(1, 13):
        return True 
    return False 

def checkDay(day, month, isLeap):
    '''
    Checks the day value entered and compares it against several checks to deturmine if the date is 
    acceptable. ie. Correct number of days in a given month and checked feb leap year. 

    Para:
            Day: Integer
            Month: Integer 
            isLeap: Boolean

    Returns:
            Boolean

    '''
    # months broken into lists corresponding with their maximum allowable days.
    days31 = [1, 3, 5, 7, 8, 10, 12]
    days30 = [4, 6, 9, 11]
    days28 = [2]

    # checks which list the input falls into and validates the value "day", an additional check is required 
    # for feb, as if the year entered is a leap year feb loses one day. 
    if month in days31:
        if day in range(1, 32):
            return True 
        else:
            return False 
    elif month in days30:
        if day in range(1, 31):
            return True 
        else:
            return False 
    elif month in days28:
        if isLeap == True:
            if day in range(1, 30):
                return True 
            else:
                return False 
        else:
            if day in range(1, 29):
                return True 
            else:
                return False 

def confirmDate(day, month, year):
    '''
    Uses the funtions checkYear(year), checkMonth(month) and checkDay(day, month, isLeap) to validate the 
    calendar date for any integer of length 8 given. 

    Para:
            Day: Integer
            Month: Integer 
            Year: Integer

    Returns: 
            Boolean
    '''
    isLeap = checkYear(year)
    confirmMonth = checkMonth(month)
    confirmDay = checkDay(day, month, isLeap)

    if confirmMonth == True and confirmDay == True:
        return True
    else:
        return False

def welcomeBanner():
    '''
    Welcome string that is printed upon the launch of the program.

    Para:
            None
    
    Returns:
            None
    '''
    print('************************************\n'+ \
          "WELCOME TO EPL's SUMMER READING CLUB\n"+ \
          '************************************')
    return 

def choicesString():
    '''
    Main menu string.

    Para:
            None
    
    Returns:
            None
    '''
    print('\nWhat would you like to do?\n' + \
          '1. Record a book that has been read.\n' + \
          '2. Generate a participant report.\n' + \
          '3. Summarize club activity.\n' + \
          '4. Quit')
    return 

def getChoice():
    '''
    Function to be called by main that fetchs a number value corresponding to the "Main Menu" string
    printed. Validates that it is acceptable. 

    Para:
            None

    Returns:
            Choice: Integer
    '''
    acceptableChoices = ['1', '2', '3', '4']
    choice = input()
    while choice not in acceptableChoices:
        print('Sorry, invalid entry. Please enter a choice from 1 to 4.')
        choice = input()

    return choice 

def openFile(fileName):
    '''
    Opens a text file from the same directory as the .py and returns a list.

    Para:
            fileName: String 
    
    Returns:
            fList: List
    '''
    with open(fileName) as f:
        fList = f.readlines()
    return fList

def stripWhiteSpace(person):
    '''
    Strips the white space and newline 
    characters from the paricipants list. Where: 
                                                person[0] = first name
                                                person[1] = last name
                                                person[2] = ID number
                                                person[3] = birthdate
    
    Para: 
            person: list

    Returns:
            person: list
    '''
    person[0] = person[0].strip()
    person[1] = person[1].strip()
    person[2] = person[2].strip()
    person[3] = person[3].strip("\n")
    person[3] = person[3].strip()
    return person

def participantDict(allParticipants):
    '''
    Converts the participant list into a dictionary with their ID as the [key] and 
    [firstname, lastname, birthdate] as values:
                                                person[0] = first name
                                                person[1] = last name
                                                person[2] = ID number
                                                person[3] = birthdate

    Para: 
            allParticipants: list

    Returns:
            partiDict: dictionary
    '''
    partiDict = {}
    for person in allParticipants:
        person = person.split(',')
        person = stripWhiteSpace(person)
        person[3] = fixDate(person[3])
        infoList = [person[0], person[1], person[3]]
        partiDict[person[2]] = infoList

    return partiDict

def fixDate(date):
    '''
    Converts the string value a participants birthdate into a string of numbers. ie. Feb == 02, 
    will also convert single digit values into double digit, ie 2 becomes 02. Will return a string 
    of the following format, 'YYYYMMDD'

    Para: 
            date: string

    Returns:
            date: string
    '''
    months = ['Jan', "Feb", 'Mar', \
            'Apr', 'May', 'Jun', \
            'Jul', 'Aug', 'Sep', \
            'Oct', 'Nov', 'Dec']

    date = date.split()
    date[0] = str(months.index(date[0]) + 1 )
    if len(date[0]) < 2:
        date[0] = '0' + str(date[0])

    if len(str(date[1])) < 2:
        date[1] = '0' + str(date[1])
    date = [date[2], date[0], date[1]]
    date = ' '.join(date)
    return date 

def validateLcn(lcn, poeple):
    '''
    "Validate Library Card Number" will check if the lcn matchs with a participant in the 
    participant dictionary. Returns True or False

    Para:
            lcn: string
            people: dictionary
    
    Returns:
            boolean
    '''
    if lcn in poeple:
        return True 
    else:
        return False

def option1(people):
    '''
    Option one of the main function. Will aquire a library card number (LCN) and validate it. Upon Validation 
    Will ask the user for a book name and a branch name. Once given LCN, book name, and branch the function will
    append (write) the information seperated by '#' to the end of the text file consisting of books read.

    Para:
            people: dictionary

    Returns:
            None
    '''
    lcn = input('Card number: ')
    while validateLcn(lcn, people) == False:
        lcn = input('Invalid library card number. Card number: ')
    book = input('Book title: ')
    branch = input('Library branch: ')
    
    with open('booksRead.txt', 'a') as f:
        f.write('\n')
        f.write(('{}#{}#{}').format(branch, lcn, book))
    print('Record added successfully.')
    return

def option2(people, levels, read, year, month, day, theme):
    '''
    Validates a given LCN and fetchs the birth date of the given participant. Given their birth date, computes
    their age. Then parses through books read dictionary using the LCN given and counts and prints the books 
    they read (while adding a * to the book name after the 23rd character in the book name). With the number 
    of books read, will assign a rank based off of clublevel.txt. Below are index's for easier readability /
    debugging.

           personKey = ID       bookKey = ID            levelKey = LEVEL NAME
           person[0] = FNAME    book[0] = BRANCH        level[0] = NAME
           person[1] = LNAME    book[1] = BOOK NAME     level[1] = RANK CUTOFF
           person[2] = DATE                             

    Para:   People: dictionary
            levels: dictionary
            read: dictionary
            year: integer 
            month: integer
            day: integer
            theme: string

    Returns:
            None
    '''
    lcn = input('Library Card Number: ')
    if validateLcn(lcn, people) == False:
        return print('Invalid library card number.')
    born = people[lcn][2]
    count = 0
    fName, lName = firstName(people[lcn][0]).upper(), lastName(people[lcn][1]).upper()
    age, currentDate = getAge(year, month, day, born), fixCurrentDate(year, month, day)
    print('\nReport for:    {:>8s} {}'.format(fName, lName))
    print('Age on {}:  {:>5}'.format(currentDate, age))
    print('-------------------------')
    print('Books read: ')

    if lcn in read:
        for value in read[lcn]:
            count += 1 
            if len(value[1]) > 23:
                value[1] = value[1][:23] + '*'
            print('-{}'.format(value[1]))

    # if there are no books in the dictionary given their ID
    else:
        print('None yet...')

    print('-------------------------')
    print('Total books read:   {:>5}'.format(count))
    rank = getRank(theme, count, levels).upper()
    print('Level:       {:>12s}'.format(rank))
    print('-------------------------')
    return 

def getRank(theme, count, levels):
    '''
    Given the number of books a participant read, parses through the level dictionary (where the key is 
    the specific theme) If the number of books read is greater then the max rank, it assigns the max rank.
    Parses through all rank cutoffs using if booksread < rank cutoff, rank = LEVELNAME 
    Below are index's for easier readability debugging.

    levelKey = LEVELNAME
    level[0] = NAME
    level[1] = RANK CUTOFF

    Para:
            Theme: String
            Count: Integer
            Levels: Dictionary

    Returns:
            None
    '''
    if count >= int(levels[theme][-1][1]):
        rank = levels[theme][-1][0]
        return rank
    else:
        for level in levels[theme]:
            if count < int(level[1]):
                rank = level[0]
                return rank 
    
def fixCurrentDate(year, month, day):
    '''
    Converts the current date into the acceptable string layout. ie YYYY MM DD. Will change single digit 
    strings to double digit. ie. 6 becomes 06, for both the month and day.

    Para:
            year: integer
            month: integer
            day: integer

    Returns:
            string: string
    '''
    year = str(year)
    month = str(month)
    day = str(day)
    if len(month) < 2:
        month = '0' + str(month)
    if len(day) < 2:
        day = '0' + str(day)    
    string = ' '.join([year, month, day])
    return string

def getAge(year, month, day, born):
    '''
    Calculates the participants age relative to the entered date using: 
    year - birthyear - 1 (if the current month / day is less then birth month / day) or 
    year - birthyear - 0 (if the current month / day is greater then birth month / day)

    Para:
            year: integer
            month: integer
            day: integer
            born: string

    Returns:
            age: integer    
    '''
    born = born.split()
    bornYear = int(born[0])
    bornMonth = int(born[1])
    bornDay = int(born[2])
    age = year - bornYear - ((month, day) < (bornMonth, bornDay))
    return age
  
def firstName(string):
    '''
    If a participants first name is larger then 8 characters long, will cut it off at 7 characters long plus 
    a asterisk. ie  ARCHIBALD becomes ARCHIBA*.

    Para:
            string: string

    Returns:
            string: string
    '''
    if len(string) > 8:
        string = string[:7] + '*'
    return string 

def lastName(string):
    ''' 
    Given a last name, returns the first letter of the last name

    Para:
            string: string

    Returns:    
            string: string 

    '''
    string = string[0]
    return string

def levelDict(levels):
    '''
    Converts the clublevel list into a dictionary with LEVELNAME as the key, with the RANKNAME and the rank 
    cutoff as the value. 
    Below are index's for easier readability debugging.

            level[0] = LEVELNAME
            level[1] = NAME
            level[2] = RANK CUTOFF

    Para:
            levels: list
    
    Returns:
            levdict: dictionary
    '''
    levDict = {} 
    for line in levels:
        line = line.split(':')
        line[2] = line[2].strip("\n")

        # if the key is not in the dictionary, will create a key, if it exists in dictionary, will add to the 
        # existing key.
        if line[0] not in levDict:
            levDict[line[0]] = [[line[1], line[2]]]
        else:
            levDict[line[0]].append([line[1], line[2]])

    return levDict

def bookDict(booksRead):
    '''
    Converts the booksread list into a dictionary with ID as the key, and BRANCH, BOOKNAME as values.
    Below are index's for easier readability / debugging.

        book[0] = BRANCH  
        book[1] = ID 
        book[2] = BOOK NAME 

    Para: 
            booksRead: List
    
    Returns:
            boDict: dictionary 
    '''
    boDict = {}
    for book in booksRead:
        book = book.split('#') 
        book[2] = book[2].strip('\n')

        # if the key is not in the dictionary, will create a key, if it exists in dictionary, will add to the 
        # existing key.
        if book[1] not in boDict:
            boDict[book[1]] = [[book[0], book[2]]]
        else:
            boDict[book[1]].append([book[0], book[2]])


    return boDict

def chooseLevel(levels):
    '''
    Given the levels dictionary, will parse through the key values (THEMES) and print them for the user to 
    select from. The user will then choose one of the printed themes for the session. Will check to see 
    if the chosen theme (the one the user entered) is valid.

    Para:
            levels: dictionary
    
    Returns:
            theme: string
    '''
    print('\nThemes to select from:')
    for key, value in levels.items():
        print('- {}'.format(key))
    theme = input('Please pick a theme from the list above: ')
    while theme not in levels:
        theme = input('Invalid entry. Please pick a theme from the list above: ')

    return theme

def option3(people, read, year, month, day):
    '''
    With values given by functions createAgeGroups() and topRead() (functions that split participants into age groups and 
    returns the highest rank per age group) prints all the data into a formated UI / box for the user to read from. 

    Para: 
            people: dictionary
            read: dictionary
            year: integer
            month: integer
            day: integer

    Returns:
            None

    '''
    fiveU, sixToNine, tenO = createAgeGroups(people, read, year, month, day)
    winner5, total5 = topRead(fiveU, read)
    winner9, total9 = topRead(sixToNine, read)
    winner13, total13 = topRead(tenO, read)

    print('+=============+==================+============+')
    print('|  Age Group  | Total Books Read | Top Reader |')
    print('+=============+==================+============+')
    print('| 5 and under |        {:<10}| {:<8}   |'.format(total5, winner5))
    print('|         6-9 |        {:<10}| {:<8}   |'.format(total9, winner9))
    print('|       10-13 |        {:<10}| {:<8}   |'.format(total13, winner13))
    print('+=============+==================+============+')

    return 

def topRead(bracket, read):
    '''
    For each participant in a given age bracket, calulates the participant who read the most number of books, checks if there is
    a tie, and if no participants read any books returns N/A. returns the topReader (winner), and the TOTAL number of books 
    the age bracket read. Primarily used in the option 3 funtion. Whenever a new "best" reader is assigned its first name and 
    last name are placed into the firstName() and lastName() functions to properly format them. 
    Below are index's for easier readability / debugging.

    bracket[lcn][0] = FIRSTNAME
    bracket[lcn][1] = LASTNAME

    Para:
            bracket: dictionary
            read: dictionary

    Returns:
            topReader: string
            bracketCount: integer 
    '''
    bracketCount = 0
    topReader = 'N/A'
    
    record = 0 
    for lcn in bracket:
        personalCount = 0 

        # if KEYERROR occurs the dictionary was empty ie, there was not a participant who read any books this summer.
        # we do not care about the specific book that was read, only the tally for the total books read
        try:
            for book in read[lcn]: 
                personalCount += 1
                bracketCount += 1 
            if personalCount > record:
                record = personalCount
                topReader = ' '.join([firstName(bracket[lcn][0]), lastName(bracket[lcn][1])])
            elif personalCount == record:
                topReader = 'Tied!'
        except KeyError:
            topReader, bracketCount = 'N/A', 0
    return topReader, bracketCount

def createAgeGroups(people, read, year, month, day):
    '''
    Parses through the participants dictionary and sort the participants into sub dictionaries by to their age relative to the
    entered date. Uses the getAge() function to get the age, then sorts the participants into the respective dictionaries
    Below are index's for easier readability debugging.

           peopleKey = ID                   fiveU = dictionary for participants from 1 to 5 years old.
           people[0] = FNAME                sixToNine = dictionary for participants from 6 to 9 years old.
           people[1] = LNAME                tenO = dictionary for participants from 10 to 13 years old.
           people[2] = DATE 

    Para: 
            people: dictionary
            read: dictionary
            year: integer
            month: integer
            day: integer

    Returns:
            fiveU: dictionary
            sixToNine: dictionary
            tenO: dictionary
    '''
    fiveU, sixToNine, tenO = {}, {}, {}
    for key in people:
        age = getAge(year, month, day, people[key][2])
        if age <= 5:
            fiveU[key] = [people[key][0], people[key][1]]
        elif age <= 9:
             sixToNine[key] = [people[key][0], people[key][1]]
        elif age <= 13:
            tenO[key] = [people[key][0], people[key][1]]

    return fiveU, sixToNine, tenO

def main():
    '''
    Main function that sets the variables, opens the files, creates the dictionaries needed to run the program. Asks the user 
    for the date, theme and the option they want to do. 

    Para:
            None
    
    Returns: 
            None

    '''
    welcomeBanner()
    year, month, day = getDate(1)
    while confirmDate(day, month, year) == False:
        year, month, day = getDate(2)
    levels = levelDict(openFile('clubLevels.txt'))
    theme = chooseLevel(levels)

    quit = False
    while not quit:
        people = participantDict(openFile('participants.txt'))
        
        read = bookDict(openFile('booksRead.txt'))
        choicesString()
        choice = getChoice()

        if choice == '1':
            option1(people)
        elif choice == '2':
            option2(people, levels, read, year, month, day, theme)
        elif choice == '3':
            option3(people, read, year, month, day) 
        elif choice == '4':
            quit = True 
            print('Goodbye')
    return

if __name__ == '__main__':
    main()