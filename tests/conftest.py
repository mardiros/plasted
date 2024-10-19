from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def root() -> Path:
    return Path(__file__).parents[1]
