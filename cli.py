#python cli.py <domain> <from_unit> <to_unit> <value>
#команда /путь к файлу /аргументы 
#argv=argument values
#sys system library
from sys import argv
from unitflex import convert

def main():
    domain = argv[1]
    from_unit = argv[2]
    to_unit = argv[3]
    value = float(argv[4])
    print(convert(domain, from_unit, to_unit, value))


if __name__ == "__main__":
    main()
