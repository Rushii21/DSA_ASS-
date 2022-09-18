def accept_data(cricket,badminton,football):
    c1=int(input("Enter the no of students who play Cricket "))
    b1=int(input("Enter the no of students who paly Badminton "))
    f1=int(input("Enter the no of students who play Football "))

    print("The no students play Cricket =",c1)
    print("The no students play Badminton =",b1)
    print("The no students play Football =",f1)

    for i in range(c1):
        cricket.add(input("Name of students who play cricket "))

    for i in range(b1):
        badminton.add(input("Name of students who play badminton "))

    for i in range(f1):
        football.add(input("Name of student who play Football "))

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