# 🚀 Guia de Setup — Larry Williams Trading System

Como instalar e configurar o sistema no TradingView.

---

## 📍 Passo 1: Acessar TradingView

1. Acesse **https://www.tradingview.com/chart/**
2. Faça login em sua conta
3. Selecione um **ativo e timeframe** para testar
   - Recomendado: EURUSD (1H) ou BTCUSD (1H) para começar

---

## 📋 Passo 2: Copiar o Código

### Opção A: Indicador (Recomendado para Operadores Manuais)

1. Abra o **Pine Script Editor** (Alt + P no gráfico)
2. Clique em **"New script" → Indicator**
3. Copie o código de `pine-script/indicador-larry-williams.pine`
4. Cole no editor
5. Clique em **"Save"** (Ctrl + S)
6. Nomeie como: `Larry Williams 9.1 9.2 9.3`
7. Clique em **"Add to chart"**

### Opção B: Strategy (Para Backtest Automático)

1. Abra o **Pine Script Editor** (Alt + P no gráfico)
2. Clique em **"New script" → Strategy**
3. Copie o código de `pine-script/strategy-larry-williams.pine`
4. Cole no editor
5. Clique em **"Save"** (Ctrl + S)
6. Nomeie como: `Larry Williams Strategy`
7. Clique em **"Add to chart"**

---

## ⚙️ Passo 3: Configurar Parâmetros

Após adicionar ao gráfico, clique no **ícone de engrenagem** do indicador/strategy.

### Configuração Básica (Recomendada para Iniciantes)

| Parâmetro | Valor | Razão |
|-----------|-------|-------|
| Mostrar EMA 9 | ✓ ON | Identifica correções |
| Mostrar EMA 21 | ✓ ON | Confirma tendência |
| Mostrar EMA 50 | ✓ ON | Define estrutura |
| Setup 9.1 | ✓ ON | Sinais de entrada |
| Setup 9.2 | ✓ ON | Sinais de entrada |
| Setup 9.3 | ✓ ON | Sinais de entrada |
| Ponto de Controle | ✓ ON | Confirma força |
| **Usar ADX** | ✗ OFF | Evita ruído inicial |
| **Volume > Média** | ✗ OFF | Evita ruído inicial |
| **TP Multiplicador** | 2.0 | RR 1:2 (padrão) |

### Configuração Intermediária (Filtragem)

Se estiver gerando muitos sinais falsos, ative os filtros:

```
✓ Usar ADX
  ADX Mínimo: 25 (tendência forte)

✓ Volume > Média
  (Confirma força do movimento)

TP Multiplicador: 2.5 ou 3.0 (RR melhor)
```

---

## 📊 Passo 4: Testar o Indicador

1. **Abra um gráfico** de 1H (EURUSD, BTCUSD ou ação)
2. **Observe os sinais:**
   - 🟢 **SETUP 9.1** = Verde (setas para cima/baixo)
   - 🟢 **SETUP 9.2** = Verde mais acima
   - 🟢 **SETUP 9.3** = Verde bem acima
   - 🟡 **PC** = Amarelo (confirmação)

3. **Verifique as correlações:**
   - EMA 9 > EMA 21 > EMA 50 = Tendência de ALTA ✓
   - EMA 9 < EMA 21 < EMA 50 = Tendência de BAIXA ✓

---

## 🔙 Passo 5: Para Strategy (Backtest)

Se escolheu a **Strategy**, acesse a aba **Strategy Tester** (lado direito):

1. Vá em **"Settings"** → Configure **data de início/fim**
2. Clique em **"Start Backtest"**
3. Aguarde o resultado (pode levar segundos ou minutos)

**Resultado mostrará:**
- ✓ Total de trades
- ✓ Win rate (%)
- ✓ Profit factor
- ✓ Drawdown máximo
- ✓ Lucro líquido

---

## 📱 Passo 6: Configurar Alertas (Opcional)

Para receber **notificações em tempo real**:

1. Clique com **botão direito** no indicador → **Alerts**
2. Crie um alerta por tipo de setup:
   - "COMPRA 9.1"
   - "VENDA 9.1"
   - "COMPRA 9.2"
   - "VENDA 9.2"
   - "COMPRA 9.3"
   - "VENDA 9.3"

3. Configure **notificação via:**
   - Email
   - SMS
   - Webhook (integração com bot)

---

## 🎯 Dicas Importantes

### ✅ O Que Funciona Bem

- **Forex (EURUSD, GBPUSD)** — Melhor performance
- **Timeframe 1H** — Melhor relação risco/recompensa
- **Tendências estabelecidas** — Use EMA como confirmação
- **Volume confirmando** — Força do movimento

### ❌ O Que Evitar

- Operar em **consolidações** (EMAs horizontais)
- Ignorar o **Ponto de Controle** — É validação importante
- **Scalping em 1min/5min** — Muito ruído
- Aumentar alavancagem só porque "deu certo um dia"

---

## 🔧 Troubleshooting

### **Problema: Nenhum sinal aparece**

✓ Verifique se as EMAs estão visíveis
✓ Mude para gráfico 1H em Forex
✓ Confirme que está em uma **tendência estabelecida**

### **Problema: Muitos sinais falsos**

✓ Ative o **filtro ADX** (ADX > 25)
✓ Ative o **filtro de volume**
✓ Aumente **distância mínima entre sinais** para 10 barras

### **Problema: Não consegue copiar o código**

✓ Tente copiar novamente
✓ Verifique se não há **caracteres especiais cortados**
✓ Cole em um **editor de texto antes** (notepad) e depois no Pine Script

---

## 📈 Próximos Passos

1. **Backtest em 3 meses de dados** — Veja performance
2. **Forward test 2 semanas** — Teste com dinheiro pequeno
3. **Optimize parâmetros** — Se necessário
4. **Integre com bot** — Se quiser automação

---

## 💬 Dúvidas?

Matheus Lopes: matheushclopes91@gmail.com

---

**Atualizado:** Junho 2026
