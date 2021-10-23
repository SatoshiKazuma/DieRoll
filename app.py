import random, csv

diepick = random.randint(1, 6)

with open('dieoutput.csv') as dieoutput:
    csvReader = csv.reader(dieoutput)
    for row in csvReader:
        if str(diepick) in row:
            a1,b1,c1,d1,e1,f1,g1,h1,i1=row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]
            
def ThrowDice(a,b,c,d,e,f,g,h,i):
    print(f'''
 ╭───────╮
 │ {a} {b} {c} │
 │ {d} {e} {f} │
 │ {g} {h} {i} │
 ╰───────╯
''')
ThrowDice(a1,b1,c1,d1,e1,f1,g1,h1,i1)