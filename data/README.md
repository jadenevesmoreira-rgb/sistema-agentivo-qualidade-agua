# Dados

A demonstração deste projeto utiliza dados públicos do Programa Águas de Minas, do Instituto Mineiro de Gestão das Águas (IGAM).

## Base utilizada

Arquivo de demonstração:

`Dados_Qualidade_das_Aguas_ate_2019.xlsx`

Planilha principal:

`SH ATÉ DEZ 2019`

A base utilizada na demonstração possui 39.615 registros, 769 estações e 96 parâmetros, cobrindo o período de 1997 a 2019.

O arquivo bruto não é versionado neste repositório.

## Estrutura esperada

A unidade de observação é uma amostragem identificada por:

- Estação
- Data de Amostragem
- Hora de Amostragem

Os parâmetros podem estar organizados em pares de colunas:

- parâmetro
- Sinal parâmetro

O sistema preserva valores ausentes e sinais associados às observações.

## Transformação analítica

Para a análise exploratória, os dados podem ser transformados de formato amplo para formato longo, mantendo:

- estação;
- data;
- hora;
- parâmetro;
- valor;
- sinal.

A transformação não altera a base original.

## Fonte

Programa Águas de Minas — Instituto Mineiro de Gestão das Águas (IGAM).
