from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    assert encrypt_message("abc", 2) == "a_cba"
    assert encrypt_message("abc", 3) == "cba_"
    assert encrypt_message("abc", 0) == "cba_"
    assert encrypt_message("abc", -1) == "cba_"
    with pytest.raises(TypeError) as error:
        encrypt_message("abc", "a")
        assert str(error.value) == "tipo inválido para key"
    with pytest.raises(TypeError) as error:
        encrypt_message(112233, 2)
        assert str(error.value) == "tipo inválido para message"
    # assert encrypt_message("abc", "a") == TypeError("tipo inválido para key")
    # assert encrypt_message(112233, 2) == TypeError(
    #     "tipo inválido para message"
    # )
    # assert encrypt_message("abc", 2) == "a_cba"
    # assert encrypt_message("abc", 3) == "cba_"
    # assert encrypt_message("abc", 0) == "cba_"
    # assert encrypt_message("abc", -1) == "cba_"
    # assert encrypt_message("abc", 2) != "bca_"
