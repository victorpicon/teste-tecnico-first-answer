# Teste Técnico — First Answer

## Como rodar

Requer [uv](https://docs.astral.sh/uv/).

```bash
# 1. Clone e entre no diretório
git clone <repo> && cd <repo>

# 2. Configure sua chave de API do Gemini
cp .env.example .env
# edite .env e substitua "your_key_here" pela sua chave

# 3. Rodar os 3 casos de teste
uv run main.py

# 4. Rodar com input customizado
uv run main.py --texto "Prefiro o Nubank ao Inter" --marca "Nubank"
```

A chave do Gemini é gratuita e não requer cartão de crédito: https://aistudio.google.com/app/apikey

> Um Dockerfile seria simples de adicionar, mas o UV já garante reprodutibilidade total do ambiente — sem necessidade de infraestrutura extra para rodar o script.

## Abordagem escolhida

**Chamada a uma API de LLM (Gemini 2.5 Flash) com extração estruturada em JSON.**

Por quê não as alternativas:

- **Lista estática + regex**: não consegue lidar com marcas desconhecidas. Qualquer texto sobre um setor novo precisaria de curadoria manual constante.
- **NER (spaCy/transformers)**: modelos treinados em corpora genéricos erram em marcas de nicho (fintech brasileiro, marcas compostas como "BTG Pactual Black"). Um modelo fine-tuned resolveria, mas foge do escopo de 1 hora.
- **Embeddings + similaridade**: requer uma lista de referência para comparar — volta ao problema da lista estática.

O LLM (Gemini 2.5 Flash) resolve os casos difíceis naturalmente: "Nubank Ultravioleta" é reconhecido como sub-marca da Nubank, "Fresh Foam" não é uma marca independente da New Balance, "Banco Inter" e "Inter" são a mesma empresa. O `response_mime_type="application/json"` garante saída estruturada sem parsing frágil.

## Como usou ferramentas de IA

**Ferramenta principal:** Claude Code (claude-sonnet-4-6) via CLI.

**Momento em que ajudou bem:** antes de escrever qualquer código, usei o comando `/grill-me` para conduzir uma sessão estruturada de design. O modelo fez perguntas uma a uma sobre cada decisão (linguagem, abordagem, API, estrutura do prompt, tratamento de erro, nomes dos campos de output). Isso evitou retrabalho — todas as decisões relevantes foram tomadas antes da primeira linha de código.

**Momento em que poderia ter atrapalhado:** o modelo sugeriu inicialmente usar apenas os casos hardcoded sem opção de CLI. A ideia fazia sentido para um demo rápido, mas empurrei por um segundo modo (args de linha de comando) porque torna o script mais útil para quem for revisar e quiser testar inputs próprios. O modelo aceitou e implementou — mas se eu tivesse aceitado a primeira sugestão sem questionar, o script seria menos flexível.

## Onde isso quebra

1. **Ambiguidade de nomes de marca**: "Inter" pode ser Banco Inter, Inter Milan ou outra empresa. O LLM escolhe com base no contexto, mas pode errar em textos ambíguos.

2. **Variantes da marca monitorada**: se `marca_monitorada` é "Nubank" e o texto usa uma gíria ou abreviação não óbvia (ex: "o banco roxo"), o modelo pode não reconhecer como a mesma marca.

3. **Textos fora do português/inglês**: o prompt foi escrito em inglês e os casos de teste são em português. Textos em outros idiomas ou scripts não-latinos podem degradar a qualidade da extração.

4. **Alucinação**: o LLM pode, raramente, "ver" uma marca que não está no texto. É incomum com prompts de extração bem definidos, mas não impossível.

5. **Rate limit / dependência de rede**: o tier gratuito do Gemini tem limite de ~1.500 req/dia. A solução não funciona offline e falha se a API estiver fora do ar.

6. **Resposta malformada**: o `response_mime_type="application/json"` do Gemini é confiável, mas não é garantia absoluta. A lógica de retry cobre uma falha, mas com apenas uma retentativa — em produção, isso precisaria de backoff exponencial e circuit breaker. A escolha foi intencional: adicionar retry completo seria over-engineering para um script de 3 casos.

## Outputs

```
--- Case 1 (marca_monitorada: Nubank) ---
{
  "own_brand_mentioned": true,
  "other_brands": [
    "Inter",
    "C6 Bank",
    "BTG Pactual"
  ]
}

--- Case 2 (marca_monitorada: Nike) ---
{
  "own_brand_mentioned": false,
  "other_brands": [
    "Olympikus",
    "Asics",
    "Mizuno",
    "New Balance"
  ]
}

--- Case 3 (marca_monitorada: First Answer) ---
{
  "own_brand_mentioned": true,
  "other_brands": [
    "ChatGPT",
    "Gemini",
    "Claude",
    "Perplexity",
    "Copilot",
    "Profound",
    "Brandlight",
    "Peec AI",
    "AthenaHQ"
  ]
}
```
