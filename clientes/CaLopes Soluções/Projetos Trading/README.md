# 📊 Larry Williams Trading System — Pine Script v6

Sistema profissional de trading para TradingView com identificação automática dos setups Larry Williams 9.1, 9.2 e 9.3, com foco em Price Action.

---

## 📋 Visão Geral

Este projeto contém um **indicador profissional** e uma **strategy de backtest** que identificam automaticamente os setups de trading de Larry Williams, utilizando média móvel exponencial (EMA) como base de análise.

**Ativos suportados:**
- ✅ Forex (pares de moedas)
- ✅ Índices (SP500, DAX, etc)
- ✅ Criptomoedas (BTC, ETH, etc)
- ✅ Ações

**Timeframes recomendados:**
- 1H (melhor performance)
- 4H
- 15min (scalping)
- D (swing)

---

## 🎯 Setups Implementados

### **Setup 9.1** — Toque na EMA 9
Entrada em correção na média de curto prazo em tendência estabelecida.
- **Risco:** Baixo
- **Frequência:** Alta
- **Melhor para:** Scalping e day trading

### **Setup 9.2** — Toque na EMA 21
Entrada em correção na média intermediária, confirmando força.
- **Risco:** Médio
- **Frequência:** Média
- **Melhor para:** Swing trading

### **Setup 9.3** — Toque na EMA 50
Entrada em correção profunda na média de longo prazo, máxima segurança.
- **Risco:** Médio-Alto
- **Frequência:** Baixa
- **Melhor para:** Posições mais longas

### **PC (Ponto de Controle)**
Rompimento que valida o setup após a correção.
- **Sinal de confirmação** para entrada
- **Aumenta acurácia** do sistema

---

## 📁 Estrutura do Projeto

```
Projetos Trading/
├── README.md                           # Este arquivo
├── pine-script/
│   ├── indicador-larry-williams.pine  # Indicador visual (recomendado)
│   └── strategy-larry-williams.pine   # Strategy para backtest
├── docs/
│   ├── setup-guia.md                  # Como usar no TradingView
│   ├── metodologia.md                 # Explicação detalhada dos setups
│   └── backtest-resultados.md         # Histórico de testes
└── config/
    └── parametros.json                # Configurações recomendadas
```

---

## 🚀 Como Usar

### 1. **Abrir no TradingView**

```
1. Acesse: https://www.tradingview.com/chart/
2. Vá em: Pine Script Editor (Alt + P no gráfico)
3. Novo Script → Cole o código do indicador ou strategy
4. Customize os parâmetros
5. Salve e aplique no gráfico
```

### 2. **Copiar Indicador** (Recomendado para operacional)
- Arquivo: `pine-script/indicador-larry-williams.pine`
- Não precisa de backtest, apenas visualização
- Ideal para traders que operam manualmente

### 3. **Copiar Strategy** (Para automação)
- Arquivo: `pine-script/strategy-larry-williams.pine`
- Executa backtest automaticamente
- Permite automação com alertas

---

## ⚙️ Parâmetros Padrão

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| **EMA 9** | 9 | Média móvel de curto prazo |
| **EMA 21** | 21 | Média móvel intermediária |
| **EMA 50** | 50 | Média móvel de longo prazo |
| **TP Multiplicador** | 2.0 | Razão risco/recompensa |
| **Volume Filter** | OFF | Filtro de volume |
| **ADX Min** | 20 | Mínimo de ADX para sinal |

---

## 📊 Filtros Disponíveis

✅ **Volume acima da média** — Confirma força
✅ **ADX (Índice de direção)** — Valida tendência
✅ **Horário operacional** — Define janelas de trading
✅ **Distância mínima entre sinais** — Evita ruído
✅ **Multi-timeframe** — Confirma tendência superior

---

## 📈 Resultados de Backtest

Ver arquivo: `docs/backtest-resultados.md`

**Resumo último teste** (atualizado: 2026-06-13):
- Taxa de Acerto: Pendente
- Profit Factor: Pendente
- Drawdown Máximo: Pendente

---

## 🔧 Próximas Melhorias

- [ ] Integração com alertas de email/SMS
- [ ] Dashboard de estatísticas
- [ ] Versão com Machine Learning
- [ ] Otimizador automático de parâmetros
- [ ] Suporte a múltiplas estratégias (Gartley, Harmonic)

---

## 📚 Referências

- **Larry Williams** — Original methodology
- **PALEX Trading** — Adaptações brasileiras (9.1, 9.2, 9.3)
- **Price Action Trading** — Technical foundation

---

## 💬 Suporte

Dúvidas ou sugestões sobre o sistema?
- Matheus Lopes: matheushclopes91@gmail.com
- CaLopes Soluções Inteligentes

---

**Desenvolvido com ❤️ para traders brasileiros** | v1.0 — Junho 2026
