from challenges.challenge_encrypt_message import encrypt_message

# import pytest


def test_encrypt_message():
    # with pytest.raises(TypeError, match="tipo inválido para key"):
    #     encrypt_message("abc", "a")
    # with pytest.raises(TypeError, match="tipo inválido para message"):
    #     encrypt_message(123, 2)
    assert encrypt_message("teste", 2) == "ets_et"
    assert encrypt_message("teste", 1) == "t_etse"
    assert encrypt_message("abc", "a") == TypeError("tipo inválido para key")
    assert encrypt_message(123, 2) == TypeError("tipo inválido para message")
