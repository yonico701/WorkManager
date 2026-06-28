import Hero from '../components/home/Hero'
import UserTypes from '../components/home/UserTypes'

function Home()  {
  return (
   <main className="relative overflow-hidden bg-white">
    <div className="absolute inset-0 bg-gradient-to-br from-pink-100 via-purple-100 to-white" />
        <div className="relative z-10">
          <Hero />
          <UserTypes />
        </div>
    </main>
  )
}

export default Home


