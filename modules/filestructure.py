import os
import json
import fusor
import savejson

def create_structure(path, name, pylint_analysis, git_analysis, code_base, old_path):
    """ Given the root directory, this function will return
        The file structure of the code base.
    """
    structure = {}
    root, subdirs, files = next(os.walk(path))
    #print "root: %s\n subirs: %s\n files: %s\n" % (root, subdirs, files)

    structure.update({"name" : name})
    structure.update({"path" : path})

    # http://stackoverflow.com/a/18435
    files = [module for module in files if module.endswith(".py")]
	
	# __init__ is a difficult case, as it is in multiple
	# directories and has 'no' size. Decided to remove
    files = [module for module in files if (not module.startswith("__init__"))]

    if (subdirs or files):
		# the fusion algorithm: for each path, we look for sub dirs and files.
		# if sub dirs exist, we call function again on the old path + sub dir
		# if no subdirs, then we add files to structure
        children = []
        if (subdirs):
            for subdir in subdirs:
                new_path = "%s/%s" % (path, subdir)
                children.append(create_structure(new_path, subdir, pylint_analysis, git_analysis, code_base, old_path))

        if (files):
            for file in files:
				# add information for front end here. Use all analyzer information
                location = "%s/%s" % (path, file)
                temp_file_dict = {}
                temp_file_dict["name"] = file
                temp_file_dict["path"] = location
                temp_file_dict["json"] = code_base + "/" + savejson.get_name(location, old_path, code_base)
                temp_file_dict["size"] = git_analysis[location]["size"]
                temp_file_dict["colour"] = pylint_analysis[location]["colour"]
                children.append(temp_file_dict)
        structure.update({"children" : children})
    return structure

if __name__ == '__main__':
    pass
