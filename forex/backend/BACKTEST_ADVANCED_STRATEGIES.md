# Backtesting Advanced Strategies

Guia prático para testar as 3 estratégias avançadas de forex.

---

## Estratégias a Testar

### 1️⃣ **EMA Crossover (Base)**
- **EMAs**: 50 (rápida) / 200 (lenta)
- **Confirmação**: RSI 70/30
- **Stops**: ATR × 2.0
- **RRR**: 1:2
- **Risco**: 0.8% por operação
- **Perfil**: Trader conservador, segue tendências principais

### 2️⃣ **Larry Williams Setup (EMA 9)**
- **EMAs**: 9 (rápida) / 20 (lenta)
- **Entrada**: Breakout acima/abaixo máxima/mínima 5 dias
- **Confirmação**: EMA 9 > EMA 20 (uptrend) ou EMA 9 < EMA 20 (downtrend)
- **Stops**: ATR × 2.0
- **RRR**: 1:2
- **Risco**: 0.8% por operação
- **Perfil**: Swing trader, aproveita breakouts claros

### 3️⃣ **Palex PC Setup (EMA 21)**
- **EMA**: 21 (suporte/resistência dinâmica)
- **Entrada**: Pullback para EMA 21 em tendência estabelecida
- **Confirmação**: Uptrend (price > EMA21 × 1.005) ou Downtrend (price < EMA21 × 0.995)
- **Stops**: ATR × 1.5 (mais apertado pois pullback é mais seguro)
- **RRR**: 1:2.5 (maior risco-recompensa)
- **Risco**: 0.8% por operação
- **Perfil**: Trend trader, entra "com a maré"

### 4️⃣ **Hybrid Confluence (Multi-Estratégia)**
- **Combines**: EMA Crossover + Larry Williams + Palex PC
- **Sinal confluência**: 2+ estratégias concordam (mesma direção, dentro de 2 candles)
- **Benefício**: Reduz falsos sinais (+20% confidence boost)
- **Perfil**: Trader conservador com foco em alta probabilidade

---

## Setup Passo-a-Passo

### Step 1: Instalar Python 3.9+

Baixe em: https://www.python.org/downloads/

**Important**: Marque "Add Python to PATH"

Verifique instalação:
```bash
python --version
```

### Step 2: Clonar/Navegar para pasta

```bash
cd C:\Users\Matheus Lopes\Desktop\calopes-solucoes\forex\backend
```

### Step 3: Criar Virtual Environment

```bash
python -m venv venv
```

Ativar:
```bash
# Windows PowerShell
venv\Scripts\Activate.ps1

# Ou Windows CMD
venv\Scripts\activate.bat
```

### Step 4: Instalar Dependências

```bash
pip install -r requirements.txt
```

Verifique instalação:
```bash
pip list | grep backtesting
```

Deve retornar: `backtesting 0.3.3`

---

## Rodar Backtests

### Opção A: Testar Apenas EMA Crossover (rápido)

```bash
python run_backtest.py
```

**Output esperado:**
```
======================================================================
Backtesting EUR_USD - EMA Crossover Strategy
======================================================================

1. Generating 1260 days of synthetic OHLC data...
   Date range: 2020-XX-XX to 2024-XX-XX
   Price range: 1.0XXX - 1.1XXX

2. Running backtest...

3. Results:
   Performance:
   - Return: X.XX%
   - Annualized Return: X.XX%
   - Sharpe Ratio: X.XX
   - Max Drawdown: X.XX%

   Trading Activity:
   - Total Trades: XXX
   - Wins: XX
   - Losses: XX
   - Win Rate: XX.XX%
   - Best Trade: X.XX%
   - Worst Trade: -X.XX%
   - Avg Trade: X.XX%

   Final Equity: $XXX,XXX.XX
```

### Opção B: Testar TODAS as estratégias (recomendado)

```bash
python run_all_strategies_backtest.py
```

**Output esperado:**
```
======================================================================
COMPARISON TABLE - All Strategies
======================================================================

                Strategy  ...  Total Signals  Avg Confidence
          EMA Crossover  ...            45           0.68
        Larry Williams   ...            25           0.75
           Palex PC      ...            18           0.80
   Hybrid Confluence     ...            68           0.80 (⭐ High Prob)

======================================================================
RECOMMENDATIONS
======================================================================

✅ Confluence Analyzer detected 28.6% of signals as high-probability
   → Use confluence-only signals to reduce false positives

Next steps:
1. Compare Sharpe ratios across strategies
2. Test on other pairs (GBP/USD, USD/JPY, etc)
3. Run with live data (not synthetic)
4. Paper trade for 2-3 weeks before going live
```

---

## Interpretar Resultados

