import pstats
def main():
    p = pstats.Stats('profile_output')
    p.print_stats()

if __name__ == '__main__':
    main()