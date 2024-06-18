import pytest


def test_get_api_key_info(exchanges):
    for _, exc in exchanges.items():
        info = exc.get_api_key_info()
        assert info["timestamp"] > 0


def test_get_balance(exchanges):
    for _, exc in exchanges.items():
        balance = exc.get_balance()
        assert balance["equity"] >= 0
        assert isinstance(balance["assets"], dict)


def test_get_transfer_history(exchanges):
    for _, exc in exchanges.items():
        transfers = exc.get_transfer_history()
        assert isinstance(transfers, list)


if __name__ == "__main__":
    pytest.main([__file__])
