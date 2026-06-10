# Dashboard Setup Guide

Complete setup para rodar o sistema completo de análise forex com dashboard interativo.

## Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                    Browser (Port 3000)                      │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Next.js/React Dashboard (frontend/)               │    │
│  │  - ChartD1W1 (gráficos candlestick)                │    │
│  │  - OpportunitiesList (sinais)                      │    │
│  │  - OperationHistory (trades)                       │    │
│  │  - StrategyMetrics (backtesting)                   │    │
│  └────────────────────────────────────────────────────┘    │
│                           ↓ (HTTP requests)                 │
├─────────────────────────────────────────────────────────────┤
│                    FastAPI Backend (Port 8000)              │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Python Backend (backend/)                         │    │
│  │  - API routes (/api/opportunities, etc)            │    │
│  │  - Analysis engine (EMA, Larry Williams, Palex)    │    │
│  │  - Backtesting engine                              │    │
│  │  - Scheduler (sábado 14h, domingo 17h)             │    │
│  └────────────────────────────────────────────────────┘    │
│                           ↓ (SQL queries)                   │
├─────────────────────────────────────────────────────────────┤
│                     SQLite Database                         │
│  - Quotes (OHLC histórico)                                 │
│  - Signals (sinais gerados)                                │
│  - Operations (trades executados)                          │
└─────────────────────────────────────────────────────────────┘
```

## Setup Passo-a-Passo

### Terminal 1: Backend Python

```bash
cd C:\Users\Matheus Lopes\Desktop\calopes-solucoes\forex\backend

# Criar virtual environment (primeira vez)
python -m venv venv

# Ativar
venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor FastAPI
python -m uvicorn src.api.main:app --reload --port 8000
```

**Output esperado:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Terminal 2: Frontend React

```bash
cd C:\Users\Matheus Lopes\Desktop\calopes-solucoes\forex\frontend

# Instalar dependências (primeira vez)
npm install

# Rodar em desenvolvimento
npm run dev
```

**Output esperado:**
```
> forex-dashboard@1.0.0 dev
> next dev

  ▲ Next.js 14.0.0
  - Local:        http://localhost:3000
```

### Acessar Dashboard

Abra seu navegador em: **http://localhost:3000**

---

## Dashboard Componentes

### 🎯 Seletor de Pares (Topo)

Clique para mudar entre pares:
- EUR_USD, GBP_USD, USD_JPY, USD_CHF, AUD_USD, etc.

Cada clique carrega dados específicos do par.

### 📊 Gráfico Candlestick (Esquerda)

- **Velas verdes**: Candles up (close > open)
- **Velas vermelhas**: Candles down (close < open)
- **Linha azul**: EMA 50 (tendência rápida)
- **Linha laranja**: EMA 200 (tendência lenta)
- **Botões D1/W1**: Mudar timeframe

### 📈 Oportunidades (Centro-Esquerda)

Sinais gerados pelas estratégias:
- **LONG** (verde): Entrada de compra
- **SHORT** (vermelho): Entrada de venda
- **⭐ Confluência**: 2+ estratégias confirmam

Cada oportunidade mostra:
- Entry price
- Stop Loss (vermelho)
- Take Profit (verde)
- Confidence %
- Botão "Execute" para entrar no trade

### 📋 Histórico (Direita)

Operações fechadas:
- CLOSED_WIN (verde) - Trades vencedores
- CLOSED_LOSS (vermelho) - Trades perdedores
- OPEN (azul) - Trades abertos

Estatísticas:
- Total de trades
- Win rate %
- Operações abertas

### 📊 Métricas (Canto Superior Direito)

Backtesting metrics:
- **Sharpe Ratio** (alvo: > 1.0)
- **Win Rate** (alvo: > 50%)
- **Profit Factor** (alvo: > 1.5)
- **Max Drawdown** (alvo: < 20%)

Status: ✅ Ready ou ⚠️ Needs Optimization

---

## Usar o Dashboard

### 1. Monitorar oportunidades

- Selecione um par
- Observe o gráfico D1/W1
- Veja sinais em "Oportunidades"

### 2. Executar trades

```
⚠️ ATENÇÃO: Execução está desativada por padrão (NEXT_PUBLIC_ENABLE_EXECUTION=false)
Para ativar:
1. Edite frontend/.env.local
2. Mude para: NEXT_PUBLIC_ENABLE_EXECUTION=true
3. Restart frontend (npm run dev)
```

### 3. Acompanhar histórico

- Abra aba "Histórico"
- Veja todos os trades fechados
- Win rate calculado automaticamente

### 4. Validar estratégia

- Abra "Métricas"
- Verifique se Sharpe > 1.0
- Verifique se Win Rate > 50%
- Se OK → pronto para trading real

---

## Configuração Avançada

### Alterar intervalo de atualização

Em `frontend/src/components/Dashboard.jsx`:

```javascript
const interval = setInterval(fetchData, 60000); // 60 segundos
// Mude para:
const interval = setInterval(fetchData, 30000); // 30 segundos (mais rápido)
```

### Adicionar mais pares

Em `frontend/src/components/Dashboard.jsx`:

```javascript
const pairs = [
  'EUR_USD', 'GBP_USD', 'USD_JPY', 'USD_CHF', 'AUD_USD',
  'USD_CAD', 'NZD_USD', 'EUR_GBP', 'EUR_JPY', 'EUR_CHF',
  // Adicionar aqui:
  'GBP_JPY',
  'AUD_JPY',
  // etc
];
```

### Customizar cores

Edite `frontend/src/styles/globals.css` ou `tailwind.config.js`

---

## Troubleshooting

### Erro: "API connection failed"

**Causa**: Backend não está rodando

**Solução**:
1. Verifique se backend está em `http://localhost:8000`
2. No Terminal 1, rode: `python -m uvicorn src.api.main:app --reload --port 8000`

