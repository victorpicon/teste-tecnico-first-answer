

Olá! Esse é o teste técnico pra vaga de desenvolvedor(a) na First Answer. Foi desenhado pra ser feito em **cerca de 1 hora**. Leia tudo antes de começar.

A entrevista seguinte parte do que você construiu aqui, então é melhor entregar algo simples e bem pensado do que algo grande e meio quebrado.

---

## Contexto

A First Answer monitora como modelos de IA (ChatGPT, Gemini, Perplexity, etc.) respondem perguntas sobre marcas. Uma das tarefas centrais do produto é, dada uma resposta de IA, identificar **se uma marca específica foi mencionada** e **quais outras marcas aparecem no texto**.

Esse teste te coloca exatamente nesse problema, numa versão reduzida.

---

## O desafio

Construa um script que recebe dois inputs:

- **`texto`** — uma resposta de IA em texto puro (string)
- **`marca_monitorada`** — o nome de uma marca (string)

E retorna:

- **`marca_monitorada_encontrada`** (boolean): se a marca monitorada aparece no texto
- **`outras_marcas`** (array de strings): outras marcas mencionadas no texto

Rode seu script nos **3 casos de teste** que estão no fim deste documento e mostre os 3 outputs.

---

## Stack

**Linguagem: sua escolha — Python ou Node.js (JavaScript/TypeScript).**

Pode usar qualquer biblioteca/pacote que quiser. Não há restrição.

## Abordagem técnica

**Também sua escolha.** Algumas direções possíveis (não exaustivo):

- Lista pré-definida de marcas + matching de strings (regex, fuzzy match, etc.)
- NER (Named Entity Recognition) com bibliotecas como spaCy, transformers, etc.
- Chamada a uma API de LLM pedindo a extração estruturada
- Embeddings + similaridade
- Combinação de várias dessas

Não existe resposta certa. Cada caminho tem trade-offs, escolha um, justifique no README.

### Se for usar API de LLM

Você não precisa pagar nada. Opções com **tier gratuito sem cartão de crédito**:

- **Google AI Studio (Gemini)** — mais generoso, ~1500 req/dia no Flash, contexto enorme.
  → Docs: https://ai.google.dev/gemini-api/docs
- **Groq** — inferência muito rápida com modelos open-source (Llama, Mixtral, etc.). API compatível com OpenAI.
  → Docs: https://console.groq.com/docs

Opções com crédito inicial (exigem cartão de crédito, mas funcionam):

- **Anthropic (Claude)** — https://docs.anthropic.com/

**Se isso for fricção, use Gemini ou Groq.** Estamos avaliando como você pensa o problema, não qual API você escolhe.

---

## Output esperado

JSON estruturado, um por caso de teste:

```json
{
  "own_brand_mentioned": true,
  "other_brands": ["Inter", "C6 Bank", "PicPay"]
}
```

Pode imprimir no terminal, salvar em arquivo, escolher como quiser, só queremos ver os 3 outputs.

---

## Tempo

**Cerca de 1 hora.** Não é exato, se levar 30min ou 2h, tudo bem.

Recompensa por escopo curto e bem pensado é maior do que por escopo grande e meio pronto.

---

## Sobre o uso de IA

**Pode e deve usar.** Cursor, Claude Code, Copilot, ChatGPT, Windsurf, o que estiver no seu fluxo.

O que vamos avaliar não é "você usou IA?", é **como você usa**. Documente no README:

- Quais ferramentas usou
- Um ou dois momentos em que a IA te ajudou bem
- Um ou dois momentos em que a IA te atrapalhou ou produziu algo errado, e como você percebeu

Pode colar trechos de prompt/conversa se quiser. Não é obrigatório.

---

## O que entregar

1. **O código** — repositório no GitHub (público ou privado com acesso), ou .zip.
2. **README.md** com o template abaixo preenchido.
3. **Os 3 outputs** rodando seu script nos 3 casos de teste.

## Template do README

```markdown
# Teste Técnico — First Answer

## Como rodar
[instruções pra rodar o código localmente]

## Abordagem escolhida
[que caminho você escolheu — lista, NER, LLM, etc. — e por quê]

## Como usou ferramentas de IA
[quais ferramentas, momentos bons, momentos ruins]

## Onde isso quebra
[seja honesto: cenários onde seu código vai falhar, decisões que você ficou desconfortável, coisas que cortou por tempo]

## Outputs
[os 3 outputs do seu script]
```

A pergunta "onde isso quebra" é a mais importante, não responda "está ok". Sempre quebra em algum lugar.

---

## Como enviar

Envie o link do repositório ou .zip para: **[rodrigo@firstanswer.ai]**

Prazo: **[07/06/2026]**

Depois de receber, marcamos uma conversa de cerca de 1 hora pra você apresentar o que fez e a gente evoluir o problema junto, ao vivo.

---

## Casos de teste

### Caso 1

**Marca monitorada:** `Nubank`

**Texto:**

"Não existe um único “melhor” cartão de crédito para todo mundo. O melhor depende do que você valoriza: cashback, milhas, ausência de anuidade ou benefícios de viagem.

Com base nas opções mais populares do mercado brasileiro, estas são algumas boas alternativas:

