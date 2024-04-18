import xml.etree.ElementTree as ET
import pytest

import report_controller
def parse_test_results(xml_file):
  """Parses the JUnit XML file and returns a dictionary of test results.

  Args:
      xml_file: Path to the JUnit XML file.

  Returns:
      A dictionary containing test results data.
  """
  test_results = {"passed": 0, "failed": 0, "skipped": 0}
  tree = ET.parse(xml_file)
  root = tree.getroot()

  for testcase in root.findall("./testsuite/testcase"):
    status = testcase.attrib["status"]
    test_results[status] += 1

  return test_results

def generate_text_report(test_results, report_file):
  """Generates a text report containing test results and writes it to a file.

  Args:
      test_results: A dictionary containing test results data.
      report_file: Path to the text report file.
  """
  with open(report_file, "w") as f:
    f.write(f"Test Results Summary:\n")
    f.write(f"  Passed: {test_results['passed']}\n")
    f.write(f"  Failed: {test_results['failed']}\n")
    f.write(f"  Skipped: {test_results['skipped']}\n")



# Add this line at the end of the script
if __name__ == "__main__":
  pytest_sessionfinish(None)  # Simulate session finish for standalone execution
