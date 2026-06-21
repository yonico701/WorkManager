import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons"


function Hero()  {
    return(
        <div className="search">
            <h1> welcome to WorkManager</h1><br></br>
            <h2>Find professionals and manage jobs easily</h2><br></br>
            <input className="search" type="text" placeholder="Search..."  ></input>
            <button className="search-button" type="button" > <FontAwesomeIcon icon={faMagnifyingGlass} />  </button>


        </div>
    )
}

export default Hero