from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abc", "a")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 2)
    assert encrypt_message("menssagem", 2) == "megassn_em"
    assert encrypt_message("menssagem", 1) == "m_megassne"
    assert encrypt_message("menssagem", -1) == "megassnem"
