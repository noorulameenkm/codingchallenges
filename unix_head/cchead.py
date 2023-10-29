from argparse import ArgumentParser
from pathlib import Path



def read_from_stdin():
    i = 0
    while i < 10:
        input_ = input() 
        print(input_)
        i += 1


def parse_file(filename, numberoflines=0, chars=0):
    with open(Path(filename)) as file:
        if numberoflines == 0 and chars == 0:
            print(file.read())
        elif numberoflines > 0:
            lines = file.readlines()[:numberoflines]
            for line in lines:  print(line.strip('\n'))
        elif chars > 0:
            print(file.read(chars))


def run_command():
    parser = ArgumentParser("head command")
    parser.add_argument("files", type=str, nargs='*')
    parser.add_argument("-n", "--number", required=False, type=int, default=0, help="The number of lines to print")
    parser.add_argument("-c", "--characters", required=False, type=int, default=0)
    args = parser.parse_args()
    print(args)
    if args.files:
        for file in args.files:
            print(f"==> {file} <==")
            parse_file(file, args.number, args.characters)
            print()
    else:
        read_from_stdin()
    

if __name__ == "__main__":
    run_command()