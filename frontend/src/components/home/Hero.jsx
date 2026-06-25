function Hero() {
  return (
    <section className=" min-h-[60vh] relative overflow-hidden">
      <main className="relative isolate px-6 pt-14 lg:px-8">
        <div className="mx-auto max-w-2xl py-32 text-center sm:py-48 lg:py-24">
          <div className="hidden sm:mb-8 sm:flex sm:justify-center">
            <p className="rounded-full px-3 py-1 text-sm text-gray-600 ring-1 ring-gray-900/10">
              Modern platform for managing service requests
            </p>
          </div>

          <h1 className="text-5xl font-semibold tracking-tight text-gray-900 sm:text-7xl">
            Manage your work in one place
          </h1>

          <p className="mt-8 text-lg font-medium text-gray-500 sm:text-xl/8">
            Create jobs, manage customers, assign service providers, and track
            every task from one simple platform.
          </p>
        </div>
      </main>
    </section>
  );
}

export default Hero;