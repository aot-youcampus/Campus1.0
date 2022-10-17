import React,{useState} from 'react'
import {CgProfile} from 'react-icons/cg'
import A from '../../images/A.jpg'
import O from '../../images/Vector.jpg'
import T from '../../images/T.jpg'
import {Nav,NavbarContainer,NavName,NavNameA,NavNameO,NavNameT,NavIcon2} from './NavbarElements'
import {Link} from 'react-router-dom'
import './navbar.css'


const Navbar = () => {

  //to change the burger class
  const [burger_class,setBurgerClass] = useState("burger-bar unclicked")
  const [menu_class,setMenuClass] = useState("menu hidden")
  const [isMenuClicked,setIsMenuClicked] = useState(false)

  //toggle burger menu change
  const updateMenu = () => {
    if(!isMenuClicked){
      setBurgerClass("burger-bar clicked")
      setMenuClass("menu visible")
    }
    else{
      setBurgerClass("burger-bar unclicked")
      setMenuClass("menu hidden")
    }
    setIsMenuClicked(!isMenuClicked)
  }

  return (
    <>
      <Nav>
        <NavbarContainer>
            <div className="burger-menu" onClick={updateMenu}>
              <div className={burger_class}></div>
              <div className={burger_class}></div>
              <div className={burger_class}></div>
            </div> 
            <NavName>
                <NavNameA>
                <img src={A} alt='' height={40} width={40}/>
                </NavNameA>
                <NavNameO>
                <img src={O} alt='' height={40} width={40}/>
                </NavNameO>
                <NavNameT>
                <img src={T} alt='' height={40} width={40} />
                </NavNameT>
            </NavName>
            <NavIcon2 >
               <Link to='/profile'>
                <CgProfile size='30'/>
               </Link>
            </NavIcon2>
        </NavbarContainer>
    </Nav>  
     <div className={menu_class}>
          <ul>
            <li><Link to='/home'>
              Home
              </Link>
            </li>
            <li><Link to='/profile'>
              Profile
              </Link>
            </li>
            <li><Link to='/'>
              Create Pole
              </Link>
            </li>
            <li><Link to='/'>
              Request a Live Session
              </Link>
            </li>
            <li><Link to='/'>
              Developer Team
              </Link>
            </li>
            <li><Link to='/'>
              About Us
              </Link>
            </li>
            <li><Link to='/'>
              Contact Us
              </Link>
            </li>
          </ul>
      </div>   
         
    </>
  )
}

export default Navbar
