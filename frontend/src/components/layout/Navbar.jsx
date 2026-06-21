
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-regular-svg-icons'

function Navbar() {
return(
    <nav className="navbar-custom d-flex justify-content-between align-items-center">
        <div>
            <a className="nav-link disabled" aria-disabled="true">WorkManager</a>
        </div>

        <ul className="nav">
            <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#">HOME</a>
            </li>
            <li className="nav-item">
                <a className="nav-link" href="#">ABOUT</a>
            </li>
            <li className="nav-item">
                <a className="nav-link" href="#">JOBS</a>
            </li>
            <li className="nav-item">
                <a className="nav-link" href="#">GALLERY</a>
            </li>
            <li className="item-icon">
                

            </li>
        </ul>

        <div className="dropdown">
            <a className="nav-link dropdown-toggle" href='#' role='button' data-bs-toggle="dropdown" aria-expanded="false">
                <FontAwesomeIcon icon={faUser} />
            </a>
            <ul className='dropdown-menu dropdown-menu-end'>
                <li>
                    <a className='dropdown-item'href='#'>LOGIN </a>
                </li>
                <li>
                     <a className='dropdown-item'href='#'>REGISTER </a>
                </li>
            </ul>
        </div>
    </nav>

    )
    }

export default Navbar
