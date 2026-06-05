---
name: qualificar-leads
description: >
  Filtra uma lista bruta de leads e adiciona diagnóstico de oportunidade para cada um,
  com base nas validações feitas pelo Matheus (tem site? site funciona no celular?
  respondeu no WhatsApp?). Gera lista limpa com apenas os leads qualificados e prontos
  para abordagem. Use quando o Matheus disser "qualificar leads", "filtrar lista",
  "validar leads", "quais leads valem a pena", ou "/qualificar-leads".
---

# /qualificar-leads — Filtro e diagnóstico de leads

Pega a lista bruta do `/prospectar-leads` e devolve só quem tem oportunidade real,
com o diagnóstico específico de cada um para usar na abordagem.

## Passo 1 — Carregar a lista bruta

Perguntar qual arquivo usar (se não veio no comando):

> "Qual arquivo de leads quer qualificar? (está em `dados/` — pode colar o nome ou
> arrastar o arquivo aqui)"

Ler o arquivo indicado e listar os leads numerados para o usuário ter referência.

## Passo 2 — Orientar a validação

Explicar o processo de validação para cada lead da lista:

> "Para cada lead, preciso que você verifique três coisas:
>
> **1. Site:** O lead tem site? Se sim, abre no celular? Carrega rápido?
> → Possíveis diagnósticos: 'Sem site', 'Site fora do ar', 'Site lento no celular', 'Site desatualizado'
>
> **2. WhatsApp:** Manda uma mensagem simples (ex: 'Olá, vi o perfil de vocês!') e cronometra o tempo de resposta.
> → Possíveis diagnósticos: 'Demorou +1h no WhatsApp', 'Não respondeu', 'Sem WhatsApp ativo'
>
> **3. Presença digital geral:** O perfil do Instagram está ativo? Tem posts recentes?
> → Possíveis diagnósticos: 'Insta desatualizado', 'Sem Instagram'
>
> Vai validando e me passando no formato: **[número do lead] — [diagnóstico(s)]**
> Pode mandar conforme for validando, não precisa esperar terminar tudo."

Aguardar as validações. Ir acumulando conforme chegam.

## Passo 3 — Montar a lista qualificada

Filtrar apenas os leads que tiveram pelo menos um diagnóstico de oportunidade.
Montar tabela no formato:

```markdown
# Leads Qualificados — [Data]
> Gerado a partir de: dados/[arquivo-original].md

| # | Nome da Loja | Cidade | Instagram | Telefone/WhatsApp | Diagnóstico | Prioridade |
|---|-------------|--------|-----------|-------------------|-------------|------------|
| 1 | ... | ... | ... | ... | Sem site | Alta |
```

**Critério de prioridade:**
- **Alta:** "Sem site" ou "Site fora do ar" — dor mais óbvia, argumento mais fácil
- **Média:** "Site lento no celular" ou "Demorou +1h no WhatsApp"
- **Baixa:** "Insta desatualizado" ou dores menos críticas

## Passo 4 — Salvar e encerrar

Salvar em `dados/leads-qualificados-[YYYY-MM-DD].md`.

Mostrar resumo:

> "De [total] leads, [N] estão qualificados e salvos em `dados/leads-qualificados-[data].md`.
>
> [N alta prioridade] são alta prioridade — sem site ou site fora do ar.
>
> Próximo passo: roda `/abordar-lead` pra gerar a mensagem personalizada de cada um."

## Regras

- Só incluir leads com diagnóstico real — não qualificar por falta de dado
- Não inventar diagnóstico — registrar exatamente o que o Matheus reportou
- Se o Matheus não conseguiu validar um lead, registrar como `Não validado` e não incluir na lista final
- Sempre sugerir o `/abordar-lead` ao final
