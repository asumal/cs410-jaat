#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gluon import *
import subprocess

class Pylint_Analyzer(object):
    """ Functions related to pylint analyzer
    """
    # command line operators to only receive relevant information
    INSTRUCTIONS = '-rn --msg-template="{line}:{C}:{msg}"'

    # type of script this command will be using
    PYLINT = 'pylint'

    # general warning that may be ignored for our purpose
    IGNORE_WARNING = 'No config file found, using default configuration'

    def __init__(self, name, root):
        self.name = name
        self.root = root
        self.analysis = self.begin_analysis(self.root)

    def get_name(self):
        """ Return the name of this object
        """
        return self.name

    def get_root(self):
        """ Return the file path to the code base
        """
        return self.root

    def get_analysis(self):
        """ Return the analysis related to this object
        """
        return self.analysis

    def get_pylint_results():
        """ brief - Runs pylint on the specified file
            param path_to_root - the file to run pylint on
            return - the errors associated with the specified file
        """
        message = ['pylint', '-rn', '--msg-template="{line}:{C}:{symbol}"','C:\Users\Arjun\pease']

        p1 = subprocess.Popen(message, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_value, stderr_value = p1.communicate()

        list_of_errors = stderr_value.splitlines()

        if (len(list_of_errors) == 1):
            list_of_arguments = stdout_value.splitlines()
            analyzer_results = parse_pylint_results(list_of_arguments)
        else:
            print list_of_errors
        return analyzer_results

    def parse_pylint_results(results):
        pylint_results = {}
        for item in results:
            if item.startswith('*************'):
                name = get_file_name(item)
                pylint_results.update({name: {}})
            else:
                line_number, error_type, message = get_line_and_error(item)
                pylint_results[name].update({line_number : {"category" : error_type, "desc" : message}})
        return pylint_results
