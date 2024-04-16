import React from 'react'
import { Link } from 'react-router-dom'
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';

const Footer = () => {
  return (
    <>
      <div className='text-center pt-4'>
      <Container className='nav justify-content-center fw-bold'>
        <Link to="/" className='nav-link'>Home</Link>
        <Link to="/storyline" className='nav-link'>Storyline</Link>
        <Link to="/stories" className='nav-link'> My Stories</Link>
        <Link to="/favorites" className='nav-link'>Favorites</Link>
      </Container>
      <p className='pt-4'>&copy; Story Line: Made with ❤️ Neka Blair 2024</p>
      </div>
    </>
  )
}

export default Footer