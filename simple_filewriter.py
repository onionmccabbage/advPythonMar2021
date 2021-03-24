fout = open('mylog.txt', 'at')
print('here is new text', file=fout)
fout.close()

# alternatively
with open('mylog.txt', 'at') as fout:
    print('here is some further text', file=fout)
    # no need to close, the 'with' statementt closes automatically