import Header from './components/layout/Header'
import Hero from './components/home/Hero'
import UserTypes from './components/home/UserTypes'
import Footer from './components/layout/Footer'

function App() {
  return (
    <div className="min-h-screen bg-white">
      <Header />

      <main className="relative overflow-hidden bg-white">
        <div className="absolute inset-0 bg-gradient-to-br from-pink-100/60 via-purple-100/50 to-white" />

        <div className="relative z-10">
          <Hero />
          <UserTypes />
        </div>
      </main>

      <Footer />
    </div>
  )
}

export default App