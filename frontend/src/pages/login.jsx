import LoginForm from '../components/auth/LoginForm'

function Login() {
  return (
    <main className="relative min-h-screen overflow-hidden px-6 py-20">
      <div className="absolute inset-0 bg-gradient-to-br from-pink-50 via-purple-100 to-white" />

      <div className="relative z-10">
        <LoginForm />
      </div>
    </main>
  )
}

export default Login