# Contents of datamanip's ' SCORES ' 
def LOOK_AT_DATA(INFO):
    import re
    import datetime
    VSCORE = 0.0
    HSCORE = 0.0
    IN = INFO[-1]
    IN = IN.upper()
    IN = re.sub("[^\w]", " ",  IN).split()
    INFO[0] = (INFO[0].translate(None, '\n'))
    CURRFILE = ('config\%s' %INFO[0])
    HW_FILE = ('HPKW')
    VR_FILE = ('VPKW')
    VW_FILE = ('VWLD')
    FILE = " "
    GRBSIZE = True
    SIZES = []
    for I in range(1,4):
        if ( I == 1 ): FILE = HW_FILE
        if ( I == 2 ): FILE = VR_FILE
        if ( I == 3 ): FILE = VW_FILE
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
        with open(FILE) as inf:
            LST = inf.readlines()
        for T in range(len(LST)):
            LST[T] = (LST[T].translate(None, '\n'))
        for D in range(len(SIZES)):
            for J in range(len(LST)):
                for ZED in range(len(IN)):
                    if (I == 1) and (LST[J] == IN[ZED]): HSCORE += W_SCORE
                    if (I == 2) and (LST[J] == IN[ZED]): VSCORE += W_SCORE
                    if (I == 3) and (LST[J] == IN[ZED]):
                        PIE = (W_SCORE/2)
                        HSCORE += PIE
                        VSCORE += PIE
    if ( HSCORE > VSCORE ): TPSCR = "Hardware"
    if ( HSCORE < VSCORE ): TPSCR = "Software/Virus"
    if ( HSCORE == VSCORE ): TPSCR= "Tied Score"
    STAMP = datetime.datetime.now()
    OUTTXT = ('''
    # # # [%s] # # #\n\nMachine: %s \nInput given: %s \nHSCORE : %s \nVSCORE : %s \nInput Diagnosis : %s\n
                # # # [ END ] # # # \n \n \n''') % (STAMP, INFO[0], INFO[-1], HSCORE, VSCORE, TPSCR)
    with open(CURRFILE, 'a+') as FX:
        FX.write(OUTTXT)
    return;

