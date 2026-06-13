# Calculadora de ROI — CaLopes Soluções Inteligentes

Landing page completa com calculadora interativa de ROI para prospecção de clientes.

## 📋 O que contém

- **Calculadora ROI em tempo real**: calcula perdas mensais/anuais conforme o cliente insere ticket médio e número de clientes
- **Hero section**: headline impactante com copy direto
- **3 Cards de solução**: Site, IA no WhatsApp, Consultoria
- **Formulário de agendamento**: coleta nome, email, WhatsApp, ramo do negócio
- **Dark mode completo**: paleta azul/preto/branco
- **100% responsivo**: mobile, tablet, desktop
- **Arquivo único**: HTML com CSS e JavaScript inline — sem dependências externas (apenas Google Fonts)

## 🎨 Paleta de cores

- Azul destaque: `#00A3E0`
- Fundo principal: `#1A1A1A`
- Fundo secundário: `#121212`
- Texto: `#FFFFFF` (branco)
- Texto secundário: `#A0A0A0` (cinza médio)

## 🚀 Como usar

1. **Abrir no navegador**: Clique duplo em `index.html` ou abra pelo navegador
2. **Testar a calculadora**: Digite valores em "Ticket médio" e "Clientes por mês" → resultado aparece em tempo real
3. **Testar responsividade**: Redimensione a janela ou abra DevTools (F12) → modo mobile
4. **Validar formulário**: Deixe campos em branco ou email inválido → mostra erro

## 🔧 Funcionalidades JS

- **Cálculo ROI**: `(Ticket × Clientes × 0.30)` = perda mensal em tempo real
- **Formatação BRL**: valores exibidos como `R$ X.XXX,XX`
- **Validação de email**: regex básico
- **Validação de WhatsApp**: 11 dígitos brasileiros com auto-formatação
- **Auto-format WhatsApp**: digita `11999999999` → `11 99999-9999`

## 📝 TODO

- [ ] Integrar com email (Mailgun/SendGrid ou API própria)
- [ ] Integrar com WhatsApp Business API para notificar Matheus
- [ ] Analytics (GA4 ou similar)
- [ ] A/B testing de headlines
- [ ] Redirect para agendamento externo (Calendly, Typeform)

## 📱 Responsividade

- **Desktop** (1200px+): Layout cheio com cards lado-a-lado
- **Tablet** (768px-1199px): Cards em grid adaptável
- **Mobile** (até 767px): Stack vertical, inputs com 44px de altura (toque confortável)

## 🔐 Segurança

- Validação client-side apenas (para UX)
- **TODO**: Validação server-side antes de processar formulário
- Sem armazenamento de dados localmente

## 🎯 Próximos passos

1. Copiar link `calculadora-roi/index.html` para compartilhar
2. Colocar em um servidor/hosting (Vercel, Netlify, seu próprio host)
3. Integrar com backend para processar agendamentos
4. Testar em devices reais (celular, tablet)
