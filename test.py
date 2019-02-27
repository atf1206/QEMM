
from pyq import q
from datetime import date




q.trade:([]date:();sym:();qty:())


q.insert('trade', (date(2006,10,6), 'IBM', 200))

q.trade.show()


