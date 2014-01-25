

def GENERATE():
    import random

    NUMBER_OF_FILES = 150
    
    for i in range(0,  NUMBER_OF_FILES):
        with open('names.txt') as f:
            for K, l in enumerate(f):
                pass
        NUMB = (K)
        NUMB_GEN_X = random.randint(0,NUMB);
        OP = open('names.txt')
        LINES = OP.readlines()
        NAME = LINES[NUMB_GEN_X]
        f.close()

        with open('av.txt') as f:
            for K, l in enumerate(f):
                pass
        NUMB = (K)
        NUMB_GEN_X = random.randint(0,NUMB);
        OP = open('av.txt')
        LINES = OP.readlines()
        AV = LINES[NUMB_GEN_X]
        f.close()

        with open('brands.txt') as f:
            for K, l in enumerate(f):
                pass
        NUMB = (K)
        NUMB_GEN_X = random.randint(0,NUMB);
        OP = open('brands.txt')
        LINES = OP.readlines()
        BRND = LINES[NUMB_GEN_X]
        f.close()

        with open('model.txt') as f:
            for K, l in enumerate(f):
                pass
        NUMB = (K)
        NUMB_GEN_X = random.randint(0,NUMB);
        OP = open('model.txt')
        LINES = OP.readlines()
        MODL = LINES[NUMB_GEN_X]
        f.close()

        with open('summs.txt') as f:
            for K, l in enumerate(f):
                pass
        NUMB = (K)
        NUMB_GEN_X = random.randint(0,NUMB);
        OP = open('summs.txt')
        LINES = OP.readlines()
        SUMS = LINES[NUMB_GEN_X]
        f.close()

        with open('years.txt') as f:
            for K, l in enumerate(f):
                pass
        NUMB = (K)
        NUMB_GEN_X = random.randint(0,NUMB);
        OP = open('years.txt')
        LINES = OP.readlines()
        YRS = LINES[NUMB_GEN_X]
        f.close()

        with open('os.txt') as f:
            for K, l in enumerate(f):
                pass
        NUMB = (K)
        NUMB_GEN_X = random.randint(0,NUMB);
        OP = open('os.txt')
        LINES = OP.readlines()
        OS = LINES[NUMB_GEN_X]
        f.close()
        
        NUMB_GEN_X = random.randint(1,9);
        fileName = ('shop/' + NAME + str(NUMB_GEN_X))
        S = fileName.split(' ')
        for i in range(len(S)):
            S[i] = S[i].translate(None, '\n')
        fileName = "".join(S)

        Tname = (NAME.translate(None, '\n') + str(NUMB_GEN_X))
        OF = open(fileName, 'w')
        OUTTXT = ('''%s \n%s \n%s \n%s \n%s \n%s \n%s''') % (Tname, OS, AV, YRS, BRND, MODL, SUMS)
        OF.write(OUTTXT)
        OF.close()


        # MAKE CONFIG FILE

        import xgetscores as FRG
        with open(fileName) as OP:
            INFO = OP.readlines()
        OP.close()
        FRG.LOOK_AT_DATA(INFO);
        

        
    return;

GENERATE();
