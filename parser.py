import sys

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        with open(filename, "r") as fh:
            for num, line in enumerate(fh):
                if num == 0:
                    print(f"{filename}:{line[line.find('(')+1:line.find(')')]}")
                else:
                    continue
