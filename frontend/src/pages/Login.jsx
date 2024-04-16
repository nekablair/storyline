import React, { useEffect, useState } from 'react'
import { useOutletContext, useNavigate } from 'react-router-dom'
import { login } from "../utilities";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

const Login = () => {
  const [register, setRegister] = useState(false);
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const {setUser, user} = useOutletContext()
  const navigate = useNavigate()

  const submitForm = async (e) => {
    e.preventDefault()
    let response = await login(email, password, register)
    setUser(response)
  }

  useEffect(() => {
    if (user) {
      navigate('/')
    }
  }, [user])


  return (
    <>
      {/* <div>Login</div> */}
      <h1>
        {/* {register ? "Register" : "Login" } */}
        Login
      </h1>
      <Form onSubmit={(e)=>{submitForm(e)}}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="Enter email" value={email} onChange={(e) => setEmail(e.target.value)} />
          <Form.Text className="text-muted">
            We'll never share your email with anyone else.
          </Form.Text>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </Form.Group>
        <Button variant="warning" type="submit" onClick={() => setRegister(!register)}>
        {/* {register ? "Already have an account": "Don't have an account?"} */}
        Login
        </Button>
      </Form>
    </>
  )
}

export default Login