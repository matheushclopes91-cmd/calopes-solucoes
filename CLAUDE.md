# CaLopes Soluções Inteligentes — MazyOS

Operação da CaLopes. Aqui ficam todos os clientes, propostas, conteúdo e entregas da consultoria.

**Estrutura de pastas:**
- `_memoria/` — quem é a CaLopes, como falamos, foco atual
- `identidade/` — marca da CaLopes (aplicada nas peças internas e de clientes)
- `marketing/` — conteúdo institucional da CaLopes
- `saidas/` — documentos pontuais, análises, entregas avulsas
- `dados/` — arquivos a analisar (relatórios de cliente, exports)
- `scripts/` — automações e scripts internos

## Sobre a CaLopes

Consultoria de tecnologia focada em transformar atendimento em vendas. Entrega sites profissionais, automações de WhatsApp e soluções de IA para óticas e pequenos negócios locais.

Atende: proprietários de óticas e pequenos negócios locais que querem melhorar atendimento, captar mais clientes e aumentar vendas com tecnologia.

Serviços principais:
- Sites profissionais
- Automações de atendimento (WhatsApp / IA)
- Estratégia digital para negócios locais

Time: só o Matheus. Horário disponível: seg–sex 19h–22h e sáb 8h–11h45.

## Clientes ativos

*(Atualizar via `/atualizar` conforme novos clientes entrarem)*

## O que mais produzimos aqui

- Propostas comerciais para novos clientes
- Conteúdo para Instagram e WhatsApp da CaLopes
- Scripts de prospecção e abordagem
- Materiais de apresentação e carrosséis

## Tom de voz

Direto, humano e focado em resultado real. Parece que alguém realmente olhou pro negócio do cliente antes de falar — sem enrolação, sem promessa vaga.

Evitar: promessas milagrosas, corporativês ("sinergia", "alavancar", "disruptar"), textos genéricos de copy-paste, tom de guru.

## Regras do sistema

- Cliente novo → criar pasta `clientes/<Nome>/` com briefing e subpastas conforme as entregas contratadas
- Proposta nova → salvar em `saidas/proposta-<cliente>-<data>.html` antes de fechar
- Casos de sucesso → documentar em `clientes/<Nome>/caso.md` (reuso em pitches)
- Tempo é escasso — priorizar ações que atacam o gargalo de prospecção

## Ferramentas conectadas

- [ ] Notion
- [ ] Gmail
- [ ] Google Calendar
- [ ] Canva
- [ ] Meta Ads
- [ ] WhatsApp Business API

*(Marcar conforme for instalando os MCPs)*

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (quando existirem e estiverem preenchidos):

1. `_memoria/empresa.md` — quem é o Matheus, o que faz, como funciona o negócio
2. `_memoria/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` — foco atual, prioridades, prazos

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Pra qualquer tarefa visual (carrossel, post, landing page), consultar `identidade/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe skill relevante em `.claude/skills/`. Se encontrar, seguir as instruções da skill. Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível, perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o padrão de repetição for claro.

---

## Aprender com correções

Quando o Matheus corrigir algo, melhorar uma resposta ou dar uma instrução que parece permanente, perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** → `_memoria/empresa.md`
- **Sobre preferências e estilo** → `_memoria/preferencias.md`
- **Sobre prioridades e foco** → `_memoria/estrategia.md`
- **Regra de comportamento nessa pasta** → próprio `CLAUDE.md`

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante (cliente novo, skill nova, mudança de foco, ferramenta instalada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize a memória?"

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo inteiro.

---

## Criação de skills

Quando o Matheus pedir skill nova:

1. Verificar se existe template relevante em `templates/skills/`
2. Perguntar se é específica desse projeto ou útil em qualquer projeto
3. Ler `_memoria/empresa.md` e `_memoria/preferencias.md` pra calibrar ao contexto da CaLopes
4. Seguir o fluxo da skill-creator nativa do Claude Code
