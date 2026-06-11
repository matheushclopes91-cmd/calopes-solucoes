import { FiCheck } from 'react-icons/fi'

export default function Servicos() {
  return (
    <div>
      {/* Header */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-16">
        <div className="container-max">
          <h1 className="text-4xl font-bold">Nossos Serviços</h1>
          <p className="text-blue-100 mt-2">Soluções completas para sua saúde visual</p>
        </div>
      </section>

      {/* Serviços */}
      <section className="py-16">
        <div className="container-max">
          <div className="space-y-16">
            {[
              {
                title: 'Teste da Visão Completo',
                description: 'Avaliação completa de sua saúde ocular com equipamentos de última geração',
                features: ['Refratometria digital', 'Topografia corneana', 'Teste de pressão ocular', 'Análise de cores'],
                icon: '👓'
              },
              {
                title: 'Adaptação de Lentes de Contato',
                description: 'Serviço especializado de adaptação com lentes da melhor qualidade',
                features: ['Medição precisa', 'Testes de conforto', 'Treinamento de uso', 'Acompanhamento pós-venda'],
                icon: '👁️'
              },
              {
                title: 'Consulta de Estilo',
                description: 'Ajuda profissional para escolher os óculos perfeitos para seu rosto e estilo',
                features: ['Análise de formato de rosto', 'Sugestão de cores', 'Consultoria de moda', 'Garantia de satisfação'],
                icon: '✨'
              },
              {
                title: 'Limpeza e Manutenção',
                description: 'Cuidado profissional para seus óculos durarem mais',
                features: ['Limpeza profunda', 'Ajuste de armação', 'Polimento de lentes', 'Troca de hastes'],
                icon: '🧼'
              }
            ].map((servico, idx) => (
              <div key={idx} className="border-b pb-12 last:border-b-0">
                <div className="flex items-start gap-6">
                  <div className="text-5xl">{servico.icon}</div>
                  <div className="flex-1">
                    <h3 className="text-2xl font-bold mb-3">{servico.title}</h3>
                    <p className="text-gray-600 mb-6">{servico.description}</p>
                    <ul className="grid grid-cols-1 md:grid-cols-2 gap-3">
                      {servico.features.map((feature, i) => (
                        <li key={i} className="flex items-center gap-2 text-gray-700">
                          <FiCheck className="text-blue-600 flex-shrink-0" size={20} />
                          {feature}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Diferenciais */}
      <section className="py-16 bg-blue-50">
        <div className="container-max">
          <h2 className="text-3xl font-bold text-center mb-12">Por que nossos serviços são diferenciados</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="flex gap-4">
              <div className="text-3xl flex-shrink-0">🎯</div>
              <div>
                <h3 className="font-bold mb-2">Diagnóstico Preciso</h3>
                <p className="text-gray-600">Utilizamos equipamentos de última geração para diagnóstico 100% preciso</p>
              </div>
            </div>
            <div className="flex gap-4">
              <div className="text-3xl flex-shrink-0">⏱️</div>
              <div>
                <h3 className="font-bold mb-2">Atendimento Rápido</h3>
                <p className="text-gray-600">Horários flexíveis e agenda otimizada para sua comodidade</p>
              </div>
            </div>
            <div className="flex gap-4">
              <div className="text-3xl flex-shrink-0">💰</div>
              <div>
                <h3 className="font-bold mb-2">Preços Justos</h3>
                <p className="text-gray-600">Oferecemos ótimo custo-benefício com qualidade garantida</p>
              </div>
            </div>
            <div className="flex gap-4">
              <div className="text-3xl flex-shrink-0">🤝</div>
              <div>
                <h3 className="font-bold mb-2">Garantia Total</h3>
                <p className="text-gray-600">Todos os produtos e serviços possuem garantia de satisfação</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
