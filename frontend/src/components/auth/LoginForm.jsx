import { Link } from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHammer } from '@fortawesome/free-solid-svg-icons'

function LoginForm() {
  return (
    <section className="mx-auto max-w-md rounded-3xl border border-gray-200 bg-white p-10 shadow-xl">
      <div className="flex justify-center text-2xl font-bold text-indigo-600">
        WorkManager <FontAwesomeIcon icon={faHammer} />
      </div>

      <p className="mt-10 text-center text-base leading-7 text-gray-600">
        Sign in to your account
      </p>

      <form className="mt-8 space-y-5">
        <div>
          <label
            htmlFor="email"
            className="block text-sm font-semibold text-gray-700"
          >
            Email address
          </label>

          <input
            id="email"
            name="email"
            type="email"
            autoComplete="email"
            className="mt-2 block w-full rounded-md border border-gray-300 px-4 py-2.5 text-sm outline-none focus:border-indigo-600"
          />
        </div>

        <div>
          <label
            htmlFor="password"
            className="block text-sm font-semibold text-gray-700"
          >
            Password
          </label>

          <input
            id="password"
            name="password"
            type="password"
            autoComplete="current-password"
            className="mt-2 block w-full rounded-md border border-gray-300 px-4 py-2.5 text-sm outline-none focus:border-indigo-600"
          />
        </div>

        <button
          type="button"
          className="mt-4 w-full rounded-md bg-indigo-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition duration-200 hover:bg-indigo-500"
        >
          Login
        </button>
      </form>

      <p className="mt-8 text-center text-sm text-gray-600">
        Don't have an account?{' '}
        <Link
          to="/register"
          className="font-semibold text-indigo-600 hover:text-indigo-500"
        >
          Register
        </Link>
      </p>
    </section>
  )
}

export default LoginForm