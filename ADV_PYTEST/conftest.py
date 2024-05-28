from datetime import datetime

from py.xml import html
import pytest

# Fixtures Section

# Fixture to provide a sample data
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

# Fixture to setup and teardown resources
@pytest.fixture(scope="session")
def setup_teardown():
    # Setup code
    print("Setup")
    yield
    # Teardown code
    print("Teardown")

# Hooks Section

# Hook to modify HTML report results table row
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):
    if "example" in report.nodeid:
        # Insert custom text for specific tests
        cells.insert(1, '<td>This is a custom text for example test</td>')

# Called before adding the title to the report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Sauce Demo Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["<p>Test Requirements: Run single test script with assertions.</p>"])


@pytest.mark.hookwrapper
# pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    timestamp = datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])
    if report.when == 'call':

        feature_request = item.funcargs['request']

        driver = feature_request.getfixturevalue('setup')
        driver.save_screenshot('sauce/scr'+timestamp+'.png')

        extras.append(pytest_html.extras.image('sauce/scr'+timestamp+'.png'))

        # always add url to report
        extras.append(pytest_html.extras.url('http://www.saucedemo.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.image('sauce/scr.png'))
            extras.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extras = extras

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.server_name = item.keywords['servername'].kwargs['server']

# Called after building results table header.
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Server Name', class_='sortable server-name', col='server-name'))

# Called after building results table row.
# @pytest.hookimpl(hookwrapper=True)
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.server_name, class_='col-server-name'))

@pytest.hookimpl(hookwrapper=True)
def pytest_html_results_table_row(report, cells):
    print("Hook called for test:", report.nodeid)
    outcome = yield
    report_nodeid = report.nodeid
    if "example" in report_nodeid:
        print("Inserting custom text for test:", report_nodeid)
        cells.insert(1, '<td>This is a custom text for example test</td>')
    outcome.force_result(None)

# Configurations Section

# Configuration to be applied to all tests
def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow")

# Configuration to be applied based on command line options or environment variables
def pytest_addoption(parser):
    parser.addoption("--myoption", action="store_true", help="enable my option")

# Function to perform actions based on command line options or environment variables
def pytest_collection_modifyitems(config, items):
    if config.getoption("--myoption"):
        # Perform actions based on option
        pass

