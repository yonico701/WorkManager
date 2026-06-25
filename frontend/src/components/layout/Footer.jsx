import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faFacebook,
  faInstagram,
  faGithub,
  faLinkedin,
} from '@fortawesome/free-brands-svg-icons'

function Footer() {
  return (
    <footer className="bg-slate-950 text-slate-400">
      <div className="mx-auto max-w-7xl px-8 py-16">
        <div className="grid gap-12 md:grid-cols-4">
          <div>
            <h2 className="text-2xl font-bold text-indigo-400">
              WorkManager
            </h2>

            <p className="mt-6 max-w-xs text-sm leading-6">
              Manage jobs, customers, and service providers from one simple
              platform.
            </p>

            <div className="mt-8 flex gap-5 text-xl">
              <FontAwesomeIcon
                icon={faFacebook}
                className="cursor-pointer transition duration-200 hover:text-indigo-400"
              />

              <FontAwesomeIcon
                icon={faInstagram}
                className="cursor-pointer transition duration-200 hover:text-indigo-400"
              />

              <FontAwesomeIcon
                icon={faGithub}
                className="cursor-pointer transition duration-200 hover:text-indigo-400"
              />

              <FontAwesomeIcon
                icon={faLinkedin}
                className="cursor-pointer transition duration-200 hover:text-indigo-400"
              />
            </div>
          </div>

          <div>
            <h3 className="text-sm font-semibold text-white">
              Platform
            </h3>

            <ul className="mt-6 space-y-4 text-sm">
              <li className="transition duration-200 hover:text-indigo-400">Jobs</li>
              <li className="transition duration-200 hover:text-indigo-400">Customers</li>
              <li className="transition duration-200 hover:text-indigo-400">Providers</li>
              <li className="transition duration-200 hover:text-indigo-400">Dashboard</li>
            </ul>
          </div>

          <div>
            <h3 className="text-sm font-semibold text-white">
              Support
            </h3>

            <ul className="mt-6 space-y-4 text-sm">
              <li className="transition duration-200 hover:text-indigo-400">Help Center</li>
              <li className="transition duration-200 hover:text-indigo-400">Documentation</li>
              <li className="transition duration-200 hover:text-indigo-400">Contact</li>
              <li className="transition duration-200 hover:text-indigo-400">Guides</li>
            </ul>
          </div>

          <div>
            <h3 className="text-sm font-semibold text-white">
              Company
            </h3>

            <ul className="mt-6 space-y-4 text-sm">
              <li className="transition duration-200 hover:text-indigo-400">About</li>
              <li className="transition duration-200 hover:text-indigo-400">Gallery</li>
              <li className="transition duration-200 hover:text-indigo-400">Careers</li>
              <li className="transition duration-200 hover:text-indigo-400">Legal</li>
            </ul>
          </div>
        </div>

        <div className="mt-16 border-t border-slate-800 pt-8 text-sm text-slate-500">
          © 2026 WorkManager. All rights reserved.
        </div>
      </div>
    </footer>
  )
}

export default Footer