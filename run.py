import sys
from core import run_file

if len(sys.argv) < 2:
    print("OSCi: osc file.osc")
else:
    run_file(sys.argv[1])
