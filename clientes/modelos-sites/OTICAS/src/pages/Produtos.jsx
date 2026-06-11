import { useState } from 'react'

export default function Produtos() {
  const [filtro, setFiltro] = useState('todos')

  const produtos = [
    { id: 1, nome: 'Óculos de Sol Premium', categoria: 'oculo-sol', preco: 'R$ 450', imagem: '😎' },
    { id: 2, nome: 'Armação Clássica', categoria: 'armacao', preco: 'R$ 280', imagem: '👓' },
    { id: 3, nome: 'Lentes Progressivas', categoria: 'lente', preco: 'R$ 800', imagem: '👁️' },
    { id: 4, nome: 'Armação Infantil', categoria: 'infantil', preco: 'R$ 180', imagem: '👦' },
    { id: 5, nome: 'Óculos Gamer', categoria: 'gamer', preco: 'R$ 350', imagem: '🎮' },
    { id: 6, nome: 'Lentes de Contato', categoria: 'lente', preco: 'R$ 120/caixa', imagem: '💧' },
  ]

  const categorias = [
    { id: 'todos', label: 'Todos' },
    { id: 'oculo-sol', label: 'Óculos de Sol' },
    { id: 'armacao', label: 'Armações' },
    { id: 'lente', label: 'Lentes' },
    { id: 'infantil', label: 'Infantil' },
    { id: 'gamer', label: 'Gamer' },
  ]

  const produtosFiltrados = filtro === 'todos'
    ? produtos
    : produtos.filter(p => p.categoria === filtro)

  return (
    <div>
      {/* Header */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-16">
        <div className="container-max">
          <h1 className="text-4xl font-bold">Nossos Produtos</h1>
          <p className="text-blue-100 mt-2">Qualidade premium com melhor preço</p>
        </div>
      </section>

      {/* Filtros */}
      <section className="py-12">
        <div className="container-max">
          <div className="flex flex-wrap gap-4 justify-center">
            {categorias.map(cat => (
              <button
                key={cat.id}
                onClick={() => setFiltro(cat.id)}
                className={`px-6 py-2 rounded-full font-semibold transition-colors ${
                  filtro === cat.id
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-200 text-gray-800 hover:bg-gray-300'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* Grid de Produtos */}
      <section className="py-12">
        <div className="container-max">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {produtosFiltrados.map(produto => (
              <div key={produto.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
                <div className="bg-gradient-to-br from-blue-300 to-blue-500 h-48 flex items-center justify-center">
                  <span className="text-6xl">{produto.imagem}</span>
                </div>
                <div className="p-6">
                  <h3 className="text-lg font-bold mb-2">{produto.nome}</h3>
                  <p className="text-blue-600 text-2xl font-bold mb-4">{produto.preco}</p>
                  <div className="flex gap-3">
                    <button className="flex-1 bg-blue-600 text-white py-2 rounded-lg font-semibold hover:bg-blue-700 transition-colors">
                      Ver Detalhes
                    </button>
                    <button className="flex-1 border-2 border-blue-600 text-blue-600 py-2 rounded-lg font-semibold hover:bg-blue-50 transition-colors">
                      Adicionar
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Info */}
      <section className="py-16 bg-gray-50">
        <div className="container-max">
          <h2 className="text-2xl font-bold mb-8">Como escolher?</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <h3 className="font-bold mb-3 flex items-center gap-2">
                <span className="text-2xl">1️⃣</span> Identifique sua necessidade
              </h3>
              <p className="text-gray-600">Você precisa de proteção solar, leitura ou uso diário?</p>
            </div>
            <div>
              <h3 className="font-bold mb-3 flex items-center gap-2">
                <span className="text-2xl">2️⃣</span> Escolha a armação
              </h3>
              <p className="text-gray-600">Encontre um estilo que combina com seu rosto e personalidade</p>
            </div>
            <div>
              <h3 className="font-bold mb-3 flex items-center gap-2">
                <span className="text-2xl">3️⃣</span> Selecione as lentes
              </h3>
              <p className="text-gray-600">Lentes certas para sua prescrição e estilo de vida</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
