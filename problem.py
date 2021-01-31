import string
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import shutil
import sys
hostname="localhost"
dir_path=sys.argv[1]

#print("the dir name is ", dir_path)

class Problem(BaseHTTPRequestHandler):
    def do_POST(self):
        json_data = None
        json_data = json.load(self.rfile)
        #print(json_data)
        #print(json_data['name'])
        if json_data is not None:
            json.dumps(json_data)
        else:
            print("Got no data")
        #print(json_data)
        problem_name = json_data['name']
        problem_name.translate({ord(c): None for c in string.whitespace})
        #making folder in current directory
        path_for_problem = os.path.join(dir_path, problem_name)
        path_for_problem = path_for_problem.replace(' ','_')
        path_for_problem = path_for_problem.replace('.','')
        path_for_problem = path_for_problem.replace('\'','')
        #print(path_for_problem)
        if os.path.exists(path_for_problem) and os.path.isdir(path_for_problem):
            shutil.rmtree(path_for_problem)
        os.mkdir(path_for_problem)

        input_data = json_data['tests']
        #print(input_data)
        #saving the samples in diff folders.
        #making the seperate folders for each Test

        os.mkdir(os.path.join(path_for_problem,"test_cases"))
        for idx, u in enumerate(input_data):
            #print(u['input'],"\n", u['output'],"\n")
            name = os.path.join(path_for_problem,"test_cases",str(idx))
            os.mkdir(name)
            with open(os.path.join(name,"input.txt"),'w') as f:
                f.write(u['input'])
            with open(os.path.join(name,"output.txt"),'w') as f:
                f.write(u['output'])


def run():
   port = 5001
   server = HTTPServer((hostname, port), Problem)
   server.serve_forever()

if __name__ == '__main__':
    run()
