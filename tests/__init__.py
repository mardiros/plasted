import os
import sys
from pathlib import Path

root = Path(__file__).parent
fake_packages = root / "dummy_packages"
for dirs in fake_packages.iterdir():
    sys.path.insert(0, str(dirs))

os.environ["PLASTER_URI"] = "file+yaml://test.yaml"
