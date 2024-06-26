import { useState, useEffect} from 'react'
import NavBar from './components/NavBar'
import Footer from './components/Footer'
import { Outlet, useNavigate, useLoaderData } from 'react-router-dom'
import './App.css'
import axios from 'axios'

function App() {
  // const [user, setUser] = useState(useLoaderData)
  const [user, setUser] = useState()

  // const navigate = useNavigate()

  // useEffect(() => {
  //   if (!user) {
  //     navigate('/')
  //   }
  // }, [user])

  // const testConnection = async() => {
  //   const response = await axios.get("http://localhost:8000/api/test/")
  //   console.log(response)
  // }

  // useEffect(() => {
  //   testConnection()
  // }, [])

  return (
    <>
      <NavBar user = {user} setUser = {setUser} />
      <Outlet context={{ user, setUser }} />
      <Footer/>
    </>
  )
}

export default App
