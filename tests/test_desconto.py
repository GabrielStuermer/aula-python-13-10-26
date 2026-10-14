from desconto import calcular_desconto

def test_desconto_de_10_porcento():
    resultado = calcular_desconto(100, 10)

    assert resultado == 90

def test_sem_desconto():
    resultado = calcular_desconto(100, 0)

    assert resultado == 100

def test_desconto_acima_do_limite():
    resultado = calcular_desconto(100, 51)

    assert resultado == 50

def test_desconto_negativo():
    resultado = calcular_desconto(100, -10)
    assert resultado == 100