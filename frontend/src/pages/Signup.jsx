import React, { useEffect, useState } from 'react'
import { signup } from "../utilities";
import { useOutletContext, useNavigate } from 'react-router-dom'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

const Signup = () => {
  const [register, setRegister] = useState(false);
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const {setUser, user} = useOutletContext()
  const navigate = useNavigate()

  const submitForm = async (e) => {
    e.preventDefault()
    // console.log("submitted form")
    // const email = e.target.elements.email.value;
    // const password = e.target.elements.password.value;
    let response = await signup(email, password, register)
    setUser(response)
  }

  useEffect(() => {
    if (user) {
      navigate('/')
    }
  }, [user])

  return (
    <>
    <div>Signup</div>
    <h1>{register ? "Register" : "Login" }</h1>
    <Form onSubmit={(e)=>{submitForm(e)}}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="Enter email" name="email" value={email} onChange={(e) => setEmail(e.target.value)} />
          <Form.Text className="text-muted">
            We'll never share your email with anyone else.
          </Form.Text>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="Password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
        </Form.Group>
        <Button variant="primary" type="submit" onClick={() => setRegister(!register)}>
          {register ? "Already have an account": "Don't have an account?"}
        </Button>
      </Form>
    </>
  )
}

export default Signup