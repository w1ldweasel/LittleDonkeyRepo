# /usr/bin/python3
def getagefromdate(d):
    import datetime
    today = datetime.date.today()
    dob = datetime.datetime.strptime(d, '%d/%m/%Y')
    """ this next bit works because comparison of tuples works in order
    comparing firsttuple[1] to secondtuple[1], if false (0), then,
    compares firsttuple[2] to secondtuple[2], until it evaluates
    to true (1) or comes to the end """
    return today.year - dob.year - ((today.month, today.day) <
                                    (dob.month, dob.day))


def itsyourbirthday(d):
    # this function returns true if d is the users birthday
    import datetime
    today = datetime.date.today()
    dob = datetime.datetime.strptime(d, '%d/%m/%Y')
    if today.month == dob.month and today.day == dob.day:
        return True
    else:
        return False


def isvaliddate(d):
    import datetime
    try:
        datetime.datetime.strptime(d, '%d/%m/%Y')
    except:
        return False
    else:
        return True


def sayhi(myname):
    print("Hello " + myname)


def getdateofbirth():
    dob = ""
    i = 0
    # validate date string in dob
    while not isvaliddate(dob):
        if i == 0:
            dob = input("\nImpart your sensitive details here "
                        "so i can destroy your credit rating "
                        "on frozen tiramisu's from Iceland."
                        "\nWhat is your DoB? (dd/mm/yyyy):\n")
        else:
            dob = input("\n**Tut** - try again with a valid date.")
        i += 1
    return dob

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        n = input("\n*tut* dont you even know how to pass positional "
                  "arguments to script parameters you unconscionable "
                  "ignoramus? \n Now enter your name here: \n")
        sayhi(n)
    else:
        sayhi(sys.argv[1])
    # ask the user for their date of birth
    dob = getdateofbirth()
    # calculate their age as of today
    userage = getagefromdate(dob)
    print("\nOh i'm surprised, you are " + str(userage) + ", you don't look a"
          " day over " + str((userage + 15)))
    # check if it's the users birthday
    bday = itsyourbirthday(dob)
    if bday:
        print("Happy " + str(userage) + " Birthday!")
