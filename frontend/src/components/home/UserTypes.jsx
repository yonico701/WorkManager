import {Link} from "react-router-dom";

function UserTypes() {
  return (
    <section className="relative isolate px-6 pb-24 lg:px-8">
      <div className="mx-auto max-w-7xl">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-base font-semibold text-indigo-600">
            Choose your role
          </h2>

          <p className="mt-2 text-4xl font-semibold tracking-tight text-gray-900 sm:text-5xl">
            One platform, two ways to work
          </p>

          
        </div>

        <div className="mx-auto mt-16 grid max-w-5xl gap-8 md:grid-cols-2">
          <div className="rounded-3xl bg-white p-8 shadow-sm ring-1 ring-gray-900/10 transition duration-200 hover:-translate-y-1 hover:shadow-lg">
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-indigo-600 text-xl text-white">
              👤
            </div>

            <h3 className="mt-6 text-2xl font-semibold text-gray-900">
              Customer
            </h3>

            <p className="mt-4 text-sm leading-6 text-gray-600">
              Open a new job request, describe the service you need, and track
              the progress from start to finish.
            </p>

            <ul className="mt-6 space-y-3 text-sm text-gray-700">
              <li>✓ Create new job requests</li>
              <li>✓ Track job status</li>
              <li>✓ Manage your service history</li>
            </ul>

            <Link
              to = "/login"
              className="mt-8 inline-block rounded-md bg-indigo-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm transition duration-200 hover:bg-indigo-500"
            >
              Create Job
            </Link>
          </div>

          <div className="rounded-3xl bg-white p-8 shadow-sm ring-1 ring-gray-900/10 transition duration-200 hover:-translate-y-1 hover:shadow-lg">
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-indigo-600 text-xl text-white">
              🔧
            </div>

            <h3 className="mt-6 text-2xl font-semibold text-gray-900">
              Provider
            </h3>

            <p className="mt-4 text-sm leading-6 text-gray-600">
              Browse open jobs, join relevant requests, and update the work
              status while completing the job.
            </p>

            <ul className="mt-6 space-y-3 text-sm text-gray-700">
              <li>✓ View available jobs</li>
              <li>✓ Join open requests</li>
              <li>✓ Update job progress</li>
            </ul>

            <Link
              to = "/login"
              className="mt-8 inline-block rounded-md bg-indigo-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm transition duration-200 hover:bg-indigo-500"
            >
              View Open Jobs
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

export default UserTypes;