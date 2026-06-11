import { Link } from 'react-router-dom'
import { FiEye, FiShoppingBag, FiUserCheck } from 'react-icons/fi'

export default function Home() {
  return (
    <div>
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-24">
        <div className="container-max text-center">
          <h1 className="text-5xl font-bold mb-6">Sua Visão, Nossa Prioridade</h1>
          <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
            Óculos e lentes de qualidade premium para toda a família. Diagnóstico preciso e estilo que combina com você.
          </p>
          <div className="flex gap-4 justify-center flex-wrap">
            <Link to="/agendamento" className="bg-white text-blue-600 px-8 py-3 rounded-lg font-bold hover:bg-gray-100 transition-colors">
              Agendar Consulta Gratuita
            </Link>
            <Link to="/servicos" className="border-2 border-white text-white px-8 py-3 rounded-lg font-bold hover:bg-white hover:text-blue-600 transition-colors">
              Conhecer Serviços
            </Link>
          </div>
        </div>
      </section>

      {/* Why Choose Us */}
      <section className="py-16 bg-gray-50">
        <div className="container-max">
          <h2 className="text-4xl font-bold text-center mb-12">Por que escolher a gente?</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-lg shadow-md text-center">
              <div className="flex justify-center mb-4">
                <FiEye size={40} className="text-blue-600" />
              </div>
              <h3 className="text-xl font-bold mb-3">Tecnologia Avançada</h3>
              <p className="text-gray-600">
                Equipamentos de última geração para diagnóstico preciso e recomendações personalizadas.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md text-center">
              <div className="flex justify-center mb-4">
                <FiShoppingBag size={40} className="text-blue-600" />
              </div>
              <h3 className="text-xl font-bold mb-3">Marcas Premium</h3>
              <p className="text-gray-600">
                Acervo com as melhores marcas nacionais e internacionais de óculos e lentes.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md text-center">
              <div className="flex justify-center mb-4">
                <FiUserCheck size={40} className="text-blue-600" />
              </div>
              <h3 className="text-xl font-bold mb-3">Atendimento Especializado</h3>
              <p className="text-gray-600">
                Profissionais qualificados dedicados ao melhor atendimento e orientação.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="py-16">
        <div className="container-max">
          <h2 className="text-4xl font-bold mb-12">Produtos em Destaque</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {['Óculos de Sol Premium', 'Lentes Progressivas', 'Armações Infantis'].map((product, idx) => (
              <div key={idx} className="bg-gray-100 rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                <div className="h-48 bg-gradient-to-br from-blue-300 to-blue-500 flex items-center justify-center">
                  <span className="text-white text-6xl">👁️</span>
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-bold mb-2">{product}</h3>
                  <p className="text-gray-600 mb-4">Qualidade e estilo para você</p>
                  <Link to="/produtos" className="text-blue-600 font-semibold hover:underline">
                    Ver detalhes →
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-blue-600 text-white py-16">
        <div className="container-max text-center">
          <h2 className="text-3xl font-bold mb-6">Não deixe para depois</h2>
          <p className="text-lg mb-8">Marque sua consulta gratuita e descubra qual é a melhor solução para você</p>
          <Link to="/agendamento" className="bg-white text-blue-600 px-8 py-3 rounded-lg font-bold hover:bg-gray-100 transition-colors inline-block">
            Agendar Agora
          </Link>
        </div>
      </section>
    </div>
  )
}
