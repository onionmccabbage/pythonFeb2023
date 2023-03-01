from  my_context_mgr import write_to_context
from swapi_service import SwapiService
import sys

def main():
    data = SwapiService.getSwapi()
    write_to_context('people1.txt', data)

if __name__ == "__main__":
    sys.argv.append('swapi.txt') # we can inject additional sys.argv values
    main()