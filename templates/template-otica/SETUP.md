# ⚡ Setup Rápido

## 1. Primeiro Setup
```bash
npm install
npm run dev
```

Vá para `http://localhost:5173` e veja o site funcionando.

## 2. Customizar em 5 Minutos

### Logo e Nome
Abra `src/components/Header.jsx` (linhas ~19):
```jsx
<span className="text-2xl font-bold text-blue-600">Óptica Pro</span>
```
Mude para o nome da ótica real.

### Contato (Telefone, Email, Endereço)
Abra `src/components/Footer.jsx` e altere:
- Linhas ~24-28: Telefone, email, endereço
- Linhas ~38-42: Links de redes sociais

### Cores Principais
Abra `tailwind.config.js` (linhas ~7-10):
```js
colors: {
  primary: '#00A3E0',    // ← Mude aqui (azul)
  secondary: '#0A1A3D',  // ← Mude aqui (escuro)
  accent: '#FF6B35',     // ← Mude aqui (destaque)
}
```

### Textos Principais
- `src/pages/Home.jsx` - Títulos, descrições, produtos em destaque
- `src/pages/Sobre.jsx` - História, team
- `src/pages/Servicos.jsx` - Lista de serviços
- `src/pages/Produtos.jsx` - Categorias, lista de produtos

## 3. Adicionar Imagens Reais

1. Crie pasta `public/images/`
2. Coloque as fotos lá
3. Em qualquer componente, substitua:

**De:**
```jsx
<span className="text-6xl">😎</span>
```

**Para:**
```jsx
<img src="/images/oculos-sol.jpg" alt="Óculos de Sol" className="w-full h-48 object-cover" />
```

## 4. Conectar Agendamento

A página está pronta, mas precisa integrar com um serviço.

**Opções fáceis:**
- **WhatsApp**: Redirecionar para número via link
- **Calendly**: Embed do calendario
- **EmailJS**: Enviar email diretamente do formulário
- **Seu backend**: Salvar no banco de dados

Abra `src/pages/Agendamento.jsx` (função `handleSubmit`) e integre.

## 5. Deploy

**GitHub Pages (gratuito):**
```bash
npm run build
# Fazer upload da pasta 'dist' para GitHub Pages
```

**Vercel (recomendado, super fácil):**
```bash
npm install -g vercel
vercel
```

**Netlify (fácil também):**
Suba a pasta `dist` no Netlify

---

## 🎯 Checklist Antes de Entregar

- [ ] Logo/nome da ótica alterado
- [ ] Contato (telefone, email, endereço) correto
- [ ] Cores customizadas
- [ ] Imagens reais substituindo emojis
- [ ] Textos de cada página revisados
- [ ] Serviços atualizados
- [ ] Produtos adicionados/removidos
- [ ] Formulário de agendamento integrado
- [ ] Redes sociais linkadas
- [ ] Testado em mobile/tablet/desktop

---

**Pronto! Você tem um site profissional para uma ótica em poucos minutos.**
