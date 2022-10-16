import styled from 'styled-components'

export const Nav=styled.nav`
    position: fixed;
    z-index: 10;
    width:100%;
    top: 0;
    background-color: white;
   
`

export const NavbarContainer=styled.div`
    display:flex;
    width:100%;
    height:10vh;
    align-items:center;
    flex-direction:row;
    justify-content:space-between;
    box-shadow:0px 4px 22px 5px rgba(89,88,88,0.14)
    
`


export const NavName=styled.div`
    display:flex;
    flex-direction:row;
    padding-top:5px;   

`
export const NavNameA=styled.div`
    
`
export const NavNameO=styled.div`
    
`
export const NavNameT=styled.div`
    
`

export const NavIcon2=styled.div`
    position:relative;
    padding-right:15px;
    &:hover{
        &::before{
            z-index: -1;
            padding:0.2rem;
            border-radius: 20px;
            width: 40px;
            height:40px;
            background-color: rgba(0,0,0,0.24);
            content: "";
            position: absolute;
            top:-25%;
            right:15%;
            bottom: 0;
            size: 15%;
        }
    }
`
