import pytest
from commons.simulator_controller import SimulatorController


@pytest.fixture(scope="function")
def simulator():
    sim = SimulatorController()
    yield sim
    sim.close()