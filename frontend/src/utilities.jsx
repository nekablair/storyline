import React from 'react'
import axios from 'axios'

export const api = axios.create({
  baseURL: import.meta.env.Vite_Base_URL,
})

export const login = async (email, password, register) => {
  let response = await api.post(`api/v1/users/${register ? "signup" : "login"}/`, {
    email:email,
    password:password,
  })
  if (response.status === 200 || response.status === 201) {
    let token = response.data.token;
    api.defaults.headers.common["Authorization"] = `Token ${token}`
    localStorage.setItem("token", token)
    return response.data.user;
  } else {
    alert("Log in failed")
  }
}

export const fetchImages = async() => {
  // try {
  // const response = await axios.get(`http://127.0.0.1:8000/api/images/an_image/${imageId}/`)
  const response = await axios.get(`http://127.0.0.1:8000/api/images/all_images/`) 
  // let response = await api.get(`/images/all_images/`)
  console.log(response)
  // console.log(response.data.images)
  // data = response.data.images
  if (response.status === 200) {
    return response.data
  }
  return []
  {/*this is working for all images, can see list in backend of app in browser, now have to render to front end browser for user to see,
  now can see the first image in the front end, though it is super large, have to add styling */}
  // console.log(response)
  // setImageData(response.data.images[0])
  // console.log(response.data.images)
  // } catch (error) {
    // console.error('Error fetching image:', error)
  }
// }