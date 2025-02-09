import pytest
from src.classes import Category


@pytest.fixture()
def test_class_category():
    return Category()


def test_category_count():
    passed = Category().category_count == 0
    if passed:
        cat1 = Category()
        cat2 = Category()
        passed = Category().category_count == 2

        if passed:
            del cat1
            passed = Category().category_count == 1

            if passed:
                del cat2
                passed = Category().category_count == 0
    assert passed
