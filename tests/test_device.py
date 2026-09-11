from src.device import (
    get_device_status,
    get_cpu_usage,
    get_memory_usage,
)


def test_device_status():
    assert get_device_status() == "ONLINE"


def test_cpu_usage():
    cpu = get_cpu_usage()
    assert cpu < 80


def test_memory_usage():
    memory = get_memory_usage()
    assert memory < 80