### Erro: "Cannot GET /"

**Causa**: Frontend não iniciou corretamente

**Solução**:
1. Verifique se em `http://localhost:3000`
2. No Terminal 2, rode: `npm run dev`

### Gráficos não aparecem

**Causa**: Lightweight-charts não instalado

**Solução**:
```bash
cd frontend
npm install lightweight-charts
npm run dev
```

### Backend lento/travado

**Causa**: Muitos cálculos simultâneos

**Solução**:
1. Reduza número de pares testados
2. Aumente `num_days` no backtest (menos frequência)
3. Use `NEXT_PUBLIC_UPDATE_INTERVAL=120000` (2 minutos)

---

## Deploy

### Local (Desenvolvimento)

```bash
# Terminal 1: Backend
cd backend && python -m uvicorn src.api.main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend && npm run dev

# Acesse: http://localhost:3000
```

### Produção (Docker)

```bash
# Construir imagens
docker-compose build

# Rodar containers
docker-compose up

# Acesse: http://localhost
```

### Arquivo docker-compose.yml

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      OANDA_TOKEN: ${OANDA_TOKEN}
      OANDA_ACCOUNT: ${OANDA_ACCOUNT}
    volumes:
      - ./data:/app/data

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      NEXT_PUBLIC_API_URL: http://backend:8000
    depends_on:
      - backend

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: forex
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
```

---

## Checklist de Setup

- [ ] Python 3.9+ instalado
- [ ] Node.js 16+ instalado
- [ ] Backend virtual environment criado
- [ ] Backend dependências instaladas (`pip install -r requirements.txt`)
- [ ] Frontend dependências instaladas (`npm install`)
- [ ] Backend rodando em `http://localhost:8000`
- [ ] Frontend rodando em `http://localhost:3000`
- [ ] Dashboard abrindo no navegador
- [ ] Dados carregando corretamente
- [ ] Sinais aparecendo na aba Oportunidades
- [ ] Gráficos D1/W1 visualizáveis

---

## Próximas Steps

1. ✅ **Backend + Frontend rodando**
2. ⏳ Rodar backtesting das estratégias (`python run_all_strategies_backtest.py`)
3. ⏳ Paper trading (2-3 semanas sem risco)
4. ⏳ Conectar OANDA real
5. ⏳ Go live com pequeno capital

---

## Performance

| Métrica | Esperado | Seu Sistema |
|---------|----------|------------|
| Frontend load | < 2s | ? |
| API response | < 500ms | ? |
| Chart render | < 1s | ? |
| Backtest (5 anos) | < 30s | ? |

Teste com: `F12` → Network tab

---

## Suporte

Se encontrar problemas:
1. Verifique Console (F12) para erros JavaScript
2. Verifique Terminal 1 para erros Python
3. Verifique se ambos servidores estão rodando
4. Restart ambos servidores se tudo falhar
