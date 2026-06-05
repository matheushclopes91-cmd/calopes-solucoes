---
name: prospectar-leads
description: >
  Monta uma lista organizada de leads (óticas e pequenos negócios locais) a partir
  de uma cidade/região e nicho informados. Orienta a pesquisa no Google Maps e Instagram
  e estrutura os dados encontrados em tabela Markdown pronta para a próxima etapa.
  Use quando o Matheus disser "prospectar leads", "buscar óticas em X", "minerar leads",
  "quero uma lista de leads em <cidade>", ou "/prospectar-leads".
---

# /prospectar-leads — Mineração de leads locais

Transforma cidade + nicho em lista estruturada de leads prontos para qualificação.
A pesquisa é assistida: o Claude orienta exatamente o que buscar e como coletar,
o Matheus executa a busca e cola os dados encontrados.

## Passo 1 — Receber os parâmetros

Perguntar (se não vieram junto ao comando):

> "Qual cidade/região e qual nicho? (ex: 'Óticas em Caxias do Sul' ou 'Salões em Bento Gonçalves')"

Se já vieram no comando, confirmar e seguir.

## Passo 2 — Orientar a pesquisa no Google Maps

Gerar a instrução de busca exata:

> "Abre o Google Maps e busca: **'[nicho] em [cidade]'**
>
> Para cada resultado encontrado, copia:
> - Nome da loja
> - Telefone (se aparecer)
> - Site (se tiver no perfil)
> - Link do Maps
>
> Cola aqui quando terminar. Pode ser em texto corrido — eu organizo."

Aguardar o usuário colar os dados brutos.

## Passo 3 — Orientar a pesquisa no Instagram

> "Agora no Instagram, busca: **'[nicho] [cidade]'** ou **'[nicho] [cidade] oficial'**
>
> Para cada perfil relevante encontrado:
> - Nome de usuário (@)
> - Nome exibido
> - Telefone/WhatsApp (se tiver na bio)
> - Link do site (se tiver na bio)
>
> Cola aqui."

Aguardar e cruzar com os dados do Maps para evitar duplicatas.

## Passo 4 — Montar a tabela

Organizar todos os dados coletados no formato:

```markdown
# Leads — [Nicho] em [Cidade] — [Data]

| # | Nome da Loja | Cidade | Instagram | Telefone/WhatsApp | Site | Fonte |
|---|-------------|--------|-----------|-------------------|------|-------|
| 1 | ... | ... | ... | ... | ... | Maps/Insta |
```

Regras de preenchimento:
- Campos sem dado: deixar `—`
- Telefone: formatar como `(XX) XXXXX-XXXX`
- Instagram: incluir o `@`
- Site: incluir só o domínio (sem `https://`)

## Passo 5 — Salvar e encerrar

Salvar o arquivo em `dados/leads-[nicho-slug]-[cidade-slug]-[YYYY-MM-DD].md`.

Mostrar resumo:

> "Lista salva em `dados/leads-[arquivo].md` com [N] leads.
>
> Próximo passo: roda `/qualificar-leads` pra filtrar quem tem mais chances de fechar."

## Regras

- Não inventar dados — só registrar o que o usuário coletou
- Se o usuário colar dados bagunçados, reorganizar sem perguntar
- Não limitar o número de leads — registrar tudo que vier
- Sempre sugerir o `/qualificar-leads` ao final
