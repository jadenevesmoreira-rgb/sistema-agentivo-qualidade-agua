"""
Harness simplificado do sistema de análise.

Fluxo:
estrutura -> qualidade -> análise -> validação -> relatório
"""

from datetime import datetime


def executar_pipeline(etapas):
    """
    Executa as etapas na ordem definida.

    Cada etapa deve retornar um dicionário contendo:
        {
            "status": "OK" ou "BLOQUEADO",
            "evidencia": "..."
        }

    O pipeline é interrompido caso uma etapa retorne
    o status "BLOQUEADO".
    """

    resultados = []

    for nome, funcao in etapas:
        inicio = datetime.now()

        resultado = funcao()

        registro = {
            "etapa": nome,
            "status": resultado["status"],
            "evidencia": resultado["evidencia"],
            "timestamp": inicio.isoformat(timespec="seconds")
        }

        resultados.append(registro)

        if resultado["status"] == "BLOQUEADO":
            break

    return resultados


def verificar_conclusao(resultados):
    """
    Verifica se todas as etapas executadas foram concluídas
    sem bloqueio.
    """

    if not resultados:
        return False

    return all(
        resultado["status"] == "OK"
        for resultado in resultados
    )
