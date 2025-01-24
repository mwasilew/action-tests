import os
import sys
import yaml
import voluptuous
from lava_common.schemas import validate

exitcode = 0

for root, dirs, files in os.walk("./lava"):
    for fname in files:
        if fname.endswith(".yaml"):
            filename = os.path.join(root, fname)

            try:
                f = open(filename, "rb")
                y = yaml.safe_load(f)
                f.close()
                validate(y)
            except voluptuous.Invalid as e1:
                print(f"{filename} is invalid")
                print(e1.msg)
                exitcode += 1
            except yaml.parser.ParserError as e2:
                print(f"{filename} is invalid")
                print(e2.problem)
                print(e2.note)
                exitcode += 1
            print(f"{filename} is valid")
sys.exit(exitcode)

