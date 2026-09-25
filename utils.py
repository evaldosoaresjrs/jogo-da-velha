import os
import subprocess

# Determine command based on operating system
command = "cls" if os.name == "nt" else "clear"

# Safely execute the clear command
clear_console = lambda : subprocess.run([command], shell=True if os.name == "nt" else False)