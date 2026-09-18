# Sistema Agentivo para Análise da Qualidade da Água

## Sobre o projeto

Este projeto apresenta um sistema de trabalho para análise exploratória e controle de qualidade de dados de monitoramento da qualidade das águas superficiais em Minas Gerais.

A proposta é transformar uma análise que poderia ser realizada de forma ad hoc em um processo estruturado, verificável e reutilizável, combinando operações determinísticas de análise de dados, regras explícitas de controle de qualidade, validação dos achados e documentação da execução.

O sistema foi desenvolvido como parte do desafio técnico para a posição de Cientista de Dados da Amplo Engenharia.

---

## Problema

Dados de monitoramento ambiental podem apresentar valores ausentes, diferenças de cobertura temporal, valores extremos, inconsistências e diferentes formas de representação.

O sistema busca apoiar o analista ambiental na identificação desses aspectos antes da utilização dos dados em análises posteriores.

### Decisão apoiada

Identificar parâmetros, períodos, estações e observações que merecem atenção ou investigação adicional antes de serem utilizados em análises ambientais.

---

## Domínio

**Monitoramento da qualidade das águas superficiais em Minas Gerais, Brasil.**

### Usuário

Analista ambiental ou profissional responsável pela análise de dados de monitoramento.

### Pergunta orientadora

Quais características, limitações e padrões presentes nos dados de monitoramento devem ser considerados antes de sua utilização em análises ambientais?

---

## Dados

A demonstração utiliza dados do **Programa Águas de Minas, do Instituto Mineiro de Gestão das Águas (IGAM)**.

A base principal utilizada na demonstração é:

- **Arquivo:** `Dados_Qualidade_das_Aguas_ate_2019.xlsx`
- **Planilha:** `SH ATÉ DEZ 2019`
- **Registros:** 39.615
- **Estações:** 769
- **Parâmetros disponíveis:** 96
- **Período:** 1997–2019

O arquivo bruto não é versionado neste repositório.

A análise utiliza um conjunto reduzido de 11 parâmetros principais para a demonstração, preservando os demais parâmetros disponíveis na base original.

Os parâmetros selecionados são:

- pH in loco
- Turbidez
- Oxigênio dissolvido
- Temperatura da água
- Condutividade elétrica in loco
- Demanda Bioquímica de Oxigênio
- Fósforo total
- Nitrato
- Sólidos totais
- Nitrogênio amoniacal total
- Coliformes termotolerantes

A seleção considera a relevância para a caracterização da qualidade da água, a relação com dimensões utilizadas pelo IGAM no Índice de Qualidade das Águas (IQA), a cobertura dos dados e a diversidade entre parâmetros físico-químicos e microbiológicos.

---

## Fluxo do sistema

O processo é organizado em etapas:

```text
Entrada
  ↓
Validação da estrutura
  ↓
Controle de qualidade
  ↓
Padronização dos dados
  ↓
Análise exploratória
  ↓
Validação dos achados
  ↓
Relatório
  ↓
Registro da execução
```

### 1. Validação da estrutura
Verifica se a entrada apresenta a estrutura mínima esperada, incluindo estação, data, hora e parâmetros acompanhados de seus respectivos sinais quando aplicável.

### 2. Controle de qualidade
O sistema executa regras explícitas para verificar:
- estrutura;
- completude;
- cobertura temporal;
- consistência;
- possíveis valores extremos;
- cobertura amostral;
- semântica;
- dados ausentes.
As verificações são registradas com status, resultado e evidência.

### 3. Padronização
Os dados são transformados de um formato amplo para um formato longo, permitindo análises por:
- estação;
- período;
- parâmetro;
- valor;
- sinal da medição.
A transformação preserva os valores ausentes e os sinais associados às observações.

### 4. Análise exploratória
São realizadas análises de:
- completude;
- cobertura temporal;
- distribuição dos dados;
- estatísticas descritivas;
- possíveis valores extremos;
- padrões que merecem investigação.

### 5. Validação
Os achados passam por uma etapa específica de validação.
Cada achado deve apresentar:
- evidência observada;
- interpretação;
- conclusão permitida;
- limitações ou conclusão que não pode ser sustentada pelos dados.

### 6. Relatório
Os resultados validados são organizados em um relatório técnico, acompanhado do registro da execução.

