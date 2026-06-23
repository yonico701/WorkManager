import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-regular-svg-icons'
import { useState } from 'react'




function Navbar() {

    const [isOpen, setIsOpen] = useState(false)

    const handlUserMenu = () => {
        setIsOpen(!isOpen)
    }

    return(
        <nav className="relative flex items-center px-6 py-4 bg-blue-500 text-white shadow-md  text-lg font-semibold border-b border-gray-50 rounded-lg z-50 overflow-visible w-full"> 
            <div className="text-2xl text-orange-500">
                WorkManager
            </div>
            <ul className="flex gap-6 absolute left-1/2 transform -translate-x-1/2 ">
                <li className=" hover:text-blue-300  hover:scale-105 transition duration-200 hover:opacity-95">
                    <a href="#">HOME</a>
                </li>
                <li className=" hover:text-blue-300  hover:scale-105 transition duration-200 hover:opacity-95" >
                    <a href="#">ABOUT</a>
                </li>
                <li className=" hover:text-blue-300  hover:scale-105 transition duration-200 hover:opacity-95">
                    <a href="#">JOBS</a>
                </li>
                <li className=" hover:text-blue-300  hover:scale-105 transition duration-200 hover:opacity-95">
                    <a href="#">GALLERY</a>
                </li>
                <li>
                    

                </li>
            </ul>
            <div className="absolute right-15 top-1/2 -translate-y-1/2">
                <div className=" relative">
                    <button onClick={handlUserMenu}
                    className=" hover:text-blue-300  hover:scale-105 transition duration-200 hover:opacity-95 cursor-pointer ml-auto">
                        <FontAwesomeIcon icon={faUser} />
                    </button>
                    {isOpen && (
                        <div className="absolute left-1/2 top-full mt-3 w-40 -translate-x-1/2 bg-white text-gray-800 rounded-xl shadow-lg border border-gray-200 z-[999]">
                            <ul>
                                <li>
                                    LOGIN
                                </li>
                                <li>
                                    SIGN UP
                                </li>
                            </ul>
                        </div>
                    )}
                </div>
            </div>
            

        </nav>

        )
        }

export default Navbar
