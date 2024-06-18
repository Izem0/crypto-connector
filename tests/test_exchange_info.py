import pytest


def test_get_server_time(exchanges):
    for _, exc in exchanges.items():
        assert exc.get_server_time() > 1


if __name__ == "__main__":
    pytest.main([__file__])
