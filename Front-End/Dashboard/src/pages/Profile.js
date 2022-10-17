import React from 'react'
import {Page} from './style'
import profile from '../images/image 3.jpg'
const Profile = () => {
  return (
    <Page>
        <div1>
              <img src={profile} alt='' height={150} width={150}/>
        </div1>
        <div2>
        <a>Your name here</a>
        </div2>
        <div3>
        <a>Stream  | Year</a>
        </div3>
        <div4>
          <int1>
            <a>Interest+</a>
          </int1>
          <int2>
            <a>Add+</a>
          </int2>
        </div4>
    </Page>    
  )
}

export default Profile
