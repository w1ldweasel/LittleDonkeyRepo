# /usr/bin/python3

def sayhi(myname):
    print("Hello World")
    print("Hello " + myname)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("include your name as an arguement you prick")
    else:
        sayhi(sys.argv[1])