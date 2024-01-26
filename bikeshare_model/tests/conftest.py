# bikeshare_model/tests/conftest.py
# bikeshare_model/tests/conftest.py
import pytest
from bikeshare_model.config.core import config, create_and_validate_config
from bikeshare_model.processing.data_manager import load_pipeline


@pytest.fixture(scope="session")
def test_config():
    # Load or modify configuration specific to tests if needed
    return create_and_validate_config()


@pytest.fixture(scope="session")
def trained_model(test_config):
    pipeline_file_name = f"{test_config.app_config.pipeline_save_file}{test_config.app_config.version}.pkl"
    _pipeline = load_pipeline(file_name=pipeline_file_name)
    return _pipeline


# Add other fixtures as needed
