# 🎯 Modelos de Sites Profissionais — CaLopes

Biblioteca de templates React prontos para uso em diferentes segmentos de negócio. Cada modelo é uma base pronta para customizar com dados do cliente.

---

## 📁 Estrutura por Categoria

### 🔵 **OTICAS** _(Concluído)_
Site profissional completo para óticas e consultórios oftalmológicos.

**Inclui:**
- Home com hero + destaques
- Sobre (história, missão, valores, team)
- Serviços (teste de visão, lentes, consulta de estilo, manutenção)
- Produtos (catálogo com filtros)
- Agendamento (formulário)
- Blog (dicas de saúde visual)

**Como usar:**
```bash
cd OTICAS
npm install
npm run dev
```

Ver [SETUP.md](./OTICAS/SETUP.md) para customizar em 5 minutos.

---

### 📋 **Próximas categorias** _(Planejadas)_

- **CONSULTORIO** — Consultórios e clínicas (médico, dentista, psicólogo)
- **ECOMMERCE** — Lojas online e e-commerce
- **SERVICOS** — Serviços gerais (encanador, eletricista, design)
- **RESTAURANTE** — Restaurantes e bares
- **BELEZA** — Salões, spas, cabeleireiros
- **IMOBILIARIA** — Imobiliárias e corretoras
- **AGENCIA** — Agências (turismo, publicidade)

---

## 🚀 Como Usar Um Modelo

### 1️⃣ Escolha a categoria do cliente
Vá para a pasta correspondente (ex: `OTICAS/`)

### 2️⃣ Configure o ambiente
```bash
cd [CATEGORIA]
npm install
npm run dev
```

### 3️⃣ Customize conforme a necessidade
- Abra `SETUP.md` para guia rápido
- Consulte `README.md` para documentação completa

### 4️⃣ Após pronto, faça build
```bash
npm run build
# Enviar a pasta 'dist' para hosting (Vercel, Netlify, GitHub Pages)
```

---

## 🎨 Padrão de Design

Todos os modelos seguem:
- **Cores CaLopes**: Azul #00A3E0, secundário #0A1A3D (customizáveis)
- **Typography**: Fonte do sistema (rápido, profissional)
- **Responsivo**: Mobile-first (testado em 320px até 1920px)
- **Acessibilidade**: WCAG AA (cores, contraste, navegação)

---

## 📦 Stack Padrão

Todos os modelos usam:
- **React 18** — UI
- **React Router DOM** — Navegação
- **Tailwind CSS** — Estilização
- **React Icons** — Ícones
- **Vite** — Build tool

_Se o cliente pedir customização (API integration, CMS, etc.), será criado um projeto específico em `clientes/[nome-cliente]/`._

---

## 💡 Dicas para Propostas

Ao apresentar para um cliente novo:

1. **Mostre o site ao vivo**: Rodar `npm run dev` localmente ou fazer deploy em Vercel
2. **Customizando ao vivo**: Mudar cores, textos, imagens em tempo real (melhor impacto)
3. **Explique a facilidade**: "Tudo é feito em React, fácil de manter e escalar"
4. **Tempo de entrega**: "Template leva 2-3 dias para estar 100% pronto com seu conteúdo"

---

## 📝 Checklist Antes de Entregar

- [ ] Nome/logo do cliente
- [ ] Contato (telefone, email, endereço)
- [ ] Cores da marca
- [ ] Textos de todas as páginas
- [ ] Imagens reais (não usar emojis)
- [ ] Serviços/produtos listados
- [ ] Agendamento/contato integrado (WhatsApp, Calendly, etc)
- [ ] Redes sociais linkadas
- [ ] Testado em mobile/tablet/desktop
- [ ] Deploy realizado (Vercel/Netlify)

---

## 🔧 Criar Novo Modelo

Se precisar de uma categoria não listada:

1. Copie uma categoria existente como base
2. Customize as páginas conforme o segmento
3. Teste completamente
4. Crie um `README.md` explicando as particularidades
5. Comite em `clientes/modelos-sites/[NOVA_CATEGORIA]/`

---

**Desenvolvido com ❤️ pela CaLopes Soluções Inteligentes**
