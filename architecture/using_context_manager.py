# we can use @contextmanager to redirect output
from contextlib import contextmanager
import sys

@contextmanager # this function can now manage context, i.e. where stuff gets output to
def my_redirect(redir): # redir will be the context I want to use
    # first, we wil make a noteof the current context
    orig_context = sys.stdout # by default, sys.stdout is the print console
    # then we tell sys to use a different context
    sys.stdout = redir
    yield # the function will yield the next available object to write out to this new context
    # remember to put the original context back in place
    sys.stdout = orig_context # all good

def main():
    if len(sys.argv[]) > 1: # sys.argv[0] is ALWAYS the module name
        pass # handle the additional arguments
    with open('mylog.txt', 'a') as fout:
        # here we use our (decorated) context manager function
        with my_redirect(fout): # here we pass our file acces object to be used as the new context
            print('this text will be redirected to the log file')
        print('this text will be sent to the default console')
    print('where does this go?')



if __name__ == '__main__':
    main()