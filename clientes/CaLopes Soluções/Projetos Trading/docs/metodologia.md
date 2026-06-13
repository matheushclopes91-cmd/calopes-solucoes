# 📚 Metodologia — Larry Williams Setups 9.1, 9.2, 9.3

Explicação técnica completa dos setups de trading baseados em Price Action.

---

## 🎯 Conceito Central

A metodologia de Larry Williams utiliza **correções em tendências estabelecidas** como oportunidades de entrada. Quanto **mais profunda a correção, maior a segurança** da operação.

```
Tendência de ALTA          Tendência de BAIXA
      ↑                          ↓
  Retração                   Retração
  (Compra)                   (Venda)
      ↑                          ↓
```

---

## 📊 Definição de Tendência

### Tendência de ALTA ✓

Todas estas condições devem ser **VERDADEIRAS**:

1. **EMA 9 > EMA 21** (curto prazo acima intermediário)
2. **EMA 21 > EMA 50** (intermediário acima longo prazo)
3. **EMA 9 > EMA 9[1]** (inclinação positiva em 9)
4. **EMA 21 > EMA 21[1]** (inclinação positiva em 21)
5. **EMA 50 > EMA 50[1]** (inclinação positiva em 50)

**Visualização:**
```
        EMA 9 (inclinada para cima)
       /
      /  EMA 21 (inclinada para cima)
     /  /
    /  /  EMA 50 (inclinada para cima)
```

---

### Tendência de BAIXA ✓

Todas estas condições devem ser **VERDADEIRAS**:

1. **EMA 9 < EMA 21** (curto prazo abaixo intermediário)
2. **EMA 21 < EMA 50** (intermediário abaixo longo prazo)
3. **EMA 9 < EMA 9[1]** (inclinação negativa em 9)
4. **EMA 21 < EMA 21[1]** (inclinação negativa em 21)
5. **EMA 50 < EMA 50[1]** (inclinação negativa em 50)

**Visualização:**
```
EMA 9 (inclinada para baixo) \
                             \
                              EMA 21 (inclinada para baixo) \
                                                           \
                                                            EMA 50 (inclinada para baixo)
```

---

## 🔴 SETUP 9.1 — Toque na EMA 9

**Tipo:** Entrada em retração **superficial** na tendência

### Compra (Setup 9.1 Long)

**Quando operar:**
- ✓ Tendência de alta **válida**
- ✓ Preço **cai** em direção à EMA 9
- ✓ **Mínima do candle toca ou cruza** a EMA 9
- ✓ Candle **fecha acima** da EMA 9
- ✓ **Confirmação:** Preço não rompeu a EMA 21 (retração não foi profunda demais)

**Sinal de Entrada:**
```
├─ Candle anterior: Preço < EMA 9
├─ Candle atual: Preço toca EMA 9 (low <= EMA9)
└─ Candle atual: Fecha > EMA 9 (close > EMA9)

ENTRY = Fechamento do candle que toca a EMA 9
```

**Stop Loss:**
```
SL = Mínima do candle de sinal - 10 pips (ou ponto decimal)
```

**Take Profit:**
```
TP = Última máxima relevante relevante anterior
     (ou TP = Entry + (Entry - SL) × 2.0)
```

**Risco/Recompensa:** 1:2 mínimo recomendado

### Venda (Setup 9.1 Short)

**Quando operar:**
- ✓ Tendência de baixa **válida**
- ✓ Preço **sobe** em direção à EMA 9
- ✓ **Máxima do candle toca ou cruza** a EMA 9
- ✓ Candle **fecha abaixo** da EMA 9
- ✓ **Confirmação:** Preço não rompeu a EMA 21

**Sinal de Entrada:**
```
├─ Candle anterior: Preço > EMA 9
├─ Candle atual: Preço toca EMA 9 (high >= EMA9)
└─ Candle atual: Fecha < EMA 9 (close < EMA9)

ENTRY = Fechamento do candle
```

**Stop Loss:**
```
SL = Máxima do candle de sinal + 10 pips
```

**Take Profit:**
```
TP = Último fundo relevante anterior
     (ou TP = Entry - (SL - Entry) × 2.0)
```

---

## 🟡 SETUP 9.2 — Toque na EMA 21

