import React from 'react'
import axios from 'axios'

export const api = axios.create({
  baseURL: import.meta.env.Vite_Base_URL,
})

export const login = async (email, password, register) => {
  let response = await api.post(`users/${register ? "signup" : "login"}/`, {
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