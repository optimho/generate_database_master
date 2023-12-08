import pytest
import myfunctions.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print(f"setting up {method}")

    def teardown_method(self, method):
        print(f"Tearing down {method}")




    def test_one(self):
        assert True