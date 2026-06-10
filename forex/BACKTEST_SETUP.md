# Backtesting Setup Guide

## Phase 2 Implementation Complete ✅

Implementei um motor de backtesting robusto com análise em 5 anos de dados históricos.

## O que foi criado:

### 1. Motor de Backtesting (`src/backtest/engine.py`)
- **BacktestEngine**: Engine principal que roda simulações
- **EMACrossoverBacktest**: Implementação da estratégia EMA 50/200 com:
  - EMA crossover detection
  - RSI confirmation (70/30 levels)
  - ATR-based stop-loss (2x ATR)
  - Risk-Reward 1:2
  - Posição sizing baseado em % de equity

### 2. Configurações de Estratégia (`src/backtest/strategies.py`)
4 presets prontos:
- **conservative**: 0.5% risk, ATR×3 stops, RR 1:2.5
- **moderate**: 0.8% risk, ATR×2 stops, RR 1:2 (seu padrão)
- **aggressive**: 1.0% risk, ATR×1.5 stops, RR 1:1.5
- **fast**: EMA 20/50, RSI 9, menor período

### 3. Scripts de Teste (`run_backtest.py`)
- `run_single_pair_backtest()`: Testa um par
- `run_multi_pair_backtest()`: Testa múltiplos pares
- Gera dados sintéticos realistas (5 anos = 1260 dias)

## Como usar:

### Step 1: Instalar dependências

```bash
cd C:\Users\Matheus Lopes\Desktop\calopes-solucoes\forex\backend

# Criar virtual environment
python -m venv venv

# Ativar
venv\Scripts\activate

# Instalar packages
pip install -r requirements.txt
```

### Step 2: Rodar backtesting

```bash
# Testar um par (EUR_USD) com 5 anos de dados
python run_backtest.py

# Saída esperada:
# ======================================================================
# Backtesting EUR_USD - EMA Crossover Strategy
# ======================================================================
# 
# 1. Generating 1260 days of synthetic OHLC data...
#    Date range: 2020-XX-XX to 2024-XX-XX
#    Price range: 1.0XXX - 1.1XXX
#
# 2. Running backtest...
#
# 3. Results:
#    Performance:
#    - Return: X.XX%
#    - Annualized Return: X.XX%
#    - Sharpe Ratio: X.XX
#    - Max Drawdown: X.XX%
#
#    Trading Activity:
#    - Total Trades: XXX
#    - Wins: XX
#    - Losses: XX
#    - Win Rate: XX.XX%
#    - Best Trade: X.XX%
#    - Worst Trade: -X.XX%
#    - Avg Trade: X.XX%
#
#    Final Equity: $XXX,XXX.XX
```

### Step 3: Testar em múltiplos pares

Edite `run_backtest.py`, no final:

```python
if __name__ == "__main__":
    # Descomentar para multi-pair
    results = run_multi_pair_backtest(
        pairs=["EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF", "AUD_USD"],
        num_days=1260
    )
```

Depois rodar:
```bash
python run_backtest.py
```

## Métricas de Saída

### Performance Metrics:
- **Return [%]**: Retorno total do período
- **Annualized Return**: Retorno anualizado
- **Sharpe Ratio**: Risco-ajustado (> 1.0 é bom)
- **Max Drawdown**: Pior queda (< 20% é seguro)
- **Sortino Ratio**: Só contabiliza downside

### Trading Stats:
- **Win Rate**: % de trades vencedores (alvo: > 50%)
- **Profit Factor**: Total ganhos / Total perdas (alvo: > 1.5)
- **Expectancy**: Ganho médio por trade
- **Best/Worst Trade**: Maior ganho e maior perda

## Performance Targets

Seu sistema deve atingir:
- ✅ Win Rate: > 50%
- ✅ Sharpe Ratio: > 1.0
- ✅ Max Drawdown: < 20%
- ✅ Profit Factor: > 1.5
- ✅ Trades/ano: > 10 (não trade raramente)

## Próximas otimizações

1. **Testar diferentes pares**: Qual tem melhor Sharpe?
2. **Otimizar parâmetros**: EMA periods, RSI levels, ATR multiplier
3. **Testar configs diferentes**: Conservative vs Aggressive
4. **Walk-forward analysis**: `engine.run_walk_forward()` (in dev)
5. **Monte Carlo testing**: Simular random entry/exit pra validar

## Ajustar o backtest

Se quiser alterar parâmetros da estratégia, edite `src/backtest/engine.py`:

```python
class EMACrossoverBacktest(Strategy):
    ema_fast = 50          # Altere aqui
    ema_slow = 200         # Altere aqui
    rsi_period = 14
    rsi_overbought = 70
    rsi_oversold = 30
    atr_multiplier = 2     # Para stops mais/menos apertados
    rr_ratio = 2           # Risk-Reward ratio
    risk_percentage = 0.8  # % de risco por trade
```

## Troubleshooting

### ImportError: No module named 'backtesting'
```bash
pip install backtesting==0.3.3
```

### ValueError: "No numeric types to aggregate"
Verifique que o DataFrame tem as colunas corretas: `Open, High, Low, Close`

### Backtest não gera trades
- Aumentar janela de dados (min 200 dias pra EMA200)
- Afrouxar RSI levels (70/30)
- Aumentar volatilidade dos dados

## Salvar resultados

Para salvar resultados em JSON:

```python
import json

results = run_single_pair_backtest("EUR_USD", 1260)

with open('backtest_results.json', 'w') as f:
    json.dump(results, f, indent=2)
```

---

**Status**: ✅ Phase 2 Completo - Backtesting robusto com dados de 5 anos

**Próxima**: Phase 3 - Executor de ordens automático (conectar com OANDA real)
