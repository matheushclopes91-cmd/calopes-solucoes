# 🎯 Template Profissional de Site para Óticas

Template React moderno e profissional, pronto para ser customizado com dados de qualquer ótica.

## ✨ Características

- ✅ Multi-página com navegação completa
- ✅ Design responsivo (Mobile, Tablet, Desktop)
- ✅ Páginas incluídas:
  - **Home**: Hero + destaques + CTA
  - **Sobre**: História, missão, visão, values e time
  - **Serviços**: Descrição detalhada de todos os serviços
  - **Produtos**: Catálogo com filtros
  - **Agendamento**: Formulário profissional
  - **Blog**: Sistema de posts
- ✅ Componentes reutilizáveis
- ✅ Tailwind CSS para estilização rápida
- ✅ Ícones via React Icons

## 🚀 Como Usar

### 1. **Instalação**
```bash
cd template-otica
npm install
```

### 2. **Desenvolvimento (com live reload)**
```bash
npm run dev
```
A aplicação estará disponível em `http://localhost:5173`

### 3. **Build para produção**
```bash
npm run build
```

## 🎨 Customização

### Cores Principais
Edite `tailwind.config.js`:
```js
colors: {
  primary: '#00A3E0',    // Azul principal (CaLopes)
  secondary: '#0A1A3D',  // Azul escuro
  accent: '#FF6B35',     // Laranja destaque
}
```

### Dados da Ótica
Abra cada página e edite os textos, imagens e informações:
- `src/pages/Home.jsx` - Mensagens principais
- `src/pages/Sobre.jsx` - História, missão, time
- `src/pages/Servicos.jsx` - Lista de serviços
- `src/pages/Produtos.jsx` - Catálogo de produtos
- `src/pages/Agendamento.jsx` - Formulário
- `src/components/Header.jsx` - Logo e menu
- `src/components/Footer.jsx` - Contato e redes sociais

### Imagens
Substitua os emojis/placeholders por imagens reais:
1. Crie pasta `public/images/`
2. Coloque as imagens lá
3. Importe nos componentes:
```jsx
<img src="/images/foto.jpg" alt="Descrição" />
```

### Formulário de Agendamento
Conecte a um backend ou serviço de email (ex: EmailJS, Formspree):
```jsx
// Em src/pages/Agendamento.jsx
const handleSubmit = (e) => {
  e.preventDefault()
  // Integrar com seu serviço aqui
}
```

## 📱 Estrutura de Pastas

```
template-otica/
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   └── Footer.jsx
│   ├── pages/
│   │   ├── Home.jsx
│   │   ├── Sobre.jsx
│   │   ├── Servicos.jsx
│   │   ├── Produtos.jsx
│   │   ├── Agendamento.jsx
│   │   └── Blog.jsx
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
├── public/
├── index.html
├── package.json
├── vite.config.js
├── tailwind.config.js
└── postcss.config.js
```

## 🔧 Dependências

- **React 18** - Biblioteca UI
- **React Router DOM** - Navegação multi-página
- **Tailwind CSS** - Estilização utility-first
- **React Icons** - Ícones SVG
- **Vite** - Build tool rápido

## 💡 Dicas para Customização Rápida

1. **Logo**: Altere o texto em `Header.jsx` ou adicione uma imagem
2. **Cores**: Toque no `tailwind.config.js` e use as novas cores em todo lugar automaticamente
3. **Conteúdo**: Copie/cole de um documento ou site existente
4. **Imagens**: Substitua emojis por fotos reais (melhor para vendas)
5. **CTA**: Altere o link de agendamento para WhatsApp, Calendly, etc.

## 📞 Suporte

Para dúvidas sobre o template ou customizações, consulte a documentação do React, Tailwind e Vite.

---

**Feito com ❤️ pela CaLopes Soluções Inteligentes**
