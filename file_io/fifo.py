
def simpleWriter():
    # here we provide a file access object
    # 'at' means append text 
    # 'wt' (over)write text
    # 'xt' measns exclusive write text
    try:
        fout = open('text.txt', 'at')
        print('this is easy', file=fout)
        fout.close() #' always a good idea to close the file access object
    except FileExistsError as err:
        print(err)
    except FileNotFoundError as err:
        print(err)
    except Exception as err:
        print(err)

def simpleReader():
    fin = open('text.txt', 'rt') # 'rt' will read text
    received = fin.read() # everything as a single string
    received = fin.readline() # just one line as a string
    received = fin.readlines() # a list of the lines
    print(received)
    fin.close()

def contextReader():
    with open('text.txt') as fin: # this will automatically close when done
        received = fin.read()
        return received

if __name__ == '__main__':
    simpleWriter()
    simpleReader()
    print( contextReader() )