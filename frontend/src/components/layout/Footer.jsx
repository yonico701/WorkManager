
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faInstagram, faFacebook, faYoutube } from '@fortawesome/free-brands-svg-icons'


function Footer() {
    return(
        <div className='footer'>
            <h1 className='footer-text'> WorkManager </h1>
            <h2 className='footer-text'>Connecting customers and professionals easily. </h2>
            <h3 className='footer-rights'>© 2026 WorkManager. All Rights Reserved. </h3>
            <h4 className='icons'><FontAwesomeIcon icon={faFacebook} />
            <FontAwesomeIcon icon={faInstagram} />
            <FontAwesomeIcon icon={faYoutube} />
            </h4>

        </div>

    )
}
export default Footer
