import sys
import subprocess
import os
import filecmp
class colors:
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    ENDC = '\033[0m'

class icons:
    PASS  = colors.GREEN + 'Y' + colors.ENDC
    FAIL  = colors.RED + 'N' + colors.ENDC
    MAYBE = colors.YELLOW + '?' + colors.ENDC

def Error(message):
    print(colors.BOLD+colors.RED+"ERRORS"+colors.ENDC+": "+message)
    exit(1)

def warn(message):
    print (colors.BOLD + colors.HEADER + "WARN" + colors.ENDC + ": " + message)

def bold(message):
    print (colors.BOLD + message + colors.ENDC)

def run(cmd):
    return subprocess.call(['/bin/bash', '-i', '-c', cmd])

def print_file(path):
    f = open(path,'r')
    lines = f.readlines()
    content = ""
    for line in lines:
        line = line.strip('\n');
        line = line.strip(' ');
        if line == "": continue
        content = content + line + "\n";
    return content

def cmp(path):
    cmd = './a.out < ' + path + '/input.txt > myout.txt';
    if run(cmd):
        sys.exit()

    my_out = print_file(sys.argv[1] + '/myout.txt')
    sol_out = print_file(path + '/output.txt')
    
    if my_out == sol_out:
        print("ACCEPTED")
    else:
        print("INPUT -> \n");
        print(print_file(path +'/input.txt'))
        print("OUTPUT -> \n{}\n".format(sol_out));
        print("YOUR_OUTPUT -> \n{}\n".format(my_out));
        

cpp_file_name = sys.argv[1]+'/sol.cpp'

n = len(sys.argv)

if subprocess.call(["g++",cpp_file_name]):
    # compilation error
    sys.exit()

path = sys.argv[1] + '/test_cases'
for x in os.listdir(path):
    cmp(os.path.join(path,x));

