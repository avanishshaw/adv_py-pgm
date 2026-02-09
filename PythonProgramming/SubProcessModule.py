#  SubProcess Module

# Execute external system commands
# Iterate with OS processes
# Capture output, error and return codes
# Control the process execution

#run the OS level commands - Linux, MacOS, Windows

import subprocess

# subprocess.run() - run command and wait
# subprocess.Popen() - run process asynchronulsy
# subprocess.PIPE #- capture the output
# subprocess.CompletedProcess = result
# subprocess.TimeoutExpired - Timeout outexepction
# subprocess.calledProcessError - command failure

# result = subprocess.run("dir", shell=True, capture_output=True, text = True)

# result = subprocess.run("ipconfig", shell=True, capture_output=True, text = True)

result = subprocess.run("python --version", shell=True, capture_output=True, text = True)
print(result.stderr)
# print(result.stderr)