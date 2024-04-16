import React from 'react'
import { Link } from 'react-router-dom'
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

// change layout to column with image after word Story Line and before paragraph  at breakpoint: 850px
const NavBar = () => {

  // make logout function only showing when user is logged in, else it's not there in navbar

  return (
    <>
      <Container className='nav justify-content-center fw-bold fs-4'>
          <Navbar.Brand href="/"><img src='/books-book-svgrepo-com.svg' alt='Story Line logo' width='50' className="d-inline-block align-mid p-1"/></Navbar.Brand>
        <Link to="/" className='nav-link'>Home</Link>
        <Link to="/storyline" className='nav-link'>Storyline</Link>
        <Link to="/stories" className='nav-link'> My Stories</Link>
        <Link to="/favorites" className='nav-link'>Favorites</Link>
      </Container>
    </>
  )
}

export default NavBar