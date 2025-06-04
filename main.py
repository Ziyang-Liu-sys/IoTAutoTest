import pytest
import os
pytest.main()

os.system("allure generate -o report -c temps")