"""
templator.py reads in an excel file and a template  and outputs a file for each row
in the excel file, by substituting the template variables with the values in the columns.

This technique uses pandas to read the excel file into a DataFrame and the python format operator ``%```
to apply the values.
"""
import sys
import os
import pandas as pd


def main(template_file, excel_file):
    # read in the template and the excel file
    template = open(template_file, 'r').read()
    variables = pd.read_excel(excel_file)

    # loop over each row (note, one of the columns must be called "filename")
    for row_number, values in variables.iterrows():
        filename = values['filename']
        with open(filename, 'w') as f:
            f.write(template % values)



if __name__ == '__main__':    
    template_file = os.path.join(os.path.dirname(__file__), 'template.txt')
    excel_file = os.path.join(os.path.dirname(__file__), 'variables.xls')
    main(template_file, excel_file)