**Tipo:** Entrada em retração **intermediária** (mais segura)

### Compra (Setup 9.2 Long)

**Quando operar:**
- ✓ Tendência de alta **válida**
- ✓ Correção **alcança a EMA 21**
- ✓ **Mínima toca ou cruza** a EMA 21
- ✓ Candle **fecha acima** da EMA 21
- ✓ **Validação crítica:** EMA 9 **ainda está acima** da EMA 21
  - (Se EMA 9 cruzou abaixo de EMA 21 = sinal de enfraquecimento)

**Condição especial:**
```
Tendência está "respirando" mas ainda intacta:
- EMA 9 > EMA 21 ✓
- EMA 21 > EMA 50 ✓
```

**Sinal de Entrada:**
```
├─ Candle anterior: Preço < EMA 21
├─ Candle atual: Preço toca EMA 21 (low <= EMA21)
└─ Candle atual: Fecha > EMA 21 (close > EMA21)

E EMA 9 AINDA está acima de EMA 21

ENTRY = Fechamento do candle
```

**Stop Loss:**
```
SL = Mínima do candle de sinal - 10 pips
```

**Take Profit:**
```
TP = Última máxima relevante anterior
     (ou TP = Entry + (Entry - SL) × 2.0 a 3.0)
```

**Por que é mais seguro?**
- Retração é mais profunda = movimento reverso será mais forte
- EMA 9 se mantém acima = estrutura de alta intacta
- Oferece melhor relação risco/recompensa

### Venda (Setup 9.2 Short)

**Quando operar:**
- ✓ Tendência de baixa **válida**
- ✓ Correção **alcança a EMA 21**
- ✓ **Máxima toca ou cruza** a EMA 21
- ✓ Candle **fecha abaixo** da EMA 21
- ✓ **Validação crítica:** EMA 9 **ainda está abaixo** da EMA 21

**Sinal de Entrada:**
```
├─ Candle anterior: Preço > EMA 21
├─ Candle atual: Preço toca EMA 21 (high >= EMA21)
└─ Candle atual: Fecha < EMA 21 (close < EMA21)

E EMA 9 AINDA está abaixo de EMA 21

ENTRY = Fechamento do candle
```

**Stop Loss:**
```
SL = Máxima do candle de sinal + 10 pips
```

**Take Profit:**
```
TP = Último fundo relevante anterior
```

---

## 🟢 SETUP 9.3 — Toque na EMA 50

**Tipo:** Entrada em retração **profunda** (máxima segurança, menor frequência)

### Compra (Setup 9.3 Long)

**Quando operar:**
- ✓ Tendência de alta **válida**
- ✓ Correção **alcança a EMA 50** (retração profunda)
- ✓ **Mínima toca ou cruza** a EMA 50
- ✓ Candle **fecha acima** da EMA 50
- ✓ **Dupla validação:**
  - EMA 9 > EMA 21 ✓
  - EMA 21 > EMA 50 ✓
  - (Estrutura TOTALMENTE intacta)

**Sinal de Entrada:**
```
├─ Candle anterior: Preço < EMA 50
├─ Candle atual: Preço toca EMA 50 (low <= EMA50)
└─ Candle atual: Fecha > EMA 50 (close > EMA50)

E (EMA9 > EMA21 > EMA50)

ENTRY = Fechamento do candle
```

**Stop Loss:**
```
SL = Mínima do candle de sinal
```

**Take Profit:**
```
TP = Última máxima relevante anterior
     (ou TP = Entry + (Entry - SL) × 2.5 a 3.0)
```

**Por que é a operação mais segura?**
- Retração muito profunda antes de reverter = força máxima
- Todas as EMAs mantêm estrutura = sem comprometimento
- Maior certeza que a tendência vai continuar

### Venda (Setup 9.3 Short)

**Quando operar:**
- ✓ Tendência de baixa **válida**
- ✓ Correção **alcança a EMA 50**
- ✓ **Máxima toca ou cruza** a EMA 50
- ✓ Candle **fecha abaixo** da EMA 50
- ✓ **Dupla validação:**
  - EMA 9 < EMA 21 ✓
  - EMA 21 < EMA 50 ✓

---

## ⭐ PONTO DE CONTROLE (PC)

