from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    invalid_key = "a"
    raise_error = TypeError
    assert encrypt_message("abc", invalid_key) == raise_error(
        TypeError, "tipo inválido para key"
    )
    invalid_message = 112233
    assert encrypt_message(invalid_message, 2) == raise_error(
        TypeError, "tipo inválido para message"
    )
    assert encrypt_message("abc", 2) == "a_cba"
    assert encrypt_message("abc", 3) == "cba_"
    assert encrypt_message("abc", 0) == "cba_"
    assert encrypt_message("abc", -1) == "cba_"
    assert encrypt_message("abc", 2) != "bca_"
