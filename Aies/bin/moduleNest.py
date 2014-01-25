
# Check the existence of a file:
def DOESNT_EXIST(FILE):
    import os
    if ( os.path.isfile(FILE) ): return False
    return True;

# Print info report to file, and time stamp.
def PRINT_INFO(INFO, HSCORE, VSCORE, TPSCR, CURRFILE):
    import datetime
    STAMP = datetime.datetime.now()
    OUTTXT = ('''
    # # # [%s] # # #\n\nMachine: %s \nInput given: %s \nHSCORE : %s \nVSCORE : %s \nInput Diagnosis : %s \n
                # # # [ END ] # # # \n \n \n''') % (STAMP, INFO[0], INFO[-1], HSCORE, VSCORE, TPSCR)
    with open(CURRFILE, 'a+') as FX:
        FX.write(OUTTXT)

    return;

# Writes to file the tagged words that set TPSCR
def WRITE_COMPAIR(FILE, TAGGED):
    DE = DOESNT_EXIST(FILE);
    # if it doesnt exist, then we need to make a new one. 
    if ( DE == True ):
        with open(FILE, 'w') as FLOUT:
            for VAR in range(len(TAGGED)):
                FLOUT.write(TAGGED[VAR])
                FLOUT.write("\n")
        FLOUT.close()
    return;
    # If it exists, append it. 
    if ( DE == False ):
        with open(FILE, 'a+') as FLOUT:
            for VAR in range(len(TAGGED)):
                if (TAGGED[VAR] not in FLOUT):
                    FLOUT.write(TAGGED[VAR])
                FLOUT.write("\n")
        FLOUT.close()
    return;

# Retreive all recorded scores for that specific machine:
def RETRIEVE_SCORES(FILE):
    if DOESNT_EXIST(FILE): return;
    # Make some lists to store data, and for searching.
    # Then search the file for the strings. 
    SCORES = ["HSCORE","VSCORE"]
    HLST = []
    VLST = []
    HSCORE = []
    VSCORE = []
    for X in range(len(SCORES)):
        for Y in open(FILE):
            if SCORES[X] in Y:
                if ( X == 0): HLST.append(Y)
                if ( X == 1): VLST.append(Y)
    # Take the scores, and append them to 
    # their respective list as a Decimal.
    from decimal import Decimal
    for Z in range(len(HLST)):
        H = (HLST[Z].split(" : "))
        HSCORE.append(Decimal(H[1].translate(None, '\n')))
    for J in range(len(VLST)):
        V = (VLST[J].split(" : "))
        VSCORE.append(Decimal(V[1].translate(None, '\n')))
    # Return them as nicely packaged lists.
    return HSCORE, VSCORE;

def RETRIEVE_INPUTS(FILE):
    if DOESNT_EXIST(FILE): return;
    # Sort through config file, grap all the recoreded
    # issues, and send them in a nicely packaged list
    # back to whence they were called.
    KEY = ('Input given: ')
    LST = []
    INLST = []
    for X in open(FILE):
        if KEY in X: INLST.append(X)
    for Y in range(len(INLST)):
        IN = (INLST[Y].split(':'))
        LST.append(IN[1].translate(None, '\n'))
    return LST;

