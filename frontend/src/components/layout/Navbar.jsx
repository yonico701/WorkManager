import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-regular-svg-icons'
import { faHammer } from '@fortawesome/free-solid-svg-icons'

function Navbar() {
  const [isLoginOpen, setIsLoginOpen] = useState(false)

  const navigation = [
    { label: 'HOME', path: '/' },
    { label: 'JOBS', path: '/jobs' },
    { label: 'GALLERY', path: '/gallery' },
    { label: 'ABOUT', path: '/about' },
  ]

  const handleLoginMenu = () => {
    setIsLoginOpen(!isLoginOpen)
  }

  return (
    <nav className="left-0 z-50 grid w-full grid-cols-3 items-center px-8 py-6">
      <NavLink to="/" className="text-2xl font-bold text-indigo-600">
        WorkManager <FontAwesomeIcon icon={faHammer} />
      </NavLink>

      <ul className="hidden justify-center gap-10 text-sm font-semibold text-gray-900 md:flex">
        {navigation.map((item) => (
          <li key={item.path}>
            <NavLink
                to={item.path}
                className={({ isActive }) =>
                    `inline-block text-xl transition-all duration-200 hover:-translate-y-0.5 hover:text-indigo-600 ${
                    isActive ? 'text-indigo-600 font-bold underline underline-offset-8' : ''
                    }`
                }
                >
                {item.label}
            </NavLink>
          </li>
        ))}
      </ul>

      <div className="relative hidden justify-self-end md:block">
        <button
          onClick={handleLoginMenu}
          className="cursor-pointer text-xl font-semibold text-gray-900 transition duration-200 hover:text-indigo-600"
        >
          <FontAwesomeIcon icon={faUser} />
        </button>

        {isLoginOpen && (
          <div className="absolute right-0 mt-4 w-44 rounded-xl bg-white p-2 shadow-lg ring-1 ring-gray-900/10">
            <NavLink
              to="/login"
              className="block rounded-lg px-4 py-2 text-sm font-semibold text-gray-700 hover:bg-gray-50 hover:text-indigo-600"
            >
              Login
            </NavLink>

            <NavLink
              to="/register"
              className="block rounded-lg px-4 py-2 text-sm font-semibold text-gray-700 hover:bg-gray-50 hover:text-indigo-600"
            >
              Register
            </NavLink>
          </div>
        )}
      </div>
    </nav>
  )
}

export default Navbar