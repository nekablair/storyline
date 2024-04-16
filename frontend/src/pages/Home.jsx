import React from 'react'
import { useOutletContext, Link } from 'react-router-dom'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const Home = () => {

  

  return (
    <>
      <Container className='fluid p-5' >
        <Row className='align-items-center'> 
          <Col className='text-center'>
            <h2 className='display-1'>Story Line</h2>
            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Suscipit repellat deleniti, recusandae ullam officiis iste distinctio, consequatur quaerat autem aut in? Illum, reiciendis. Commodi doloremque architecto fugit alias enim soluta.
            Omnis qui iusto excepturi dicta eos architecto dolorem non similique laborum repellendus. Repudiandae dolore mollitia fugit, eveniet, exercitationem, dolorem libero ipsa nesciunt temporibus sint aperiam id dolorum explicabo tempora consequatur!</p>
            <div className='p-2 d-flex justify-content-evenly'>
            <Link to="/signup"><Button variant="warning">Sign Up</Button></Link>
            <Link to="/login"><Button variant="warning">Login</Button></Link>
            </div>
          </Col>
          <Col>
            <Card className="bg-dark text-white">
            <Card.Img src='/img-l4x9O42aFOfwn36o3pOcJwKi-child-creating-story.png' alt='child reading' className="img-fluid rounded mx-auto d-block" />
            <Card.ImgOverlay>
            {/* <Card.Title className=''>Make Your Imagination Come to Life</Card.Title> */}
            </Card.ImgOverlay>
            </Card>
          </Col>
        </Row>  
      </Container>
    </>
  )
}

export default Home
