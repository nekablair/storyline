// import React from 'react'
import React, { useState } from 'react'
import Bookcard from '../components/Bookcard'
import axios from 'axios'

const Storyline = () => {
  const [words, setWords] = useState("")
  const [story, setStory] = useState("")
  const [image, setImage] = useState("")

  const generate_story = async () => {
    try {
    let response = await axios.get(`http://127.0.0.1:8000/api/v1/story/generate_story/`, {
      params: {words: words}
    })
    setStory(response.data.story)
    console.log(response)
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

  const generate_image = async () => {
    // const storyResponse = await axios.get('http://localhost:8000/api/v1/story/generate_story/', {
    //     params: { text: words }
    //   });
    //   setStory(storyResponse.data.story);
    try {
      const imageResponse = await axios.get('http://localhost:8000/api/v1/images/generate_image/', {
        params: { text: words }
      });
      setImage(imageResponse.data.image);
      console.log(imageResponse)
    } catch (error) {
        console.error('Error fetching content:', error);
    }
      
      
    }

  return (
    <>
      <div>Storyline</div>
      <input type='text' value={words} onChange={(e) => setWords(e.target.value)} placeholder='Enter some words to make a story' style={{width: '300px'}} />
      <button onClick={generate_story}>Generate Story</button>
      {story && <p>{story}</p>}
      <button onClick={generate_image}>Generate Image</button>
      {/* {image && <img src={image} alt='Generated Image' />} */}
      {image && <div>{image.url}</div>}
      <Bookcard />
    </>
  )
}























// import React, { useState } from 'react'
// import Bookcard from '../components/Bookcard'
// import axios from 'axios'

// const Storyline = () => {
//   const [words, setWords] = useState("")
//   const [story, setStory] = useState("")
//   const [image, setImage] = useState("")

//   const generate_story = async () => {

//     const csrftoken = getCookie('csrftoken');

//     try {
//     let response = await axios.get(`http://127.0.0.1:8000/api/v1/story/generate_story/`, {
//       // params: {words: words}
//       words: words
//     },{
//       headers: {
//           'X-CSRFToken': csrftoken
//       }
//     })
//     setStory(response.data)
//     console.log(story)
//     } catch (error) {
//       console.error('Error fetching story: ', error)
//     }
//   }

//   function getCookie(name) {
//     const value = `; ${document.cookie}`;
//     const parts = value.split(`; ${name}=`);
//     if (parts.length === 2) return parts.pop().split(';').shift();
//   }

//     const generate_image = async () => {
//       try {
//       let response = await axios.get(`http://127.0.0.1:8000/api/v1/images/generate_image/`, {
//         // params: {words: words}
//         words: words
//       })
//       setImage(response.data)
//       console.log(image)
  
//       } catch (error) {
//       console.error('Error fetching image: ', error)
//   }}

//   // const generateContent = async () => {
//   //   try {
//   //     // Call the backend API to generate story
//   //     console.log(words)
//   //     const storyResponse = await axios.get(`http://localhost:8000/api/v1/story/generate_story/`, { 
//   //       params: { words: words }
//   //     });
//   //     setStory(storyResponse.data.story);
//   //     console.log(storyResponse.data)

//   //     // Call the backend API to generate image
//   //     const imageResponse = await axios.get('http://localhost:8000/api/v1/images/generate_image/', { 
//   //       params: { words: words }
//   //     });
//   //     setImage(imageResponse.data.image);
//   //     console.log(image)
//   //   } catch (error) {
//   //     console.error('Error fetching content:', error);
//   //   }
//   // };

//   return (
//     <>
//       <div>Storyline</div>
//       <input type='text' onChange={(e) => setWords(e.target.value)} placeholder='Enter some words to make a story' style={{width: '300px'}} />
//       <button onClick={generate_story}>Generate Story</button>
//       {story && <p>{story.text}</p>}
//       {/* this generates images and is working */}
//       <button onClick={generate_image}>Generate Image</button>
//       {/* {image && <div>{image}</div>} */}
//       {image && <img src={image.url} alt='Generated Image' />}
      
//       <Bookcard />
//     </>
//   )
// }


export default Storyline