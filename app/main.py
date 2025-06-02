

import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

CHAINLIT_APP = "./app/jobs/interact.py" 

if not os.path.exists(CHAINLIT_APP):
    print(f"Error: File not found at {CHAINLIT_APP}", file=sys.stderr)
    sys.exit(1)

env = os.environ.copy()
env["PYTHONPATH"] = "."  

try:
    subprocess.run(
        [
            "chainlit", "run", 
            str(CHAINLIT_APP)
        ],
        env=env,
        check=True,
        text=True
    )
except subprocess.CalledProcessError as e:
    print(f"Chainlit failed with error: {e}", file=sys.stderr)
except FileNotFoundError:
    print("Error: 'chainlit' command not found. Install with: pip install chainlit", file=sys.stderr)
