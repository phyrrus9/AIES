## Josh Bosley - 2013:
## The purpose of this will be to go through saved computer data, and
## find similarities between cases scored similarly. Frequently used keywords,
## and check for relations in known information ( Brand\Model\Software\Hardware\
## past diagnosis\commonly occuring issues ) 
## The goal is to 'learn,' and assist in computer repair.

def CLS():
    import os
    try:
        os.system('cls')
    except:
        os.system('clear')
    return;

def GET_INPUT():
    while(1):
        VALID = ["YES","NO"]
        USER_INPUT = ""
        USER_INPUT = raw_input("\n $~: ");
        USER_INPUT = [item.upper() for item in USER_INPUT]
        USER_INPUT = "".join(USER_INPUT);
        if (USER_INPUT in VALID): return USER_INPUT;
        print (' Please enter yes or no. ')

def COMPUTER_INIT():
    import computerEntry
    CLS();
    print('''
        Will this be a computer previously worked on before by this system?
        \n''')
    while(1):
        UIN = GET_INPUT();
        if ( UIN == "NO" ): computerEntry.INITIATE_NEW();
        if ( UIN == "YES" ): computerEntry.INITIATE_OLD();
        MAIN();
    return;

def REPORT():
    print "report"
    ## enter name, check if exists then, FULL_FILE_ANALYSIS(NAME);
    return;


def MAIN():
    CLS();
    CMD = ["EXIT","START","REPORT"]
    print ('''Welcome ! What would you like to do? \n''')
    for X in range(len(CMD)):
        print CMD[X]
    while(1):
        IN = raw_input("\n $~: ");
        IN = IN.upper()
        if (IN == CMD[0]): exit()
        if (IN == CMD[1]): COMPUTER_INIT();
        if (IN == CMD[2]): REPORT();
    return;
MAIN();
