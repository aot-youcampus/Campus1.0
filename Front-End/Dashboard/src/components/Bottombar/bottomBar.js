import styled from 'styled-components'
export const Main=styled.div`
    position: fixed;
    width:100%;
    bottom: 0;
    box-shadow: 0px -13px 50px 6px rgba(40,40,40,0.33);
    border-radius: 20px 20px 0px 0px;

    
`
export const NavMenu=styled.div`
    display:flex;
    flex-direction: row;
    justify-content:space-around ;
    align-items: center;
    width:100%;
    height: 10vh;
    
`
export const LINK=styled.div`
    position: relative;
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
            top:-20%;
            right:-27%;
            bottom: 0;
        }
    }
`
