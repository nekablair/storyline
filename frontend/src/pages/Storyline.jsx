import React, { useState } from 'react'
import Bookcard from '../components/Bookcard'
import axios from 'axios'

const Storyline = () => {
  const [words, setWords] = useState("")
  const [story, setStory] = useState("")

  const generate_story = async () => {
    try {
    let response = await axios.get(`http://127.0.0.1:8000/api/v1/story/generate_story/`, {
      params: {words: words}
    })
    setStory(response.data.story)

    } catch (error) {
      console.error('Error fetching story: ', error)
    }
    // if (response.status === 200 || response.status === 201) {
    //   let token = response.data.token;
    //   // api.defaults.headers.common["Authorization"] = `Token ${token}`
    //   localStorage.setItem("token", token)
    //   return response.data.user;
    // } else {
    //   alert("There was a problem with your story being made, try again!")
    // }
  }

  return (
    <>
      <div>Storyline</div>
      <input type='text' value={words} onChange={(e) => setWords(e.target.value)} placeholder='Enter some words to make a story' style={{width: '300px'}} />
      <button onClick={generate_story}>Generate Story</button>
      {story && <p>{story}</p>}
      <Bookcard />
    </>
  )
}

export default Storyline