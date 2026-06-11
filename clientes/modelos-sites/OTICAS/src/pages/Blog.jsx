export default function Blog() {
  const posts = [
    {
      id: 1,
      titulo: '5 Sinais de que você precisa de óculos',
      descricao: 'Reconheça os principais sinais que indicam que é hora de fazer uma avaliação da visão.',
      data: '10 de junho de 2024',
      categoria: 'Saúde',
      imagem: '👓'
    },
    {
      id: 2,
      titulo: 'Como escolher óculos de sol de qualidade',
      descricao: 'Dicas importantes para proteger seus olhos adequadamente durante o verão.',
      data: '5 de junho de 2024',
      categoria: 'Produtos',
      imagem: '😎'
    },
    {
      id: 3,
      titulo: 'Lentes progressivas: vale a pena?',
      descricao: 'Entenda os benefícios das lentes progressivas e se são ideais para você.',
      data: '28 de maio de 2024',
      categoria: 'Saúde',
      imagem: '👁️'
    },
    {
      id: 4,
      titulo: 'Cuidados com óculos de computador',
      descricao: 'Reduza o cansaço visual durante longas horas em frente à tela.',
      data: '20 de maio de 2024',
      categoria: 'Dicas',
      imagem: '💻'
    },
    {
      id: 5,
      titulo: 'Armações que combinam com seu rosto',
      descricao: 'Descubra qual formato de armação valoriza melhor seus traços.',
      data: '15 de maio de 2024',
      categoria: 'Estilo',
      imagem: '🎨'
    },
    {
      id: 6,
      titulo: 'Saúde visual em crianças: o que todo pai precisa saber',
      descricao: 'Informações essenciais sobre o desenvolvimento da visão infantil.',
      data: '10 de maio de 2024',
      categoria: 'Saúde',
      imagem: '👦'
    },
  ]

  return (
    <div>
      {/* Header */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-16">
        <div className="container-max">
          <h1 className="text-4xl font-bold">Blog</h1>
          <p className="text-blue-100 mt-2">Dicas e informações sobre saúde visual</p>
        </div>
      </section>

      {/* Posts */}
      <section className="py-16">
        <div className="container-max">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
            {posts.slice(0, 4).map(post => (
              <article key={post.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
                <div className="bg-gradient-to-br from-blue-300 to-blue-500 h-40 flex items-center justify-center">
                  <span className="text-5xl">{post.imagem}</span>
                </div>
                <div className="p-6">
                  <div className="flex items-center gap-4 mb-3">
                    <span className="text-sm bg-blue-100 text-blue-700 px-3 py-1 rounded-full">
                      {post.categoria}
                    </span>
                    <span className="text-sm text-gray-500">{post.data}</span>
                  </div>
                  <h3 className="text-xl font-bold mb-3">{post.titulo}</h3>
                  <p className="text-gray-600 mb-4">{post.descricao}</p>
                  <a href="#" className="text-blue-600 font-semibold hover:underline">
                    Ler mais →
                  </a>
                </div>
              </article>
            ))}
          </div>

          {/* Ver mais */}
          <div className="text-center mb-16">
            <button className="bg-blue-600 text-white px-8 py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors">
              Carregar mais posts
            </button>
          </div>

          {/* Newsletter */}
          <section className="bg-blue-50 p-8 rounded-lg">
            <h2 className="text-2xl font-bold mb-4">Receba nossas dicas por email</h2>
            <p className="text-gray-600 mb-6">
              Inscreva-se para receber artigos sobre saúde visual, dicas de cuidado e promoções exclusivas.
            </p>
            <div className="flex gap-3 max-w-md">
              <input
                type="email"
                placeholder="seu@email.com"
                className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-600"
              />
              <button className="bg-blue-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors">
                Inscrever
              </button>
            </div>
          </section>
        </div>
      </section>
    </div>
  )
}
