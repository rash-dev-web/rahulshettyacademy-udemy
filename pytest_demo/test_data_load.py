import pytest
from pytest_demo.base_class import BaseClass


@pytest.mark.usefixtures("data_load")
class TestDataLoad(BaseClass):

    def test_use_data(self, data_load):
        log = self.get_logger()
        print(data_load)
        log.info(data_load)
        log.debug(data_load[0])
