from app.utils.generate_code import generate_code


# тест на то что код равен по длине
def test_generate_code_length():
    code = generate_code.generate_verification_code()
    assert len(code) == 6


# тест на то что код состоит только из цифр
def test_generate_code_int():
    code = generate_code.generate_verification_code()
    assert code.isnumeric()


# тест на то чтоб код не дублировался
def test_generate_code_duplicate():
    code1 = generate_code.generate_verification_code()
    code2 = generate_code.generate_verification_code()
    assert code1 != code2
