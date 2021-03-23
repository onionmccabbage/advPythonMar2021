fout = open('mylog.txt', 'at')
print('here is some text', file=fout)
fout.close()

# alternatively
with open('mylog.txt', 'at') as fout:
    print('here is some other text', file=fout)
    # no need to close, the 'with' statementt closes automatically