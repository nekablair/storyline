import React, { useState } from 'react'
import Bookcard from '../components/Bookcard'
import axios from 'axios'

const Storyline = () => {
  const [words, setWords] = useState("")
  const [story, setStory] = useState("")
  const [image, setImage] = useState("")

  // const generate_story = async () => {
  //   try {
  //   let response = await axios.get(`http://127.0.0.1:8000/api/v1/story/generate_story/`, {
  //     params: {words: words}
  //   })
  //   setStory(response.data.story)

  //   } catch (error) {
  //     console.error('Error fetching story: ', error)
  //   }

  //   const generate_image = async () => {
  //     try {
  //     let response = await axios.get(`http://127.0.0.1:8000/api/v1/images/generate_image/`, {
  //       params: {words: words}
  //     })
  //     setImage(response.data.story)
  
  //     } catch (error) {
      
  // }}

  const generateContent = async () => {
    try {
      // Call the backend API to generate story
      const storyResponse = await axios.get('http://localhost:8000/api/v1/story/generate_story/', {
        params: { text: words }
      });
      setStory(storyResponse.data.story);

      // Call the backend API to generate image
      const imageResponse = await axios.get('http://localhost:8000/api/v1/images/generate_image/', {
        params: { text: words }
      });
      setImage(imageResponse.data.image);
    } catch (error) {
      console.error('Error fetching content:', error);
    }
  };

  return (
    <>
      <div>Storyline</div>
      <input type='text' value={words} onChange={(e) => setWords(e.target.value)} placeholder='Enter some words to make a story' style={{width: '300px'}} />
      <button onClick={generateContent}>Generate Story & Image</button>
      {image && <div>{image}</div>}
      {story && <p>{story}</p>}
      <Bookcard />
    </>
  )
}


export default Storyline