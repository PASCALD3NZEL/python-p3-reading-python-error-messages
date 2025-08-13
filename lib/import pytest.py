import pytest
import runpy

# lib/test_a_name_error.py


def test_name_error_is_raised():
    with pytest.raises(NameError):
        runpy.run_path('lib/a_name_error.py')