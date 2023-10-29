import subprocess

calc_proc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
print(calc_proc.poll() == None)
print(calc_proc.wait())
print(calc_proc.poll())
