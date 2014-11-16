import os
import json
import fusor

def create_structure(path, name, pylint_analysis, git_analysis, code_base):
    """ Given the root directory, this function will return
        The file structure of the code base.
    """
    structure = {}
    root, subdirs, files = next(os.walk(path))
#    print "root: %s\n subirs: %s\n files: %s\n" % (root, subdirs, files)

    structure.update({"name" : name})

    # http://stackoverflow.com/a/18435
    files = [module for module in files if module.endswith(".py")]
    files = [module for module in files if (not module.startswith("__init__"))]

    if (subdirs or files):
        children = []
        if (subdirs):
            for subdir in subdirs:
                new_path = "%s/%s" % (path, subdir)
                children.append(create_structure(new_path, subdir, pylint_analysis, git_analysis, code_base))

        if (files):
            for file in files:
                location = "%s/%s" % (path, file)
                temp_file_dict = {}
                temp_file_dict["name"] = file
                temp_file_dict["path"] = code_base + "/" + fusor.get_name(location, code_base)
                temp_file_dict["size"] = git_analysis[location]["size"]
                temp_file_dict["colour"] = pylint_analysis[location]["colour"]
                children.append(temp_file_dict)
        structure.update({"children" : children})
    return structure

if __name__ == '__main__':
    import filehelper as FH
    import authormapper as AM
    import pylintanalzyer as PY

    path_to_code_base = "/home/asumal/git/cs410/plumbum/plumbum"

    list_of_files = FH.find_python_files_in_project(path_to_code_base)
    pylint_analysis = PY.get_pylint_analysis(list_of_files)
    git_analysis = AM.get_git_analysis(path_to_code_base, list_of_files)

    print json.dumps(create_structure(path_to_code_base, "plumbum", pylint_analysis, git_analysis, "plumbum"))
