import { useState } from 'react'
import { Link } from 'react-router-dom'
import { FiMenu, FiX } from 'react-icons/fi'

export default function Header() {
  const [isOpen, setIsOpen] = useState(false)

  const toggleMenu = () => setIsOpen(!isOpen)

  return (
    <header className="bg-white shadow-md sticky top-0 z-50">
      <div className="container-max">
        <div className="flex justify-between items-center py-4">
          <Link to="/" className="flex items-center">
            <span className="text-2xl font-bold text-blue-600">Óptica</span>
            <span className="text-2xl font-bold text-gray-800">Pro</span>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex gap-8">
            <Link to="/" className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              Home
            </Link>
            <Link to="/sobre" className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              Sobre
            </Link>
            <Link to="/servicos" className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              Serviços
            </Link>
            <Link to="/produtos" className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              Produtos
            </Link>
            <Link to="/blog" className="text-gray-700 hover:text-blue-600 transition-colors font-medium">
              Blog
            </Link>
          </nav>

          <Link to="/agendamento" className="hidden md:block btn-primary">
            Agendar Consulta
          </Link>

          {/* Mobile Menu Button */}
          <button onClick={toggleMenu} className="md:hidden text-2xl">
            {isOpen ? <FiX /> : <FiMenu />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <nav className="md:hidden pb-4 border-t pt-4">
            <div className="flex flex-col gap-4">
              <Link to="/" className="text-gray-700 hover:text-blue-600 font-medium" onClick={() => setIsOpen(false)}>
                Home
              </Link>
              <Link to="/sobre" className="text-gray-700 hover:text-blue-600 font-medium" onClick={() => setIsOpen(false)}>
                Sobre
              </Link>
              <Link to="/servicos" className="text-gray-700 hover:text-blue-600 font-medium" onClick={() => setIsOpen(false)}>
                Serviços
              </Link>
              <Link to="/produtos" className="text-gray-700 hover:text-blue-600 font-medium" onClick={() => setIsOpen(false)}>
                Produtos
              </Link>
              <Link to="/blog" className="text-gray-700 hover:text-blue-600 font-medium" onClick={() => setIsOpen(false)}>
                Blog
              </Link>
              <Link to="/agendamento" className="btn-primary text-center" onClick={() => setIsOpen(false)}>
                Agendar Consulta
              </Link>
            </div>
          </nav>
        )}
      </div>
    </header>
  )
}
