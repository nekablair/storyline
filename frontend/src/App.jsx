import { useState, useEffect} from 'react'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import { Outlet, useNavigate, useLoaderData } from 'react-router-dom'
import './App.css'
import axios from 'axios'

function App() {
  // const [user, setUser] = useState(useLoaderData)

  // const navigate = useNavigate()

  // useEffect(() => {
  //   if (!user) {
  //     navigate('/')
  //   }
  // }, [user])

  const testAI = async() => {
    const response = await axios.get("http://localhost:8000/api/test/")
    console.log(response)
  }

  useEffect(() => {
    testConnection()
  }, [])

  return (
    <>
      {/* <Navbar user = {user} setUser = {setUser} /> */}
      <Navbar />
      {/* <Outlet context={{ user, setUser }} /> */}
      <Outlet />
      <Footer/>
    </>
  )
}

export default App