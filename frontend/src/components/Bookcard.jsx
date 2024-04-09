import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { fetchImages } from '../utilities'

function Bookcard({ imageId }) {
  const [imageData, setImageData] = useState(null)

  // useEffect(() => {
  //   const fetchImage = async() => {
  //     try {
  //     // const response = await axios.get(`http://127.0.0.1:8000/api/images/an_image/${imageId}/`)
  //     const response = await axios.get(`http://127.0.0.1:8000/api/images/all_images/`) 
  //     {/*this is working for all images, can see list in backend of app in browser, now have to render to front end browser for user to see,
  //     now can see the first image in the front end, though it is super large, have to add styling */}
  //     console.log(response)
  //     setImageData(response.data.images[0])
  //     console.log(response.data.images)
  //   } catch (error) {
  //       console.error('Error fetching image:', error)
  //   }
  // }
  //   fetchImage()
  // }, [imageId])
  useEffect(() => {
    const listImages = async () => {
      try {
        let response = await fetchImages()
        if (response.images) {
          //I had to convert the binary data into a format that could be utilized, in this case a url
          const images = response.images.map(imageData => ({url: `data:image/jpeg;base64,${imageData}`}))
          setImageData(images)
        }
          console.log(response.images)
        } catch (error) {
          console.error('Error fetching images: ', error)
        }  
    }
    listImages()

  }, [])

  


  return (
    <>
    <div>Bookcard</div>
      <div>
      {imageData && imageData.map((image, index) => (
        <img key={index} src={image.url} alt='Image' style={{width:'200px', height:'auto'}} />
      ))} 
      </div>
      
      {/* need to dynamically update alt with name of image, should be able to get that from db */}
      <h1>Story Headline</h1>
      <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Perferendis iure blanditiis facere mollitia sequi minima in commodi optio, perspiciatis ratione. Iure doloremque perferendis sint culpa aut nisi voluptas eum dolor.
      Nostrum suscipit, neque corrupti illum laudantium quos obcaecati iste magnam eligendi! Debitis, ipsum? Repellendus assumenda facilis, nostrum magnam neque reiciendis exercitationem! Dolorum nihil soluta quam ea facere ipsam fugiat ex.
      Cumque nemo excepturi qui molestias voluptatum aut alias molestiae vitae repellat doloribus labore exercitationem tenetur sapiente fugit, earum corrupti repellendus aperiam ea! Fuga sunt esse, asperiores natus doloribus exercitationem dolores.
      Culpa cupiditate fugit nesciunt vero ipsa debitis praesentium nulla magni, voluptatum voluptatem libero numquam assumenda pariatur vel error laboriosam non? Veniam cupiditate tempore ipsa distinctio commodi facilis maxime provident quasi.
      Consectetur deserunt voluptatum magnam amet tempore totam suscipit, quisquam distinctio molestiae voluptatibus ea magni quidem nostrum similique eum deleniti iusto! Cum maiores nam ea atque in iste qui necessitatibus dicta!</p>
    </>
  )
}

export default Bookcard
