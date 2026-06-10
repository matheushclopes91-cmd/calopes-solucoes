# Forex Trading Dashboard

Real-time dashboard para análise técnica de forex com visualização D1/W1, oportunidades de trading e histórico de operações.

## Stack

- **Framework**: Next.js 14
- **UI**: React 18 + Tailwind CSS
- **Charts**: lightweight-charts (gráficos financeiros)
- **State**: React Hooks
- **API**: Axios (fetch de dados do backend Python)

## Estrutura

```
frontend/
├── src/
│   ├── components/
│   │   ├── Dashboard.jsx           # Layout principal
│   │   ├── ChartD1W1.jsx           # Gráficos candlestick
│   │   ├── OpportunitiesList.jsx   # Sinais/oportunidades
│   │   ├── OperationHistory.jsx    # Histórico de operações
│   │   └── StrategyMetrics.jsx     # Métricas de backtesting
│   ├── pages/
│   │   ├── index.jsx               # Home page
│   │   ├── _app.jsx                # App wrapper
│   │   └── _document.jsx           # HTML structure
│   └── styles/
│       └── globals.css             # Estilos globais
├── package.json
├── next.config.js
├── tailwind.config.js
└── postcss.config.js
```

## Componentes

### Dashboard
- Seletor de pares (EUR_USD, GBP_USD, USD_JPY, etc)
- Atualização automática a cada minuto
- Integração com API backend

### ChartD1W1
- Gráficos candlestick com lightweight-charts
- EMAs 50 e 200
- Suporte para timeframes D1 e W1
- Realtime price updates

### OpportunitiesList
- Exibe todos os sinais de trading
- Confiança da estratégia
- Sinais de confluência (⭐)
- Botões Execute/Details

### OperationHistory
- Histórico de operações executadas
- Status: OPEN, CLOSED_WIN, CLOSED_LOSS
- P&L em %
- Estatísticas de win rate

### StrategyMetrics
- Sharpe Ratio
- Win Rate
- Profit Factor
- Max Drawdown
- Status da estratégia (Ready/Needs Optimization)

## Setup

### 1. Instalar dependências

```bash
npm install
# ou
yarn install
```

### 2. Rodar em desenvolvimento

```bash
npm run dev
# ou
yarn dev
```

Acesse em: http://localhost:3000

### 3. Build para produção

```bash
npm run build
npm start
```

## Conectar com Backend

O dashboard faz requests para a API FastAPI em `http://localhost:8000`:

```javascript
// Endpoints esperados
GET /api/opportunities?pair=EUR_USD   // Sinais
GET /api/operations?pair=EUR_USD      // Histórico
GET /api/metrics?pair=EUR_USD         // Métricas
```

**Backend deve estar rodando antes de iniciar o dashboard!**

## Customização

### Alterar cores
Edite `tailwind.config.js` ou `src/styles/globals.css`

### Adicionar indicadores ao gráfico
Em `ChartD1W1.jsx`:
```javascript
const rsiseries = chart.addLineSeries({
  color: '#6366f1',
  lineWidth: 1,
  title: 'RSI',
});

rsiSeries.setData(rsiData);
```

### Adicionar novos pares
Em `Dashboard.jsx`:
```javascript
const pairs = [
  'EUR_USD', 'GBP_USD', 'USD_JPY', 'USD_CHF', 'AUD_USD',
  'USD_CAD', 'NZD_USD', 'EUR_GBP', 'EUR_JPY', 'EUR_CHF',
  // Adicionar aqui:
  'GBP_JPY', 'AUD_JPY', // etc
];
```

## Features

- ✅ Seleção de pares
- ✅ Gráficos D1/W1
- ✅ Oportunidades com confiança
- ✅ Sinais de confluência
- ✅ Histórico com P&L
- ✅ Métricas de backtesting
- ✅ Atualização automática
- ✅ Design responsivo
- ⏳ Executar trades direto do dashboard
- ⏳ Alertas em tempo real
- ⏳ Exportar histórico (CSV/PDF)

## Troubleshooting

### "Cannot GET /"
- Verifique se o servidor está rodando em `http://localhost:3000`
- Execute `npm run dev` novamente

### "API connection failed"
- Verifique se backend está rodando em `http://localhost:8000`
- Verifique CORS em FastAPI backend

### Gráficos não aparecem
- Cheque console (F12) para erros
- Verifique que lightweight-charts foi instalado corretamente

## Deploy

### Vercel (recomendado)

```bash
npm install -g vercel
vercel
```

### Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "start"]
EXPOSE 3000
```

```bash
docker build -t forex-dashboard .
docker run -p 3000:3000 forex-dashboard
```

## Performance

- Lazy loading de componentes
- Image optimization
- CSS minification
- Bundle size: ~150KB (gzipped)

## Próximas features

- [ ] Histórico de backtests
- [ ] Exportar trades (CSV)
- [ ] Alertas via Telegram
- [ ] Dark/Light mode toggle
- [ ] Mobile app version
