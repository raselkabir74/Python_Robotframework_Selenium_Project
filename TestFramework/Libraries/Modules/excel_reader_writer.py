"""
Implementing static method to read data from excel file
"""

import xlrd
import datetime
import math

_excel_data_dictionary_keys = []
_excel_data_dictionary = {}

def read_test_data(file_path, sheet_name):
    """
    Implementing returning test data for a test suit
    :param file_path:
    :param sheet_name:
    :return: returning test data dictionary for a test suits
    """
    del _excel_data_dictionary_keys[:]
    _excel_data_dictionary = {}
    try:
       workbook = xlrd.open_workbook(file_path)
       sheet = workbook.sheet_by_name(sheet_name)
       col = 0
       for row in range(sheet.nrows):
           dictionary_key = sheet.cell(row, col).value
           value = sheet.cell(row, col+1).value
           _excel_data_dictionary_keys.append(str(dictionary_key))
           splitted_key = dictionary_key.lower().split()
           if "date" in splitted_key:
               try:
                    value = datetime.datetime(*xlrd.xldate_as_tuple(value, workbook.datemode))
                    value = "%d/%d/%d" % (value.month, value.day, value.year)
               except:
                    value = ''
                    pass
           elif (dictionary_key.lower().lower().endswith("id")) or (dictionary_key.lower().lower().endswith("number")):
                try:
                    value = math.trunc(value)
                except:
                    pass
           _excel_data_dictionary.update({_excel_data_dictionary_keys[row]: str(value)})
    except IOError:
        raise
    finally:
        return _excel_data_dictionary
