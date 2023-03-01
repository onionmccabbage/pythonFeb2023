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

def write_to_context(filename='mylog.txt', what_to_write=''):
    if len(sys.argv) > 1: # sys.argv[0] is ALWAYS the module name
        # validate  the additional arguments
        if isinstance(sys.argv[1], str):
            filename = sys.argv[1]
        # concatenate all system argument variables (includes module name)
        for item in sys.argv:
            what_to_write += f'{item} ' # put a space between each of them
    with open(filename, 'a') as fout:
        # here we use our (decorated) context manager function
        with my_redirect(fout): # here we pass our file acces object to be used as the new context
            print(what_to_write)

if __name__ == '__main__':
    write_to_context()