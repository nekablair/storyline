import React from 'react'
import { useOutletContext, Link } from 'react-router-dom'
import Button from 'react-bootstrap/Button';

const Notfoundpage = () => {
  return (
    <>
      <div>Notfoundpage</div>
      {/* you'll need to remove the navbar and footer from this 404 not found page so they can only click the home button */}
      <p>Oops, looks like your story isn't here! Click the button to go back to the home page.</p>
      <Button variant='warning'>
        <Link to="/" className='nav-link '>Home</Link>
      </Button>
    </>
  )
}

export default Notfoundpage
