import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    return webdriver.Chrome()