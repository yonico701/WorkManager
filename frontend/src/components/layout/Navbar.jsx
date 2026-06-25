import { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-regular-svg-icons'
import { faHammer } from "@fortawesome/free-solid-svg-icons";

function Navbar() {
  const [isLoginOpen, setIsLoginOpen] = useState(false)

  const navigation = ['Home', 'About', 'Jobs', 'Gallery']

  const handleLoginMenu = () => {
    setIsLoginOpen(!isLoginOpen)
  }

  return (
    <nav className=" left-0 z-50 grid w-full grid-cols-3 items-center px-8 py-6">
        <a href="#" className="text-2xl font-bold text-indigo-600">
            WorkManager <FontAwesomeIcon icon={faHammer} />
        </a>

        <ul className="hidden justify-center gap-10 text-sm font-semibold text-gray-900 md:flex">
            {navigation.map((item) => (
            <li key={item}>
                <a
                href="#"
                className="inline-block text-xl transition-all duration-200 hover:-translate-y-0.5 hover:text-indigo-600"
                >
                {item}
                </a>
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
                <a
                href="#"
                className="block rounded-lg px-4 py-2 text-sm font-semibold text-gray-700 hover:bg-gray-50 hover:text-indigo-600"
                >
                Login
                </a>

                <a
                href="#"
                className="block rounded-lg px-4 py-2 text-sm font-semibold text-gray-700 hover:bg-gray-50 hover:text-indigo-600"
                >
                Register
                </a>
            </div>
            )}
        </div>
    </nav>
    
  )
}

export default Navbar