# 📊 Resultados de Backtest — Larry Williams System

Histórico de testes realizados para validação da estratégia em diferentes mercados e timeframes.

---

## 📋 Template de Teste

Use este formato ao adicionar novos resultados:

```
## Teste #[N] — [Ativo] [Timeframe] [Data]

**Período:** [Data Início] a [Data Fim] | [Dias de teste]
**Ativo:** [EURUSD / BTCUSD / etc]
**Timeframe:** [1min / 5min / 15min / 1H / 4H / D]
**Configuração:** [Básica / Intermediária / Agressiva]

### Parâmetros
- EMA 9, 21, 50
- Setup 9.1: [ON/OFF]
- Setup 9.2: [ON/OFF]
- Setup 9.3: [ON/OFF]
- Filtros: [descrição]
- RR: [valor]

### Resultados
| Métrica | Valor |
|---------|-------|
| Total de Trades | [N] |
| Trades Vencedores | [N] ([%]) |
| Trades Perdedores | [N] ([%]) |
| Taxa de Acerto | [N%] |
| Profit Factor | [N.NN] |
| Lucro Líquido | [R$] |
| Drawdown Máximo | [%] |
| Expectância por Trade | [R$] |
| Sharpe Ratio | [N.NN] |

### Observações
- [O que funcionou bem]
- [O que não funcionou]
- [Ajustes para próximo teste]
```

---

## 🧪 Testes Realizados

### Status: Aguardando Primeiro Teste

Nenhum backtest foi realizado ainda. 

**Próximos passos:**

1. **Teste Piloto — EURUSD 1H**
   - Período: Últimos 3 meses
   - Objetivo: Validar lógica dos sinais
   - Configuração: Básica (sem filtros)

2. **Teste Principal — EURUSD 1H (1 ano)**
   - Período: 2025-06 a 2026-06
   - Objetivo: Performance real
   - Configuração: Intermediária (com ADX + Volume)

3. **Testes em Outros Ativos**
   - GBPUSD (Forex)
   - BTCUSD (Cripto)
   - SPX500 (Índice)

---

## 📈 Métricas Explicadas

### Taxa de Acerto
```
(Trades Vencedores / Total de Trades) × 100

Exemplo: 12 wins em 20 trades = 60% taxa de acerto
```

### Profit Factor
```
(Lucro Total de Vencedores) / (Perda Total de Perdedores)

Ideal: > 1.5 (significando que para cada $1 perdido, ganha $1.50)
```

### Drawdown Máximo
```
Maior queda de capital durante o período

Exemplo: Capital sai de $10.000 para $8.000 = 20% drawdown
```

### Expectância
```
(Taxa Acerto × Média Ganho) - (Taxa Erro × Média Perda)

Exemplo:
- Taxa acerto: 60%
- Média ganho: $200
- Taxa erro: 40%
- Média perda: $100
- Expectância = (0.6 × 200) - (0.4 × 100) = $120 - $40 = $80 por trade
```

### Sharpe Ratio
```
Mede risco-ajustado do retorno

Ideal: > 1.0
Excelente: > 2.0
```

---

## 🎯 Benchmarks (Esperados)

### Configuração Básica (Setup 9.1, 9.2, 9.3 sem filtros)
- Taxa de Acerto: 48-52%
- Profit Factor: 1.2-1.4
- Drawdown: 25-35%

### Configuração Intermediária (Com ADX + Volume)
- Taxa de Acerto: 55-65%
- Profit Factor: 1.6-2.0
- Drawdown: 15-25%

### Configuração Agressiva (Apenas Setup 9.3)
- Taxa de Acerto: 65-75%
- Profit Factor: 2.0-3.0
- Drawdown: 10-20%

---

## 🔍 Como Fazer Seu Próprio Backtest

### Opção 1: TradingView Nativo (Recomendado)

1. **Copie a Strategy** (`strategy-larry-williams.pine`)
2. **Adicione ao gráfico**
3. **Abra Strategy Tester** (lado direito)
4. **Configure datas:**
   - Data início: 1º do mês anterior
   - Data fim: Hoje
5. **Clique "Start Backtest"**
6. **Aguarde processamento** (pode levar minutos)
7. **Analise resultados na aba "Results"**

### Opção 2: Exportar para Análise Offline

1. Clique em **"Export"** no Strategy Tester
2. Salve o CSV
3. Abra em Excel/Google Sheets
4. Analise cada trade individualmente

---

## 📊 Template para Análise Detalhada

Se quiser analisar trade-por-trade:

| # | Data | Hora | Ativo | Setup | Entrada | SL | TP | Saída | P&L | RR Alcançado |
|---|------|------|-------|-------|---------|----|----|-------|-----|--------------|
| 1 | 2026-01-15 | 14:30 | EURUSD | 9.1 | 1.1050 | 1.1040 | 1.1070 | 1.1072 | +22 | 1:2.2 |
| 2 | 2026-01-15 | 16:45 | EURUSD | 9.2 | 1.1072 | 1.1065 | 1.1095 | 1.1058 | -14 | 1:(-1.4) |

---

## 🎬 Próximas Ações

- [ ] Realizar primeiro backtest (EURUSD 3 meses)
- [ ] Documentar resultados nesta página
- [ ] Comparar Setup 9.1 vs 9.2 vs 9.3
- [ ] Testar em 4 ativos diferentes
- [ ] Otimizar parâmetros se necessário
- [ ] Realizar forward test (papel trading 2-4 semanas)
- [ ] Iniciar trading real com posição mínima

---

## 💡 Dicas para Backtest Confiável

✅ **Use pelo menos 3 meses de dados** — Sua amostra precisa ser significativa

✅ **Teste em múltiplos ativos** — O sistema pode não funcionar em tudo

✅ **Inclua custos reais** — Commission e slippage são realidade

✅ **Verifique cada trade manualmente** — A lógica do código está correta?

✅ **Forward test antes de dinheiro real** — Papéis trading por 2-4 semanas

❌ **Não optimize demais** — Overfitting é armadilha comum

❌ **Não ignore drawdown** — Qualidade importa mais que puro retorno

---

## 📞 Dúvidas?

Matheus: matheushclopes91@gmail.com

---

**Última atualização:** Junho 2026  
**Status:** Aguardando teste piloto
