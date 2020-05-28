name = 'Mohamed AL Balushi'
#integer
age= 35
#boolean
value= True
#float
value=10.1
#print
print(name)
#save to RAM with location
print(id(name))
#RAM location with HEX
print(hex(id(name)))
#print first_name and last_name = concatenate
fname='Mohamed'
lname='Al Balushi'
print(fname + " " + lname)
#print capital and lower letter case
print(fname.upper() + " " + lname.upper())
#replace word with any other word
print(fname + " " + lname.replace('Al Balushi' , 'Moosa'))

#buffer over flow attack method
buffer= 'adp' * 100
print(buffer)

