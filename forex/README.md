# Forex Trading System - Análise Técnica + Automação

Sistema de operações proprietárias com análise técnica (EMA Crossover), backtesting de 5 anos e execução automática.

## Arquitetura

- **Backend**: Python + FastAPI + SQLAlchemy
- **Broker**: OANDA v20 API
- **Estratégia**: EMA 50/200 Crossover com confirmação RSI
- **Automação**: APScheduler (sábado 14h análise, domingo 17h execução)
- **Pares**: 20 majors
- **Risk**: 0.8% do capital por operação

## Setup

### 1. Criar Virtual Environment

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar OANDA

1. Criar conta em https://fxpractice.oanda.com (practice) ou https://fxtrade.oanda.com (live)
2. Gerar API token em Account Settings → API Access
3. Copiar `.env.example` → `.env`
4. Preencher `OANDA_ACCOUNT_ID` e `OANDA_ACCESS_TOKEN`

### 4. Inicializar Banco de Dados

```bash
python
>>> from src.db.models import Base
>>> from sqlalchemy import create_engine
>>> engine = create_engine("sqlite:///quotes.db")
>>> Base.metadata.create_all(engine)
>>> exit()
```

## Uso

### Executar API

```bash
python -m uvicorn src.api.main:app --reload
```

API disponível em `http://localhost:8000`
Docs: `http://localhost:8000/docs`

### Executar Scheduler

```bash
python src/scheduler/tasks.py
```

### Executar Análise Manual

```bash
python
>>> from src.broker.client import OANDAClient
>>> from src.analysis.signals import EMACrossoverStrategy
>>> import pandas as pd
>>> 
>>> client = OANDAClient()
>>> pair = "EUR_USD"
>>> df = client.get_quotes(pair, granularity="D", count=500)
>>> 
>>> strategy = EMACrossoverStrategy(risk_percentage=0.8)
>>> signals, analyzed_df = strategy.analyze(df)
>>> print(signals)
```

## Estrutura de Pastas

```
backend/
├── src/
│   ├── analysis/
│   │   ├── indicators.py      # EMA, RSI, ATR, MACD, BB
│   │   └── signals.py         # EMACrossoverStrategy
│   ├── backtest/              # TODO: Motor de backtesting
│   ├── broker/
│   │   ├── client.py          # Cliente OANDA
│   │   └── executor.py        # TODO: Executor de ordens
│   ├── db/
│   │   └── models.py          # SQLAlchemy models
│   ├── api/
│   │   └── main.py            # FastAPI app
│   └── scheduler/
│       └── tasks.py           # APScheduler tasks
├── requirements.txt
├── .env.example
└── .env (local, não commitar)
```

## Próximas Fases

- [ ] **Phase 2**: Motor de backtesting (backtrader/backtesting.py)
- [ ] **Phase 3**: Executor de ordens + gerenciamento de posições
- [ ] **Phase 4**: Endpoints de API mais robustos + persistência em DB
- [ ] **Phase 5**: Dashboard React (gráficos D1/W1, histórico, sinais)
- [ ] **Phase 6**: Containerização (Docker) + deployment

## Performance Target

- Win Rate: > 50%
- Sharpe Ratio: > 1.0
- Max Drawdown: < 20%
- Profit Factor: > 1.5

## Avisos

⚠️ **Paper Trading**: Sempre testar em practice mode por 2-3 semanas antes de usar com capital real

⚠️ **Risk Management**: 0.8% de risco por operação = máximo 100 operações perdidas consecutivas antes de zerem a conta

⚠️ **Market Hours**: Execução programada para Sunday 17:00 (1 hora antes da abertura do mercado)
