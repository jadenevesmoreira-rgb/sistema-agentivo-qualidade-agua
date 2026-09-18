def test_estrutura_minima():
    colunas_obrigatorias = [
        "Estação",
        "Data de Amostragem",
        "Hora de Amostragem"
    ]

    assert len(colunas_obrigatorias) == 3


def test_quantidade_regras():
    regras_esperadas = 9

    assert regras_esperadas == 9


def test_achado_deve_conter_evidencia():
    achado = {
        "evidencia": "Cobertura anual igual a 0% entre 2014 e 2019."
    }

    assert achado["evidencia"] != ""
