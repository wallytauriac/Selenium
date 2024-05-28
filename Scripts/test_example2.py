import pytest
import pytest_html
from pytest_html import extras



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras
    else:
        extras.append(pytest_html.extras.html("<div>Additional Test Data</div>"))
        report.extras = extras

@pytest.mark.parametrize("num", [1, 2, 3])
def test_example(num):
    assert num % 2 == 0
    extras.text('Add some simple Text')