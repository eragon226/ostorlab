import pytest
import time
from ostorlab.runtimes.local.services import mq

@pytest.fixture()
def mq_service():
    lrm = mq.LocalRabbitMQ(name='core_mq', network='test_network', exposed_ports={5672:5672})
    lrm.start()
    time.sleep(3)
    yield lrm
    lrm.stop()


