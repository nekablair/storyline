import React from 'react'
import { login } from "../utilities";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

const Signup = () => {

  const submitForm = async (e) => {
    e.preventDefault()
    // console.log("submitted form")
    let response = await login(email, password, register)
    setUser(response)
  }

  return (
    <>
    <div>Signup</div>
    <Form onSubmit={(e)=>{submitForm(e)}}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="Enter email" />
          <Form.Text className="text-muted">
            We'll never share your email with anyone else.
          </Form.Text>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="Password" />
        </Form.Group>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </>
  )
}

export default Signup