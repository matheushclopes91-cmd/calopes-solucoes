export default function Sobre() {
  return (
    <div>
      {/* Header */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-16">
        <div className="container-max">
          <h1 className="text-4xl font-bold">Sobre Nós</h1>
          <p className="text-blue-100 mt-2">Conheça a história e missão da Óptica Pro</p>
        </div>
      </section>

      {/* Historia */}
      <section className="py-16">
        <div className="container-max">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl font-bold mb-6">Nossa História</h2>
              <p className="text-gray-600 mb-4">
                Desde 2010, a Óptica Pro está comprometida em oferecer as melhores soluções em saúde visual. O que começou como um pequeno projeto se transformou em referência no atendimento especializado.
              </p>
              <p className="text-gray-600 mb-4">
                Com mais de uma década de experiência, nosso time de profissionais qualificados trabalha diariamente para garantir que cada cliente saia com a melhor solução para sua visão.
              </p>
              <p className="text-gray-600">
                Acreditamos que qualidade e humanidade caminham juntas. Por isso, investimos em tecnologia de ponta e em gente preparada para ouvir suas necessidades.
              </p>
            </div>
            <div className="bg-gradient-to-br from-blue-300 to-blue-500 rounded-lg h-96 flex items-center justify-center">
              <span className="text-white text-8xl">👁️</span>
            </div>
          </div>
        </div>
      </section>

      {/* Missão, Visão, Valores */}
      <section className="py-16 bg-gray-50">
        <div className="container-max">
          <h2 className="text-3xl font-bold text-center mb-12">Nossos Pilares</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-lg shadow-md">
              <h3 className="text-2xl font-bold text-blue-600 mb-4">Missão</h3>
              <p className="text-gray-600">
                Proporcionar soluções visuais que transformam vidas, combinando tecnologia de ponta com atendimento humanizado e personalizado.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md">
              <h3 className="text-2xl font-bold text-blue-600 mb-4">Visão</h3>
              <p className="text-gray-600">
                Ser a óptica mais confiável da região, conhecida pela qualidade, inovação e pelo cuidado genuíno com cada cliente.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md">
              <h3 className="text-2xl font-bold text-blue-600 mb-4">Valores</h3>
              <ul className="text-gray-600 space-y-2">
                <li>✓ Integridade e transparência</li>
                <li>✓ Qualidade em tudo</li>
                <li>✓ Respeito ao cliente</li>
                <li>✓ Inovação contínua</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Team */}
      <section className="py-16">
        <div className="container-max">
          <h2 className="text-3xl font-bold text-center mb-12">Nosso Time</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {['Dr. João Silva', 'Dra. Maria Santos', 'Especialista em Lentes'].map((name, idx) => (
              <div key={idx} className="text-center">
                <div className="bg-gradient-to-br from-blue-300 to-blue-500 rounded-lg h-64 flex items-center justify-center mb-4">
                  <span className="text-white text-6xl">👤</span>
                </div>
                <h3 className="text-xl font-bold">{name}</h3>
                <p className="text-gray-600">Óptico Especializado</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}
