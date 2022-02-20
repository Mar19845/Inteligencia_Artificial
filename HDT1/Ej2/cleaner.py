import sudoku as sdk

def fileCleaner(txt):

    l = txt.readlines()
    n = l[0].rstrip("\n")
    m = l[1].rstrip("\n")
    p = l[2].rstrip("\n").replace(' ','')
    pp = l[3].rstrip("\n").replace(' ','')
    ppp = l[4].rstrip("\n").replace(' ','')
    p1 = []
    p2 = []
    p3 = []

    for i in p:
        p1.append(i)
    p1 = list(map(int, p1))

    for i in pp:
        p2.append(i)
    p2 = list(map(int, p2))
    
    for i in ppp:
        p3.append(i)
    p3 = list(map(int, p3))

    sdk.sudokuDFS(n,m,p1,p2,p3)