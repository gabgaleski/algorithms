import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("python", 1) == "p_nohty"
    assert encrypt_message("python", 2) == "noht_yp"
    assert encrypt_message("python", 13) == "nohtyp"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('python', 'a')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 2)