### Performance Metrics (Backtesting.py)

| Métrica | Alvo | O que significa |
|---------|------|-----------------|
| **Return %** | > 10% a.a. | Ganho total no período |
| **Sharpe Ratio** | > 1.0 | Risco ajustado (>1.0 = bom) |
| **Win Rate** | > 50% | % de operações vencedoras |
| **Profit Factor** | > 1.5 | Total ganhos / Total perdas |
| **Max Drawdown** | < 20% | Pior queda de capital |
| **Best Trade** | > 2% | Maior ganho em 1 trade |

### Exemplo: Analisando Resultados

```
EMA Crossover:
- Sharpe: 1.45 ✅ (> 1.0)
- Win Rate: 58% ✅ (> 50%)
- Profit Factor: 2.1 ✅ (> 1.5)
→ Estratégia é robusta

Larry Williams:
- Sharpe: 0.82 ❌ (< 1.0)
- Win Rate: 45% ❌ (< 50%)
- Profit Factor: 1.2 ❌ (< 1.5)
→ Precisa otimização

Palex PC:
- Sharpe: 1.8 ✅ (> 1.0)
- Win Rate: 65% ✅ (> 50%)
- Profit Factor: 2.8 ✅ (> 1.5)
→ MELHOR estratégia!

Hybrid Confluence:
- Signals: 28.6% de confluência
- Confidence avg: 0.80 (vs 0.75 individual)
→ Reduz falsos sinais
```

---

## Otimizações Possíveis

### Se Win Rate < 50%:
```python
# Em src/backtest/engine.py, classe EMACrossoverBacktest:
atr_multiplier = 3.0  # ← Aumentar para stops mais largos
rsi_overbought = 65   # ← Relaxar RSI levels
rsi_oversold = 35
```

### Se Sharpe < 1.0:
```python
# Aumentar EMA periods (mais conservador)
ema_fast = 100   # ← Era 50
ema_slow = 300   # ← Era 200
```

### Se Profit Factor < 1.5:
```python
# Aumentar RRR
rr_ratio = 2.5   # ← Era 2.0
```

---

## Testar em Múltiplos Pares

No arquivo `run_all_strategies_backtest.py`, adicione:

```python
# Testar múltiplos pares
pairs = ["EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF", "AUD_USD"]

for pair in pairs:
    print(f"\nTesting {pair}...")
    test_ema_crossover(pair, num_days=1260)
    test_larry_williams(pair, num_days=1260)
    test_palex_pc(pair, num_days=1260)
```

---

## Performance Targets (Seu Sistema)

Seu sistema deve atingir NO MÍNIMO:

| Métrica | Target | Sua Estratégia | Status |
|---------|--------|----------------|--------|
| Win Rate | > 50% | ? | ? |
| Sharpe Ratio | > 1.0 | ? | ? |
| Profit Factor | > 1.5 | ? | ? |
| Max Drawdown | < 20% | ? | ? |
| Trades/ano | > 12 | ? | ? |

**Preenchir após rodar backtest**

---

## Troubleshooting

### Erro: "No module named 'backtesting'"
```bash
pip install backtesting==0.3.3
```

### Erro: "No numeric types to aggregate"
Verifique que DataFrame tem colunas corretas:
```python
# Deve ter estas colunas (case-sensitive):
df.columns = ['Open', 'High', 'Low', 'Close']
```

### Backtest não gera trades
- Aumentar `num_days` (min 200 pra EMA 200)
- Relaxar RSI levels: `rsi_overbought=65, rsi_oversold=35`
- Aumentar volatilidade dos dados

### Backtesting muito lento
- Reduzir `num_days` (ex: 500 em vez de 1260)
- Testar menos pares (ex: EUR_USD só)

---

## Salvar Resultados

```python
# No final de run_all_strategies_backtest.py:
import json

with open('backtest_results.json', 'w') as f:
    json.dump(all_results, f, indent=2)

print("✅ Resultados salvos em backtest_results.json")
```

---

## Próximas Etapas (Após Backtesting)

1. ✅ **Escolher melhor estratégia** baseado em Sharpe/Win Rate
2. ⏳ **Otimizar parâmetros** (EMA periods, ATR multiplier, RRR)
3. ⏳ **Testar em pares reais** (usar dados de OANDA)
4. ⏳ **Paper trading** (2-3 semanas sem risco real)
5. ⏳ **Go live** em prática (1 semana)
6. ⏳ **Go live** com pequeno capital (se tudo OK)

---

## Contato / Debug

Se encontrar problemas:
1. Verifique Python version: `python --version` (deve ser 3.9+)
2. Verifique dependências: `pip list`
3. Rode um teste simples: `python -c "import pandas; print(pandas.__version__)"`
