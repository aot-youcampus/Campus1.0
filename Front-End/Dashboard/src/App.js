import './App.css';
import Navbar from './components/Navbar'
import Bottombar from './components/Bottombar'
import { Route, Routes } from 'react-router-dom';
// import {Home,Studymaterial,Chat,Browse,Pc} from './pages'; 
import Home from './pages/Home'
import Studymaterial from './pages/Studymaterial'
import Chat from './pages/Chat'
import Browse from './pages/Browse'
import Pc from './pages/Pc'
import Profile from './pages/Profile'

function App() {
  return (
    <div>
      <Navbar/>
      <Routes>
        <Route path='/profile' element={<Profile/>}/>
      </Routes>
      <Bottombar/>
      <Routes>
        <Route path='/home' element={<Home/>}/>
        <Route path='/studymaterial' element={<Studymaterial/>}/>
        <Route path='/chat' element={<Chat/>}/>
        <Route path='/browse' element={<Browse/>}/>
        <Route path='/pc' element={<Pc/>}/>
      </Routes> 
    </div>
  );
}

export default App;
