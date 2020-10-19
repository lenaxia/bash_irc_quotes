import sys
from typing import List

def generate_csv(file_list:List[str]):
    """
    Aggregates cleaned quotes to as an CSV to stdout.

    Note: This is fragile code optimized around the structure of the w3m renders of
    bash.org. Also, the list comprehension is very much not performant.
    """
    for filename in file_list:
        with open(filename, "r") as fh:
            quote_id = "".join([char for char in filename if char.isnumeric()])
            text = [line.lstrip() for line in fh]
            header = text[0]
            score = int(header[header.find("(") + 1 : header.find(")")])
            body = "".join([line.replace("\n","\\n") for line in text[1:]])
            print(f"{quote_id},{score},\"{body}\"")

if __name__ == "__main__":
    generate_csv(sys.argv[1:])
