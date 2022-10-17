import { Main,NavMenu,LINK } from './bottomBar'
import {RiChat1Fill, RiComputerFill} from 'react-icons/ri'
import {FiGlobe} from 'react-icons/fi'
import {FaBookOpen,FaHome} from 'react-icons/fa'
import {Link} from 'react-router-dom'


import React from 'react'

const Bottombar = () => {
  return (
    <>
    <Main>
        <NavMenu>
            <LINK>
                <Link to='/home'>
                    <FaHome size='30'/>
                </Link>
            </LINK>
            <LINK>    
                <Link to='/studymaterial'>
                    <FaBookOpen size='30'/>
                </Link>
            </LINK>    
            <LINK>    
                <Link to='/chat'>
                    <RiChat1Fill size='30'/>
                </Link>
            </LINK>
            <LINK>    
                <Link to='/browse'>
                    <FiGlobe size='30'/>
                </Link>
            </LINK>     
            <LINK>        
                <Link to='/pc'>
                    <RiComputerFill size='30'/>
                </Link>           
            </LINK>
        </NavMenu>
    </Main> 
      
    </>
  )
}

export default Bottombar
