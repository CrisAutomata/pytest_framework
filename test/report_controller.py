from xml.etree import ElementTree as ET
import pandas as pd
import time

def read_data_from_xml_file():
    dict_data = {}
    # Parse the XML data
    root = ET.parse('test_result.xml')

    # Find all testcase elements
    testcases = root.findall(".//testcase")
    for testcase in testcases:
        test_status = 'PASSED' if testcase.find(".//failure") == None else 'FAILED'
        dict_data[testcase.attrib["name"]] = test_status
    # Print the testcase names
    print(dict_data)
    return dict_data


def create_new_sheet(writer):
    """
    Creates a new sheet name that doesn't conflict with existing ones.

    Args:
        writer: The ExcelWriter object.

    Returns:
        A unique sheet name.
    """
    sheet_names = [sheet.title for sheet in writer.sheets.values()]
    new_sheet_name = "Sheet1"
    i = 1
    while new_sheet_name in sheet_names:
        new_sheet_name = f"Sheet{i}"
        i += 1
    return new_sheet_name


def write_data_to_excel_file(input_dict):
    # Define your data as a DataFrame
    # Create a list of tuples from the dictionary
    data_list = [(key, value) for key, value in input_dict.items()]

    # Create the DataFrame using the list of tuples and column names
    data = pd.DataFrame(data_list, columns=['name', 'status'])

    # Print the DataFrame
    print(data)

    # Open the existing excel file (or create a new one) with context manager
    with pd.ExcelWriter("test_report.xlsx", engine="openpyxl", mode='a') as writer:
        # Create a unique sheet name
        sheet_name = create_new_sheet(writer)

        # Write the DataFrame to the new sheet
        data.to_excel(writer, sheet_name=sheet_name, index = True)

        print(f"New sheet '{sheet_name}' created and data written to existing_report.xlsx!")

def generate_excel_report():
    dict_data = read_data_from_xml_file()
    write_data_to_excel_file(dict_data) 

if __name__ == "__main__":
    generate_excel_report()