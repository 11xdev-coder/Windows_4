import subprocess

processes = [line.split() for line in subprocess.check_output("ps").splitlines()]

print(processes)
