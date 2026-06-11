import { FiFacebook, FiInstagram, FiPhone, FiMail, FiMapPin } from 'react-icons/fi'

export default function Footer() {
  return (
    <footer className="bg-gray-900 text-white mt-16">
      <div className="container-max py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="text-xl font-bold mb-4">Óptica Pro</h3>
            <p className="text-gray-400">
              Cuidando da sua saúde visual com qualidade e profissionalismo desde 2010.
            </p>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4">Menu</h4>
            <ul className="space-y-2 text-gray-400">
              <li><a href="/" className="hover:text-white transition-colors">Home</a></li>
              <li><a href="/sobre" className="hover:text-white transition-colors">Sobre</a></li>
              <li><a href="/servicos" className="hover:text-white transition-colors">Serviços</a></li>
              <li><a href="/produtos" className="hover:text-white transition-colors">Produtos</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4">Contato</h4>
            <ul className="space-y-3 text-gray-400">
              <li className="flex items-center gap-2">
                <FiPhone size={18} />
                <a href="tel:+5511999999999" className="hover:text-white transition-colors">(11) 99999-9999</a>
              </li>
              <li className="flex items-center gap-2">
                <FiMail size={18} />
                <a href="mailto:contato@oticapro.com.br" className="hover:text-white transition-colors">contato@oticapro.com.br</a>
              </li>
              <li className="flex items-start gap-2">
                <FiMapPin size={18} className="mt-1" />
                <span>Rua Exemplo, 123<br />São Paulo - SP</span>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4">Redes Sociais</h4>
            <div className="flex gap-4">
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <FiFacebook size={24} />
              </a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">
                <FiInstagram size={24} />
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
          <p>&copy; 2024 Óptica Pro. Todos os direitos reservados.</p>
        </div>
      </div>
    </footer>
  )
}
