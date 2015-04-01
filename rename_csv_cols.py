cols = ["Q%i"%i for i in range(1, 13)]
fout = open('the_airport_survey.fixedcolnames.csv', 'w')
fout.write(','.join(cols) + '\n')
fin = open('the_airport_survey.fixed.csv')
header = fin.next()
for l in fin:
    fout.write(l)

fin.close()
fout.close()

qs = header.strip().split(',')
fout = open('questions.txt', 'w')
fout.write('\n'.join(qs))
fout.close()
