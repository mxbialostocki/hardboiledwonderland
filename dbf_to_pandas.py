"""
load legacy unity data into pandas dataframe
you'll need iter() because, by default, Pandas won't recognise that the dbf object is iterable.
"""
from dbfread import DBF
from pandas import DataFrame

unity = DBF("./local/MASTER.DBF")
frame = DataFrame(iter(unity))
unitycsv = frame.to_csv("./local/unitymastercsv.csv")

# print(frame[-20:])
frame.head()

test_frame = frame[-50:]

# for record in test_frame:
#     print(record[1] + ' || ' + record[2] + ' by ' + record[3])