### O que torna o processo verificável?
O sistema diferencia operações determinísticas de interpretação.
Operações como contagem, cálculo de cobertura, identificação de duplicidades, transformação dos dados e detecção de candidatos a valores extremos são realizadas por código.
As conclusões não são geradas apenas a partir de interpretação textual: elas dependem das evidências produzidas pelas verificações e passam por uma etapa de validação.
O sistema também preserva os dados originais e registra as decisões relevantes da execução.

### Papel do LLM
O uso de LLM é previsto como uma camada de apoio à interpretação e comunicação dos resultados, e não como substituto das verificações determinísticas.
O LLM pode auxiliar na:
- organização das análises;
- interpretação contextual dos resultados;
- elaboração do relatório;
- comunicação dos achados;
- identificação de hipóteses para investigação.

As operações que exigem reprodutibilidade devem permanecer apoiadas por código e regras explícitas.

### Principais achados da demonstração
A análise da base demonstrou:
- heterogeneidade na cobertura dos diferentes parâmetros;
- elevada cobertura para vários dos parâmetros principais;
- ausência de registros de coliformes termotolerantes entre 2014 e 2019 na base analisada;
- existência de observações que podem ser classificadas como candidatas a valores extremos pelo critério do intervalo interquartil (IQR).
Esses resultados são tratados como evidências para investigação e não como diagnóstico automático de erro de medição ou de condição ambiental.

### Controle de qualidade
O sistema possui 9 regras de controle de qualidade:
| Código | Categoria | Objetivo |
|---|---|---|
| CQ-01 | Estrutura | Verificar elementos estruturais mínimos |
| CQ-02 | Estrutura | Verificar a organização esperada dos parâmetros |
| CQ-03 | Completude | Quantificar valores preenchidos e ausentes |
| CQ-04 | Completude temporal | Verificar cobertura ao longo do tempo |
| CQ-05 | Consistência | Verificar consistência dos dados |
| CQ-06 | Valores extremos | Identificar candidatos a valores extremos |
| CQ-07 | Cobertura amostral | Avaliar a distribuição das amostragens |
| CQ-08 | Semântica | Verificar elementos semânticos relevantes |
| CQ-09 | Dados ausentes | Identificar e registrar dados ausentes |

Os resultados das verificações são registrados para permitir rastreabilidade.

### Rastreabilidade
O processo registra:
- etapa executada;
- regra aplicada;
- status;
- resultado;
- evidência;
- momento da execução.
  
O objetivo é permitir que os resultados apresentados no relatório possam ser relacionados às verificações que os produziram.

### Limitações e escopo
O sistema não pretende:
- estabelecer relações causais;
- produzir diagnóstico ambiental definitivo;
- determinar a causa de dados ausentes;
- classificar automaticamente valores extremos como erros de medição;
- avaliar risco à saúde;
- determinar conformidade regulatória;
- substituir a avaliação de especialistas;
- realizar previsões futuras sem uma pergunta e dados adequados.
  
A ausência de uma evidência ou a baixa cobertura de determinado parâmetro não é interpretada automaticamente como erro dos dados.

### Estrutura do repositório
```text
sistema-agentivo-qualidade-agua/
├── README.md
├── DOMAIN_MANIFEST.yaml
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── analise_qualidade_agua.ipynb
├── data/
│   └── README.md
├── agent/
│   ├── system_prompt.md
│   └── skills.md
├── harness/
│   └── pipeline.py
├── outputs/
│   └── relatorio_final.md
└── tests/
    └── test_quality.py
```

### Execução
A análise principal é apresentada no notebook:
notebooks/analise_qualidade_agua.ipynb
O diretório harness/ contém a estrutura de execução do processo, enquanto tests/ contém verificações automatizadas básicas.
O arquivo DOMAIN_MANIFEST.yaml documenta o domínio, contrato de entrada, escopo, riscos e critérios de conclusão.

### Reprodutibilidade e reutilização
A estrutura foi organizada para que o processo possa ser reutilizado dentro do domínio declarado.
Para uma nova entrada, o sistema deve primeiro verificar sua compatibilidade com o contrato do domínio. Entradas que não atendam aos requisitos mínimos devem ser sinalizadas ou bloqueadas antes da análise.
A separação entre dados, regras, análise, validação e relatório permite adaptar o processo sem eliminar os critérios de controle.

### Fonte dos dados
Instituto Mineiro de Gestão das Águas (IGAM) — Programa Águas de Minas.
Os dados utilizados são provenientes de fonte pública.

### Autoria
Projeto desenvolvido por Jade Neves como parte do desafio técnico para a posição de Cientista de Dados da Amplo Engenharia.
