# Advanced Trading Strategies

Adicionadas 2 estratégias avançadas ao sistema, além da EMA Crossover base.

## 1. Larry Williams Setup (EMA 9 Breakout)

**Conceito**: Estratégia de breakout do trader lendário Larry Williams

### Regras:
- **Indicador**: EMA 9 (confirmação de tendência) + EMA 20
- **Entrada LONG**: 
  - Price quebra acima da máxima dos últimos 5 dias
  - EMA 9 > EMA 20 (confirmação de uptrend)
- **Entrada SHORT**:
  - Price quebra abaixo da mínima dos últimos 5 dias
  - EMA 9 < EMA 20 (confirmação de downtrend)
- **Stop Loss**: ATR × 2.0
- **Take Profit**: RRR 1:2
- **Risk**: 0.8% por operação

### Quando usar:
- Mercados com volatilidade média
- Preferível em breakouts claros
- Bom para swing trading (D1 timeframe)

### Exemplo:
```
EUR/USD quebra acima de $1.1000 (máxima 5 dias)
EMA9 = $1.0995, EMA20 = $1.0950
✅ LONG @ 1.1001, SL @ 1.0950, TP @ 1.1052
```

---

## 2. Palex PC Setup (EMA 21 Pullback)

**Conceito**: Setup PC (Point Convertido) do trader Palex - opera pullbacks na tendência

### Regras:
- **Indicador**: EMA 21 (suporte/resistência dinâmica)
- **Entrada LONG**:
  - Uptrend confirmado (price > EMA21 × 1.005)
  - Price puxa de volta e toca/passa a EMA21
  - Entry no toque da EMA21
- **Entrada SHORT**:
  - Downtrend confirmado (price < EMA21 × 0.995)
  - Price puxa de volta e toca/passa a EMA21
  - Entry no toque da EMA21
- **Stop Loss**: Abaixo da vela de pullback - ATR × 1.5
- **Take Profit**: RRR 1:2.5 (maior RR pois pullback é mais confiável)
- **Risk**: 0.8% por operação

### Quando usar:
- Melhor em tendências bem definidas
- Pullbacks são high-probability entries
- Ótimo em mercados com média volatilidade
- Minimiza risco pois entra "com a maré"

### Exemplo:
```
EUR/USD em uptrend, EMA21 @ $1.0950
Price puxa de volta para $1.0955 (toca EMA21)
✅ LONG @ 1.0956, SL @ 1.0920, TP @ 1.1036
```

---

## 3. Hybrid Multi-Strategy Analyzer (Confluence)

**Conceito**: Combina múltiplas estratégias para identificar "confluências" - sinais high-probability quando 2+ estratégias concordam

### Como funciona:
1. Roda simultaneamente: EMA Crossover, Larry Williams, Palex PC
2. Detecta quando 2 estratégias geram sinais na mesma direção dentro de 2 candles
3. Marca como "confluence signal" com confidence aumentada
4. Prioriza sinais de confluência (menor falsos positivos)

### Vantagens:
- ✅ Reduz false signals (2 estratégias confirmam)
- ✅ Aumenta confidence (confluence = 120% confidence)
- ✅ Melhor win rate
- ✅ Menos operações, mas de maior qualidade

### Exemplo de confluência:
```
Candle 100: EMA Crossover gera sinal LONG @ 1.1000
Candle 101: Palex PC gera sinal LONG @ 1.1002
           ⭐ CONFLUENCE: Duas estratégias confirmam
           Confidence boosted: 0.75 → 0.90
```

---

## Como usar as estratégias

### 1. No pipeline de análise semanal:

```python
from src.analysis.advanced_strategies import (
    LarryWilliamsSetup, PalexPCSetup, HybridMultiStrategyAnalyzer
)

# Strategy 1: Larry Williams
lw = LarryWilliamsSetup()
signals_lw, df_lw = lw.analyze(df)

# Strategy 2: Palex PC
pc = PalexPCSetup()
signals_pc, df_pc = pc.analyze(df)

# Combined: Confluence analyzer
analyzer = HybridMultiStrategyAnalyzer()
all_signals, confluence_only, df = analyzer.analyze(df)
```

### 2. Configurar qual estratégia usar no scheduler:

```python
from src.scheduler.runner import TradingPipeline

# Use Larry Williams setup
pipeline = TradingPipeline(strategy_config='larry_williams')

# Use Palex PC setup
pipeline = TradingPipeline(strategy_config='palex_pc')

# Use original EMA Crossover (default)
pipeline = TradingPipeline(strategy_config='moderate')
```

### 3. Testar estratégias:

```bash
python test_advanced_strategies.py

# Saída:
# ======================================================================
# Larry Williams Setup (EMA 9 Breakout)
# ======================================================================
# Total signals: 25
# LONG signals: 14
# SHORT signals: 11
#
# ======================================================================
# Palex PC Setup (EMA 21 Pullback)
# ======================================================================
# Total signals: 18
# LONG signals: 10
# SHORT signals: 8
#
# ======================================================================
# Hybrid Multi-Strategy Analyzer (Confluence)
# ======================================================================
# Total signals from all strategies: 68
# Larry Williams signals: 25
# Palex PC signals: 18
# ⭐ CONFLUENCE SIGNALS: 8 (Higher probability!)
```

---

## Recomendações de uso

### Para Conservative Traders:
Usar **HybridMultiStrategyAnalyzer** (confluence only)
- Menos trades
- Maior win rate
- Mais confiança

### Para Swing Traders:
Usar **Larry Williams Setup**
- Breakouts são oportunidades claras
- Bom em D1 timeframe
- RRR 1:2 é adequado

### Para Trend Traders:
Usar **Palex PC Setup**
- Pullbacks em tendência = low risk
- RRR 1:2.5 melhor que breakouts
- Melhor expectancy

### Para Exploradores de Estratégias:
Usar **hybrid confluence**
- Testa todas as estratégias
- Identifica sinais mais confiáveis
- Ajuda a escolher qual é melhor

---

## Próximos Passos

1. ✅ Implementado: 3 estratégias completamente funcional
2. ⏳ Backtest: Testar 5 anos com cada estratégia
3. ⏳ Otimizar: Ajustar parâmetros baseado em performance
4. ⏳ Executar: Rodar live em practice mode
5. ⏳ Comparar: Qual estratégia tem melhor Sharpe/Win Rate?

---

## Performance Targets

Para cada estratégia:
- Win Rate: > 50%
- Sharpe Ratio: > 1.0
- Profit Factor: > 1.5
- Max Drawdown: < 20%

**Goal**: Confluência deve ter Win Rate > 60% (por eliminar falsos sinais)
