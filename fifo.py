# see https://pastebin.com/5RQqzB8R
# file input and file output - fifo

# this is a file access object (NOT the file itself)
fout = open('snip.txt', 'wt') # a to append to a file 'w' to overwrite 't' for a text file (the default)
print('here is some content', file=fout) # direct the output to our file
fout.close() # tidy up

# writing longer pieces of text in fragments
long_string = "the while... loop will automatically close any open files\nwhich saves us doing it"

# NB this is a great place to check for exceptions
try:
    fout = open('other.txt', 'xt') # x means exclusive access - if the file exists we get an exception
    size   = len(long_string)
    offset = 0
    chunk  = 24
    # loop over the text writing a bit at a time
    while True:
        if offset > size:
            break
        else:
            fout.write(long_string[offset:offset+chunk])
            offset+=chunk
except FileExistsError as err: # Exception catches all exception types
    print('the file already exists')
    print(err.errno)
except Exception as err: # Exception catches all exception types
    print('Some other exception occurred')
    print(err.errno)
finally:
    print('this block always runs, even if there is an exception')
# no need to close() since the while will close in break

# reading from text files
fin = open('other.txt', 'r') # 'r' means read. 'rt' means read text, which is the default
received = fin.read() # readline() for one line readlines for a list of all lines
anymore = fin.readline() # oops - nothing left!!
print('anymore contains {} and nothing else'.format(anymore))
print(received)
# # we can 'seek' a position within a file
fin.seek(24)
the_rest = fin.read() # from here onwards
print(the_rest)
fin.seek(0)
the_rest = fin.read()
print(the_rest)
fin.seek(48)
the_rest = fin.read()
print(the_rest)
fin.close() # good idea to tidy up, which releases resources

# bytes encode values at a lower level than text

# handle byte files
b = bytes( range(0, 256) ) # start at 0 stop before 256
print(b)

fout = open('bfile', 'wb') # 'w' to (over)write 'b' means bytes (rather than text)
fout.write(b)
fout.close()

# NB we could use a while loop again, which will auto-close the file access object

# read bytes back from a file
fin = open('bfile', 'rb')
retrieved_b = fin.read() # read the whole file 
fin.close()
print(retrieved_b)