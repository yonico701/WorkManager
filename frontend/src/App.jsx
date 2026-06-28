import Header from './components/layout/Header'
import Footer from './components/layout/Footer'

import { Routes,Route } from 'react-router-dom'

import Home from './pages/home'
import Login from './pages/login'
import Register from './pages/register'
import Jobs from './pages/jobs'
import CreateJob from './pages/createJob'
import About from './pages/about'
import Gallery from './pages/gallery'


function App() {
  return (
    <div className="min-h-screen bg-white">
      <Header />

      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/jobs" element={<Jobs/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/createJob" element={<CreateJob/>}/>
        <Route path="/gallery" element={<Gallery/>}/>
        <Route path="/about" element={<About/>}/>

      </Routes>

      

      <Footer />
    </div>
  )
}

export default App