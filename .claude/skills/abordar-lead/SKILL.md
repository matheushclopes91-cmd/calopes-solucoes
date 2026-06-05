---
name: abordar-lead
description: >
  Gera mensagem de primeiro contato personalizada para um lead qualificado, citando
  o nome real do negócio e a dor específica encontrada na qualificação. O texto sai
  pronto para copiar e enviar no WhatsApp — sem parecer spam. Lê o tom de voz da
  CaLopes antes de escrever. Use quando o Matheus disser "criar mensagem para lead X",
  "gerar abordagem", "escrever mensagem pro WhatsApp", "abordar lead", ou "/abordar-lead".
---

# /abordar-lead — Mensagem de primeiro contato personalizada

Gera texto de abordagem pronto para enviar no WhatsApp. Calibrado com o tom da CaLopes:
direto, humano, mostra que olhou pro negócio — sem enrolação e sem cheiro de spam.

## Dependências

Ler antes de escrever qualquer coisa:
- `_memoria/preferencias.md` — tom de voz, o que evitar
- `_memoria/empresa.md` — nome, o que faz, como se apresenta

## Passo 1 — Receber os dados do lead

Perguntar (se não vieram no comando):

> "Me passa os dados do lead:
> - Nome da loja
> - Diagnóstico (ex: 'Sem site', 'Site lento no celular', 'Demorou 2h no WhatsApp')
>
> Se quiser gerar pra vários de uma vez, cola a lista inteira que eu processo tudo."

Aceitar tanto lead avulso quanto lista inteira do `/qualificar-leads`.

## Passo 2 — Gerar a mensagem

Para cada lead, escrever uma mensagem seguindo a estrutura:

1. **Saudação com nome:** Sempre usar o nome da loja ou do responsável (se souber)
2. **Apresentação rápida:** Nome do Matheus + CaLopes em uma frase — sem pitch longo
3. **Observação específica:** Mencionar a dor concreta encontrada naquele negócio — nunca genérico
4. **Gancho de valor:** O que a CaLopes resolve, ligado diretamente à dor citada
5. **Pergunta de abertura:** Uma pergunta direta e simples para iniciar conversa — não "posso te apresentar?", mas algo que mostre que já pensou na solução

**Exemplo de estrutura aplicada:**
```
Olá! Sou o Matheus da CaLopes Soluções Inteligentes. 😊

Estava olhando o perfil da [Nome da Loja] e notei que [dor específica —
ex: 'vocês ainda não têm um site' / 'o site de vocês não abre direito
no celular' / 'mandei mensagem no WhatsApp e demorou bastante pra ter retorno'].

É exatamente esse tipo de situação que faz a gente perder venda sem perceber.

Ajudamos óticas a resolver isso com [solução direta — site profissional /
atendimento automatizado / página otimizada pra celular].

Posso te mostrar como ficaria pra [Nome da Loja] especificamente?
```

**Adaptar conforme o diagnóstico:**

| Diagnóstico | Observação específica | Solução no gancho |
|-------------|----------------------|-------------------|
| Sem site | "vocês ainda não têm um site" | "site profissional que aparece no Google e passa credibilidade" |
| Site fora do ar | "o site de vocês está fora do ar" | "site estável que não some na hora que o cliente vai ver" |
| Site lento no celular | "o site de vocês demora pra carregar no celular" | "site otimizado pra mobile — onde a maioria das buscas acontece" |
| Demorou no WhatsApp | "mandei mensagem e demorou bastante pra ter retorno" | "automação de atendimento que responde na hora, mesmo fora do horário" |
| Não respondeu | "tentei falar pelo WhatsApp e não tive retorno" | "sistema de atendimento que não deixa cliente sem resposta" |

## Passo 3 — Entregar as mensagens

Apresentar cada mensagem em bloco separado, claramente identificado:

```
---
📍 [Nome da Loja] — Diagnóstico: [diagnóstico]

[mensagem pronta pra copiar]

---
```

Ao final, perguntar:
> "Alguma mensagem que você quer ajustar antes de enviar?"

## Passo 4 — Ajuste (se pedido)

Se o Matheus pedir ajuste, fazer e mostrar só a mensagem ajustada — não todas de novo.

## Regras

- Nunca usar "alavancar", "sinergia", "escalar", "disruptar" ou qualquer corporativês
- Nunca prometer resultado milagroso ("fature 10x mais")
- Nunca soar como template — o nome da loja e o diagnóstico SEMPRE aparecem
- Emoji com moderação: no máximo 1-2 por mensagem, só onde cabe naturalmente
- Tamanho ideal: 5-8 linhas — cabe numa tela de celular sem rolar
- Se vier lista de leads, processar todos e entregar de uma vez
