# import os
# import subprocess
# path = "jobs/interact.py"
# # You can modify the port or other options as needed
# env = os.environ.copy()
# env["PYTHONPATH"] = "."
# subprocess.run(["chainlit", "run", path])

import os
import subprocess
import sys
from pathlib import Path

# Get absolute path to current directory (project root)
BASE_DIR = Path(__file__).parent.resolve()

# Absolute path to Chainlit app
CHAINLIT_APP = BASE_DIR / "jobs" / "interact.py"

# Validate file exists
if not CHAINLIT_APP.exists():
    print(f"Error: File not found at {CHAINLIT_APP}", file=sys.stderr)
    sys.exit(1)

# Set environment with absolute PYTHONPATH
env = os.environ.copy()
env["PYTHONPATH"] = str(BASE_DIR)  # Critical for Windows!

# Run Chainlit with absolute path
try:
    subprocess.run(
        [
            "chainlit", "run", 
            str(CHAINLIT_APP), 
            "--port", "8000"
        ],
        env=env,
        check=True,
        text=True
    )
except subprocess.CalledProcessError as e:
    print(f"Chainlit failed with error: {e}", file=sys.stderr)
except FileNotFoundError:
    print("Error: 'chainlit' command not found. Install with: pip install chainlit", file=sys.stderr)