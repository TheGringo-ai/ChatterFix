

'use client';

export default function PMPage() {
  return (
    <div className="p-6 space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">Preventive Maintenance</h1>
        <p className="text-gray-600">Manage all scheduled maintenance tasks across your equipment and assets.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Upcoming PMs</h2>
          <p className="text-gray-700 mb-4">View and schedule upcoming preventive maintenance tasks.</p>
          <a href="/dashboard/pm/upcoming" className="text-blue-600 hover:underline">View Upcoming →</a>
        </div>

        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Completed PMs</h2>
          <p className="text-gray-700 mb-4">Review completed PM work and technician records.</p>
          <a href="/dashboard/pm/completed" className="text-blue-600 hover:underline">View Completed →</a>
        </div>

        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">PM Templates</h2>
          <p className="text-gray-700 mb-4">Manage reusable PM task templates by asset or category.</p>
          <a href="/dashboard/pm/templates" className="text-blue-600 hover:underline">Manage Templates →</a>
        </div>
      </div>
    </div>
  );
}