# Used to clear the screen. :D 
def CLS():
    import os
    try:
        os.system('cls')
    except:
        os.system('clear')
    return;


# Check input for valid input, and handle accordingly.
def GET_INPUT():
    while(1):
        VALID = ["EXIT","YES","NO"]
        USER_INPUT = ""
        USER_INPUT = raw_input(" \n $~: ");
        USER_INPUT = [item.upper() for item in USER_INPUT]
        USER_INPUT = "".join(USER_INPUT);
        if (USER_INPUT in VALID):
            if (USER_INPUT == VALID[0]):exit()
            if (USER_INPUT == VALID[1]):return True;
            if (USER_INPUT == VALID[2]):return False;
        print (''' Please enter a valid command /n
                    %s''' %VALID)
    return;

# Checks to see if a file exists. Since we don't want the file to
# overwritten, return false. 
def EXIST_CHECK_NEW(NAME):
    import os
    if ( os.path.isfile('local\shop\%s' %NAME) ): return False
    return True;

# Not the case here. So is reverse. 
def EXIST_CHECK_OLD(NAME):
    import os
    if ( NAME.upper() == "EXIT"): exit()  
    if ( os.path.isfile('local\shop\%s' %NAME) ): return True
    return False;

# Loadfile Info from shop. 
def LOAD_INFO(NAME):
    FILE = ('local\shop\%s' %NAME)
    with open(FILE) as inf:
        INFO = inf.readlines()
    inf.close()
    return INFO;

# Handles finding, and editing already entered computer
# data. 
def INITIATE_OLD():
    import os
    import moduleNest
    CLS();
    
    print (''' \n
    Please enter the name of the computer to access
    it's file. If you are unsure of file name, press
    enter to view a list of files available .\n\n ''')

    while(1):
        IN = raw_input(' \n $~: ');
        A = EXIST_CHECK_OLD(IN);
        if ( A == True ):
            print (''' \n File found, loading..  ''')
            INFO = LOAD_INFO(IN)
            break
        if ( A == False ):
            print (''' \n The filename ` %s ` was not found. ''' %IN)
            print (" \n Valid/Existing files: \n")
            for dirname, dirnames, filenames in os.walk('local\shop'):
                for filename in filenames:
                    print os.path.join(filename)
    CLS();
    
    # Check one last time to see if it is the correct.
    # Ask about new issues. Do some data spiffing. 
    print('''\n File loaded contains this information: \n\n''')
    for i in range(len(INFO)):
        print INFO[i]
    print ('''\n Is this the correct file ? ''')
    IN = GET_INPUT();
    if ( IN == True ):
        CLS();
        INFO[0] = (INFO[0].translate(None, '\n'))
        INFO[0] = (INFO[0].translate(None, ' '))
        CURRFILE = ('local\shop\%s' %INFO[0])
        
        print(''' \n " %s " \n
             was the last recorded issue. \n ''' %INFO[-1])
        print(''' \n\n What seems to be the issue with %s today ?''' %INFO[0])
        while(1):
            INPUT = raw_input(" \n $~: ");
            CLS();
            print('''\n %s \n
                    Is this this your final description of
                    the issue at hand? (yes/no) \n\n''' %INPUT)
            ANSWER = GET_INPUT();
            CLS();
            # write out updated entry to file and rebuild
            # the INFO list. Then Look at the data. 
            if ( ANSWER == True ):
                INFO[-1] = INPUT
                F = open(CURRFILE,'w')
                for x in range(len(INFO)):
                    F.write('''%s\n''' %INFO[x])
                F.close()
                moduleNest.CALCULATE_SCORES(INFO);
                break
            if ( ANSWER == False ): break
    if ( IN == False): INITIATE_OLD();
    moduleNest.FULL_FILE_ANALYSIS(INFO[0]);
    return;

# Ran when entering new computer information. 
def INITIATE_NEW():
    import moduleNest
    QUESTIONS = ["Current operating system :",
                 "Current antivirus : ",
                 "Year of purchase : ",
                 "Brand : ",
                 "Model : "]
    RESPONSE_LIST = []
    CLS();
    # Get computer name :
    while(1):
        print (''' Please enter a valid name: ''')
        IN = raw_input('\n $~: ');
        A = EXIST_CHECK_NEW(IN);
        if ( A == True ):
            RESPONSE_LIST.append(IN)
            CLS();
            break
        CLS();
        print ('''%s exists. Please type another name,
                        or type `exit`.\n\n''' %IN)
        
    # Get computer information : 
    for i in range(len(QUESTIONS)):
        print QUESTIONS[int(i)]
        IN = raw_input('\n $~: ');
        RESPONSE_LIST.append(IN);
        print ('\n')
        
    # Ask for a description of the computer, and problems it is having. 
    while(1):
        CLS();
        print ('''\n
                Please enter a detailed description of the issue you are
                having with %s\n
                Also include any apparent physical
                damage. The more detailed the report, the more accurate
                this system will be.\n ''' %RESPONSE_LIST[0])
        IN = raw_input('\n $~: ');
        CLS();
        print ('''\n\n%s\n\n
        Is this the description of %s you would like to submit? \n ''') %(IN, RESPONSE_LIST[0])
        
        INA = GET_INPUT();
        if ( INA == True):
            RESPONSE_LIST.append(IN);
            # Save it to file
            NAME = ('local\shop\%s' %RESPONSE_LIST[0])
            F = open(NAME,'w')
            for x in range(len(RESPONSE_LIST)):
                F.write('''%s\n''' %RESPONSE_LIST[x])
            F.close()

            # Send the info on along to getdata.
            # Could use RESPONSE_LIST, but this
            # way we are sure we are getting all
            # the data.
            CLS();
            INFO = LOAD_INFO(RESPONSE_LIST[0]);
            moduleNest.CALCULATE_SCORES(INFO);
            moduleNest.FULL_FILE_ANALYSIS(INFO[0]);
            break
        
    return;













