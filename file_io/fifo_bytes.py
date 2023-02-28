# reading and writing byte files

def simpleByteWriter():
    # we really should use try-except when dealing with external assets
    b = bytes( range(0,255) ) # make some bytes
    fout = open('bytes', 'wb') # 'b' for bytes
    fout.write(b)
    fout.close() # always remember to do this - or use 'with'

def simpleByteReader():
    r = False # commonly use None
    try:
        with open('bytes', 'rb') as fin:
            r = fin.read()
    except Exception as err:
        pass
    finally:
        pass
        return r # f'{r}' # the finally block ALWAYS executes

if __name__ == '__main__':
    simpleByteWriter()
    print( simpleByteReader() )