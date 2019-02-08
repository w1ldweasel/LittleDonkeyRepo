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
    # run out of time, will update this in next version!


def isvaliddate(d):
    import datetime
    try:
        datetime.datetime.strptime(d, '%d/%m/%Y')
    except:
        return False
    else:
        return True


def sayhi(myname):
    dob = ""
    # validate date string in dob
    while not isvaliddate(dob):
        dob = input("\nHello " + myname + ". \n Impart your sensitive personal"
                    " details here so i can destroy your credit rating with a "
                    "£6000 spending spree on frozen tiramisu's at Iceland."
                    " \n What is your DoB? (dd/mm/yyyy):\n")

    userage = getagefromdate(dob)
    print("\n Oh i'm surprised, you are " + str(userage) + ", you don't look a"
          " day over " + str((userage + 15)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        n = input("\n*tut* dont you even know how to pass positional "
                  "arguments to script parameters you unconscionable "
                  "ignoramus? \n Now enter your name here: \n")
        sayhi(n)
    else:
        sayhi(sys.argv[1])