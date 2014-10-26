from collections import OrderedDict
import subprocess

def convert_file_to_json(filename):
    file_lines = {}
    file_lines[filename] = {}
    with open(filename) as file:
        line_num = 1
        for line in file:
            file_lines[filename][str(line_num)] = {'code':line}
            line_num = line_num + 1
    return file_lines

def find_python_files_in_project(filepath):
    output = subprocess.check_output("find {} -name '*.py'".format(filepath),shell=True, cwd=r'{}'.format(filepath))
    output_array = output.splitlines()
    return output_array

if __name__ == '__main__':
    "Testing functions"

    from sys import argv
    from settings import load_project_properties

    try:
        script, user, code_base = argv
    except ValueError:
        print "Incorrect number of arguments"
    else:
        config = load_project_properties()
        #print 'config', config

        file_path = config[user][code_base]
        print "List of Python Files\n", find_python_files_in_project(file_path)