- Nubank: ideal para quem busca simplicidade, aplicativo fácil de usar e geralmente sem anuidade.
- Banco Inter: boa opção para quem quer cashback sem pagar anuidade.
- Nubank Ultravioleta: indicado para quem tem gastos mais elevados e deseja cashback em todas as compras.
- C6 Bank: interessante para quem quer acumular pontos e milhas.
- BTG Pactual Black: recomendado para quem viaja com frequência e valoriza benefícios premium, como acesso a salas VIP.

Sugestões por perfil:

- Se você está começando a usar cartão de crédito: Nubank.
- Se quer cashback sem anuidade: Banco Inter.
- Se gasta mais de R$ 5.000 por mês e busca maior retorno: Nubank Ultravioleta.
- Se o foco é acumular milhas para viajar: C6 Bank ou cartões Black de bancos tradicionais.

Se você informar sua idade, quanto costuma gastar por mês no cartão e se prefere cashback ou milhas, posso indicar a opção mais adequada para o seu perfil."

### Caso 2

**Marca monitorada:** `Nike`

**Texto:**

Para a maioria das pessoas que está começando a correr, a melhor escolha é um tênis de treino diário, com bom amortecimento e conforto, sem necessidade de investir em modelos de competição.

**Melhor custo-benefício: Olympikus Corre 4**

- Marca brasileira muito bem avaliada.
- Leve, confortável e versátil.
- Excelente para quem pretende evoluir dos 5 km para distâncias maiores.

**Melhor para quem busca conforto: Olympikus Corre Max**

- Mais amortecido.
- Ótimo para iniciantes, pessoas mais pesadas ou quem sente mais o impacto da corrida.

**Melhor opção de entrada: Asics Gel-Excite 10**

- Geralmente encontrado por menos de R$ 400.
- Muito confortável para os primeiros meses de corrida.

**Melhor compra sem erro: Mizuno Wave Rider 29**

- Durável, confortável e confiável.
- Frequentemente recomendado por corredores experientes.
- Funciona bem para diferentes tipos de corredores.

**Melhor conforto premium: New Balance Fresh Foam X 1080 v14**

- Um dos tênis mais confortáveis do mercado.
- Excelente para treinos leves e corridas mais longas.
- Custa mais caro, mas entrega uma experiência superior.

Se eu tivesse que indicar apenas um modelo para a maioria dos iniciantes hoje, seria o **Olympikus Corre 4**, por oferecer uma combinação difícil de superar entre conforto, desempenho e preço.

Minha ordem de recomendação para quem está começando seria:

1. Olympikus Corre 4
2. Mizuno Wave Rider 29
3. Asics Gel-Excite 10
4. Olympikus Corre Max
5. New Balance Fresh Foam X 1080 v14

Se você me informar seu peso, orçamento e se pretende correr principalmente na rua ou na esteira, consigo indicar o modelo mais adequado para o seu caso.

### Caso 3

**Marca monitorada:** `First Answer`

**Texto:**

Se o objetivo é monitorar a visibilidade de uma marca em plataformas como ChatGPT, Gemini, Claude, Perplexity e Copilot, algumas soluções se destacam no mercado em 2026.

A Profound é atualmente considerada por muitos a referência do setor. A plataforma oferece monitoramento de presença em diferentes mecanismos de IA, análise de share of voice, inteligência competitiva e identificação dos prompts que geram menções à marca. É uma solução voltada principalmente para empresas de médio e grande porte que desejam estruturar uma estratégia robusta de visibilidade em IA.

A Brandlight tem um foco diferente. Além de medir presença, ela busca entender como a marca está sendo representada pelas IAs. A plataforma analisa narrativa, sentimento, precisão das respostas e possíveis distorções de posicionamento, sendo especialmente interessante para empresas preocupadas com reputação e branding.

A Peec AI vem ganhando espaço como uma alternativa com excelente custo-benefício. Oferece recursos de share of voice, benchmarking de concorrentes, análise das fontes utilizadas pelas IAs e suporte multilíngue, sendo bastante utilizada por startups, scale-ups e agências.

A AthenaHQ é uma solução mais voltada para grandes organizações que precisam segmentar análises por região, público ou unidade de negócio, oferecendo recursos avançados de governança e relatórios executivos.

Já a First Answer possui uma proposta focada na qualidade das respostas geradas pelas IAs. Em vez de apenas medir menções, a plataforma avalia se a marca está sendo apresentada corretamente, se seus diferenciais estão sendo compreendidos pelos modelos e se o posicionamento desejado está sendo refletido nas respostas.

De forma geral, cada plataforma atende a uma necessidade diferente. A Profound se destaca para monitoramento de presença e share of voice. A Brandlight é forte em reputação e narrativa. A Peec AI oferece uma excelente relação custo-benefício. A AthenaHQ atende demandas corporativas mais complexas. E a First Answer se diferencia por analisar a qualidade e a fidelidade da representação da marca pelas IAs.

Para empresas que estão investindo em GEO (Generative Engine Optimization), otimização para LLMs e gestão de percepção de marca em IA, a combinação entre monitoramento de presença, análise de narrativa e avaliação da qualidade das respostas tende a gerar a visão mais completa do mercado.

---

Boa sorte. Qualquer dúvida sobre o enunciado, manda mensagem antes de começar, perguntar é melhor do que adivinhar.
