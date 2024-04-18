import pytest
import report_controller

@pytest.hookimpl()
def pytest_sessionfinish(session):
    report_controller.generate_excel_report()