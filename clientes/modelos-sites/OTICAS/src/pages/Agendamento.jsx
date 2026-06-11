import { useState } from 'react'

export default function Agendamento() {
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    telefone: '',
    data: '',
    hora: '',
    servico: '',
    mensagem: ''
  })

  const [enviado, setEnviado] = useState(false)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    // Aqui você conectaria a um backend/serviço de email
    setEnviado(true)
    setTimeout(() => setEnviado(false), 5000)
  }

  return (
    <div>
      {/* Header */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-16">
        <div className="container-max">
          <h1 className="text-4xl font-bold">Agendar Consulta</h1>
          <p className="text-blue-100 mt-2">Reserve seu horário agora mesmo</p>
        </div>
      </section>

      {/* Formulário */}
      <section className="py-16">
        <div className="container-max">
          <div className="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-md">
            {enviado && (
              <div className="mb-6 p-4 bg-green-100 text-green-800 rounded-lg">
                ✓ Agendamento recebido! Entraremos em contato em breve para confirmar.
              </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Nome */}
              <div>
                <label className="block font-semibold mb-2">Nome Completo *</label>
                <input
                  type="text"
                  name="nome"
                  value={formData.nome}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-600"
                  placeholder="Seu nome"
                />
              </div>

              {/* Email e Telefone */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="block font-semibold mb-2">Email *</label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-600"
                    placeholder="seu@email.com"
                  />
                </div>
                <div>
                  <label className="block font-semibold mb-2">Telefone *</label>
                  <input
                    type="tel"
                    name="telefone"
                    value={formData.telefone}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-600"
                    placeholder="(11) 99999-9999"
                  />
                </div>
              </div>

              {/* Data e Hora */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="block font-semibold mb-2">Data Desejada *</label>
                  <input
                    type="date"
                    name="data"
                    value={formData.data}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-600"
                  />
                </div>
                <div>
                  <label className="block font-semibold mb-2">Horário Preferido *</label>
                  <select
                    name="hora"
                    value={formData.hora}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-600"
                  >
                    <option value="">Selecione um horário</option>
                    <option value="09:00">09:00</option>
                    <option value="10:00">10:00</option>
                    <option value="11:00">11:00</option>
                    <option value="14:00">14:00</option>
                    <option value="15:00">15:00</option>
                    <option value="16:00">16:00</option>
                  </select>
                </div>
              </div>

              {/* Serviço */}
              <div>
                <label className="block font-semibold mb-2">Serviço Desejado *</label>
                <select
                  name="servico"
                  value={formData.servico}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-600"
                >
                  <option value="">Selecione um serviço</option>
                  <option value="consulta">Consulta de Visão</option>
                  <option value="adaptacao">Adaptação de Lentes</option>
                  <option value="estilo">Consultoria de Estilo</option>
                  <option value="manutencao">Manutenção</option>
                </select>
              </div>

              {/* Mensagem */}
              <div>
                <label className="block font-semibold mb-2">Mensagem (Opcional)</label>
                <textarea
                  name="mensagem"
                  value={formData.mensagem}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-600"
                  placeholder="Conte-nos mais sobre sua necessidade"
                  rows="4"
                />
              </div>

              {/* Botão */}
              <button
                type="submit"
                className="w-full bg-blue-600 text-white py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors"
              >
                Confirmar Agendamento
              </button>
            </form>

            {/* Info adicional */}
            <div className="mt-8 pt-8 border-t">
              <h3 className="font-bold mb-4">Outras formas de contato:</h3>
              <div className="space-y-2 text-gray-600">
                <p>📞 Telefone: (11) 3333-3333</p>
                <p>📧 Email: contato@oticapro.com.br</p>
                <p>⏰ Seg-Sex: 9h às 20h | Sábado: 9h às 15h</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
