import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By


def test_should_find_element_by_xpath(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    child = element.find_element(By.XPATH, "select")
    assert child.get_attribute("id") == "2"


def test_should_not_find_element_by_xpath(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    with pytest.raises(NoSuchElementException):
        element.find_element(By.XPATH, "select/x")


def test_finding_dot_slash_elements_on_element_by_xpath_should_find_not_top_level_elements(driver, pages):
    pages.load("simpleTest.html")
    parent = driver.find_element(By.ID, "multiline")
    children = parent.find_elements(By.XPATH, "./p")
    assert 1 == len(children)
    assert "A div containing" == children[0].text


def test_should_find_elements_by_xpath(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    children = element.find_elements(By.XPATH, "select/option")
    assert len(children) == 8
    assert children[0].text == "One"
    assert children[1].text == "Two"


def test_should_not_find_elements_by_xpath(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    children = element.find_elements(By.XPATH, "select/x")
    assert len(children) == 0


def test_finding_elements_on_element_by_xpath_should_find_top_level_elements(driver, pages):
    pages.load("simpleTest.html")
    parent = driver.find_element(By.ID, "multiline")
    all_para_elements = driver.find_elements(By.XPATH, "//p")
    children = parent.find_elements(By.XPATH, "//p")
    assert len(all_para_elements) == len(children)


def test_should_find_element_by_name(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    child = element.find_element(By.NAME, "selectomatic")
    assert child.get_attribute("id") == "2"


def test_should_find_elements_by_name(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    children = element.find_elements(By.NAME, "selectomatic")
    assert len(children) == 2


def test_should_find_element_by_id(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    child = element.find_element(By.ID, "2")
    assert child.get_attribute("name") == "selectomatic"


def test_should_find_elements_by_id(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    child = element.find_elements(By.ID, "2")
    assert len(child) == 2


def test_should_find_element_by_id_when_multiple_matches_exist(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.ID, "test_id_div")
    child = element.find_element(By.ID, "test_id")
    assert child.text == "inside"


def test_should_find_element_by_id_when_no_match_in_context(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.ID, "test_id_div")
    with pytest.raises(NoSuchElementException):
        element.find_element(By.ID, "test_id_out")


def test_should_find_element_by_link_text(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "div1")
    child = element.find_element(By.LINK_TEXT, "hello world")
    assert child.get_attribute("name") == "link1"


def test_should_find_elements_by_link_text(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "div1")
    children = element.find_elements(By.LINK_TEXT, "hello world")
    assert len(children) == 2
    assert "link1" == children[0].get_attribute("name")
    assert "link2" == children[1].get_attribute("name")


def test_should_find_element_by_class_name(driver, pages):
    pages.load("nestedElements.html")
    parent = driver.find_element(By.NAME, "classes")
    element = parent.find_element(By.CLASS_NAME, "one")
    assert "Find me" == element.text


def test_should_find_elements_by_class_name(driver, pages):
    pages.load("nestedElements.html")
    parent = driver.find_element(By.NAME, "classes")
    elements = parent.find_elements(By.CLASS_NAME, "one")
    assert 2 == len(elements)


def test_should_find_element_by_tag_name(driver, pages):
    pages.load("nestedElements.html")
    parent = driver.find_element(By.NAME, "div1")
    element = parent.find_element(By.TAG_NAME, "a")
    assert "link1" == element.get_attribute("name")


def test_should_find_elements_by_tag_name(driver, pages):
    pages.load("nestedElements.html")
    parent = driver.find_element(By.NAME, "div1")
    elements = parent.find_elements(By.TAG_NAME, "a")
    assert 2 == len(elements)


def test_should_be_able_to_find_an_element_by_css_selector(driver, pages):
    pages.load("nestedElements.html")
    parent = driver.find_element(By.NAME, "form2")
    element = parent.find_element(By.CSS_SELECTOR, '*[name="selectomatic"]')
    assert "2" == element.get_attribute("id")


def test_should_be_able_to_find_multiple_elements_by_css_selector(driver, pages):
    pages.load("nestedElements.html")
    parent = driver.find_element(By.NAME, "form2")
    elements = parent.find_elements(By.CSS_SELECTOR, '*[name="selectomatic"]')
    assert 2 == len(elements)


def test_should_throw_an_error_if_user_passes_in_invalid_by(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    with pytest.raises(WebDriverException):
        element.find_element("foo", "bar")


def test_should_throw_an_error_if_user_passes_in_invalid_by_when_find_elements(driver, pages):
    pages.load("nestedElements.html")
    element = driver.find_element(By.NAME, "form2")
    with pytest.raises(WebDriverException):
        element.find_elements("foo", "bar")