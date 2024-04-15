import React from 'react'
import App from './App'
import Home from './pages/Home'
import Errorpage from './pages/Errorpage'
import Notfoundpage from './pages/Notfoundpage'
import Finalstoryline from './pages/Finalstoryline'
import Login from './pages/Login'
import Signup from './pages/Signup'
import Storyline from './pages/Storyline'
import Progression from './pages/Progression'
import { createBrowserRouter } from 'react-router-dom'


const router = createBrowserRouter([{
    path:'/',
    // loader: getInfo,
    element: <App/>,
    errorElement: <Errorpage/>,
    children: [
        {
            index: true,
            element: <Home/>
        },
        {
            path:"login/",
            element: <Login/>
        },
        {
            path:"signup/",
            element: <Signup/>
        },
        {
            path:"storyprogress/",
            element: <Progression/>
        },
        { 
            path:"storyline/",
            element: <Storyline/>
        },
        {
            path:"finalstory/",
            element: <Finalstoryline/>
        },
        {
            path:"*",
            element:<Notfoundpage/>
        }
    ]
}]) 

export default router