def CALCULATE_SCORES(INFO):
    import re
    VSCORE = 0.0
    HSCORE = 0.0
    # Switch to upper, and split in to words
    # void of \n for compairison
    IN = INFO[-1]
    IN = IN.upper()
    IN = re.sub("[^\w]", " ",  IN).split()
    INFO[0] = (INFO[0].translate(None, '\n'))
    CURRFILE = ('local\config\%s' %INFO[0])
    HW_FILE = ('local\data\HPKW') # Hardware Related
    VR_FILE = ('local\data\VPKW') # Virus Relate
    VW_FILE = ('local\data\VWLD') # Could be either
    TAGGED = []
    FILE = " "
    GRBSIZE = True
    SIZES = []
    # Range 1-4; this will cycle through the 3 compairson files
    for I in range(1,4):
        # Initiate the files based on loop. 
        if ( I == 1 ): FILE = HW_FILE
        if ( I == 2 ): FILE = VR_FILE
        if ( I == 3 ): FILE = VW_FILE
        # Calculate word weight score
        # and fill SIZES, which keeps track of file length
        W_SIZE = 0
        for CNT in range(1,4):
            if ( CNT == 1 ): AFILE = HW_FILE
            if ( CNT == 2 ): AFILE = VR_FILE
            if ( CNT == 3 ): AFILE = VW_FILE
            with open(AFILE) as z:
                for SIZE, k in enumerate(z):
                    pass
            if ( GRBSIZE == True ):
                SIZES.append(SIZE)
            W_SIZE += SIZE
        GRBSIZE = False
        W_SCORE = (1.0/W_SIZE)
        # Build LST with contents of FILE
        with open(FILE) as inf:
            LST = inf.readlines()
        for T in range(len(LST)):
            LST[T] = (LST[T].translate(None, '\n'))
        # Add weights to overall score.
        # Cut the pie for uncertainty
        # Store tagged words. Unless they
        # are already tagged.
        for D in range(len(SIZES)):
            for J in range(len(LST)):
                for ZED in range(len(IN)):
                    if (I == 1) and (LST[J] == IN[ZED]):
                        HSCORE += W_SCORE
                        if LST[J] not in TAGGED:
                            TAGGED.append(LST[J])
                    if (I == 2) and (LST[J] == IN[ZED]):
                        VSCORE += W_SCORE
                        if LST[J] not in TAGGED:
                            TAGGED.append(LST[J])
                    if (I == 3) and (LST[J] == IN[ZED]):
                        PIE = (W_SCORE/2)
                        HSCORE += PIE
                        VSCORE += PIE
                        if LST[J] not in TAGGED:
                            TAGGED.append(LST[J])           
    # Set TPSCR accordingly. 
    if ( HSCORE > VSCORE ): TPSCR = "Hardware"
    if ( HSCORE < VSCORE ): TPSCR = "Software/Virus"
    if ( HSCORE == VSCORE ): TPSCR= "Tied Score"

    # Begin setting tagged words, then write_compair the data
    TEMP = INFO
    for TMP in range(len(TEMP)):
        TEMP[TMP] = (TEMP[TMP].translate(None, '\n'))
        TEMP[TMP] = (TEMP[TMP].upper())
    TEMP = [i for i in TEMP if i != ' ']
    AVUP = TEMP[2]
    BRUP = TEMP[4]
    OSUP = TEMP[1]
    AVFILE = ('local\data\stored\AV\%r ' %AVUP)
    BRNDFL = ('local\data\stored\BRND\%r ' %BRUP)
    OSFLE = ('local\data\stored\OS\%r ' %OSUP)
    # Report Tagged words to AV/OS/BRND listings 
    if (TPSCR == "Hardware"):
        FILE = BRNDFL
        WRITE_COMPAIR(FILE, TAGGED);
    else:
        FILE = AVFILE
        WRITE_COMPAIR(FILE, TAGGED);
        FILE = OSFLE
        WRITE_COMPAIR(FILE, TAGGED);
    PRINT_INFO(INFO, HSCORE, VSCORE, TPSCR, CURRFILE);
    return;

def FULL_FILE_ANALYSIS(NAME):
    FILE = ('local/config/%s' %NAME)
    if DOESNT_EXIST(FILE): return;
    HLST, VLST = RETRIEVE_SCORES(FILE);
    REPORTS = RETRIEVE_INPUTS(FILE);
    HSCORE = HLST[0]
    VSCORE = VLST[0]
    for X in range(len(HLST)): HSCORE = (HLST[X] + HSCORE)
    for Y in range(len(VLST)): VSCORE = (VLST[Y] + VSCORE)

    print (''' %s 's Report Information . 
            \n Overall HSCORE was : %s
            \n Overall VSCORE was : %s
            \n Last known issues  :
            %s
            \n
            ''') % (NAME, HSCORE, VSCORE, REPORTS[-1])
    if ( HLST[-1] > VLST[-1] ): print (''' The last issue was determined to be a hardware issue. ''')
    if ( VLST[-1] > HLST[-1] ): print (''' The last issue was determined to be a Software/Virus issue. ''') 
    if ( HLST[-1] == VLST[-1]): print (''' The last issue was undetermied.''')
    
    pse = raw_input(" Press any key to continue " );
    ############################################################################################


    #                       HERE I WILL ADD CODE TO GO THROUGH ALL EXISTING FILES, AND
    #                       FIND OUT WHICH OTHER PROBLEMS IN THE PAST ARE 'SIMILAR' TO THIS CURRENT
    #                       ISSUE.


    ############################################################################################



    return;
















