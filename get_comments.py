import pandas
d = pandas.read_csv('the_airport_survey.fixedcolnames.csv')
comments = d.Q12
comments = comments[comments.notnull()]
comments.to_csv('comments.csv', index=False)