**Sinal de confirmação** que valida o setup após a retração.

### PC Comprador (Long)

**O que é:**
Após uma retração em tendência de alta, o candle que faz uma **nova máxima**, rompendo a máxima do candle anterior.

**Visualização:**
```
Máxima anterior: 1.1050
PC Comprador:    1.1052 (novo high)
                 └─ Este é o PC
```

**Utilidade:**
- ✓ Confirma que a correção foi absorvida
- ✓ Sinal de força bullish
- ✓ Ótimo para **adicionar posição** (piramiding)
- ✓ Pode servir como **confirmação para entrada tardia**

### PC Vendedor (Short)

**O que é:**
Após uma retração em tendência de baixa, o candle que faz uma **nova mínima**, rompendo a mínima do candle anterior.

**Visualização:**
```
Mínima anterior: 1.1050
PC Vendedor:     1.1048 (novo low)
                 └─ Este é o PC
```

---

## 📈 Tabela de Comparação dos Setups

| Aspecto | 9.1 | 9.2 | 9.3 |
|---------|-----|-----|-----|
| **Profundidade** | Superficial (EMA 9) | Intermediária (EMA 21) | Profunda (EMA 50) |
| **Frequência** | Alta | Média | Baixa |
| **Segurança** | Média | Alta | Muito Alta |
| **RR típico** | 1:1.5 | 1:2.0 | 1:2.5+ |
| **Timeframe** | 1min, 5min, 15min | 15min, 1H, 4H | 1H, 4H, D |
| **Melhor para** | Scalping | Day trade | Swing trade |

---

## 🎓 Exemplo Prático (EURUSD 1H)

```
14:00 — Tendência de ALTA confirmada
        EMA 9: 1.1050
        EMA 21: 1.1045
        EMA 50: 1.1040

15:00 — Preço começa a retrair
        Close: 1.1048

16:00 — Toque na EMA 9
        Low: 1.1049
        Close: 1.1051 > EMA9 ✓
        
        ➜ SETUP 9.1 GERADO
        Entry: 1.1051
        SL: 1.1049 - 10 pips = 1.1039
        TP: Last High = 1.1065
        RR = 1:(1.1065-1.1051)/(1.1051-1.1039) = 1:1.17

17:00 — Nova máxima
        High: 1.1067 > High anterior ✓
        
        ➜ PONTO DE CONTROLE DETECTADO
        Confirmação: Pode manter posição ou adicionar
```

---

## 🚫 Armadilhas Comuns

### ❌ Retração que não reverte
```
Você vê Setup 9.2
Mas a retração CONTINUA abaixo da EMA 21
├─ EMA 9 cruzou abaixo de EMA 21 ❌
├─ Estrutura foi comprometida
└─ IGNORE o sinal
```

### ❌ Operação contra a tendência
```
Você vê sinal de COMPRA 9.3
Mas EMA 9 está abaixo de EMA 21 ❌
├─ Não há tendência de alta
├─ É falso sinal
└─ IGNORE completamente
```

### ❌ PC sem setup anterior
```
Você vê nova máxima (PC)
Mas NÃO houve sinal 9.1, 9.2 ou 9.3 ❌
├─ PC sozinho não é entrada
├─ Sempre precisa de setup + PC
└─ Use apenas como confirmação
```

---

## 📖 Referências e Adaptações

Este sistema é baseado em:
- **Larry Williams** — Conceito original de retrações em tendências
- **PALEX Trading** (Brasil) — Adaptação 9.1, 9.2, 9.3
- **Stormer Trading** — Validações e filtros
- **L&S Trading** — Otimizações para Forex

**Variações conhecidas:**
- Alguns traders usam SMA 20 em vez de EMA 21
- Alguns usam ADX > 30 para filtro mais rígido
- Alguns adaptam para multi-timeframe (confirmar em TF maior)

---

## 🎯 Próximas Melhorias

- [ ] Integrar com osciladores (RSI, Estocástico) para confirmação
- [ ] Versão com Harmonic Patterns
- [ ] Integração com Fibonacci Retracement
- [ ] Backtest automático por setup (qual tem melhor taxa?)

---

**Desenvolvido por:** CaLopes Soluções Inteligentes  
**Última atualização:** Junho 2026
