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
            except voluptuous.Invalid as exc:
                print(f"{filename} is invalid")
                print(exc.msg)
                exitcode += 1
            print(f"{filename} is valid")
sys.exit(exitcode)

