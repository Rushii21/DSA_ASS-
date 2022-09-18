def accept_data(cricket,badminton,football):
    c1=int(input("Enter the no of students for Cricket "))
    b1=int(input("Enter the no of students for Badminton "))
    f1=int(input("Enter the no of students for Football "))

    print("The no students for Cricket =",c1)
    print("The no students for Badminton =",b1)
    print("The no students for Football =",f1)

    for i in range(c1):
        name=input("Enter name for cricket ")
        cricket.add(name)

    for i in range(b1):
        name=input("Enter name for badminton ")
        badminton.add(name)

    for i in range(f1):
        name=input("Enter name for Football ")
        football.add(name)

    print("Name of the students for Cricket ",cricket)
    print("Name of the students for Badminton ",badminton)
    print("Name of the students for Football ",football)

def cricket_and_badminton(cricket,badminton):
    play=set()
    for i in cricket:
        if i in badminton:
            play.add(i)
    print("The students who play both Criket and badminton",play)
    

def main():
    cricket=set()
    badminton=set()
    football=set()
    accept_data(cricket,badminton,football)
    cricket_and_badminton(cricket,badminton)
main()
