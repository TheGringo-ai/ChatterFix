'use client';

export default function PartsPage() {
  return (
    <div className="p-6 space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">Parts Dashboard</h1>
        <p className="text-gray-600">Welcome to your parts management center.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Search Parts</h2>
          <p className="text-gray-700 mb-4">Look up parts by number, name, or linked asset.</p>
          <a href="/dashboard/parts/search" className="text-blue-600 hover:underline">Search Parts →</a>
        </div>

        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Part Usage</h2>
          <p className="text-gray-700 mb-4">Track how parts are used across work orders and PMs.</p>
          <a href="/dashboard/parts/usage" className="text-blue-600 hover:underline">View Usage →</a>
        </div>

        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Vendors & Orders</h2>
          <p className="text-gray-700 mb-4">Manage part vendors and track open orders.</p>
          <a href="/dashboard/parts/vendors" className="text-blue-600 hover:underline">Manage Vendors →</a>
        </div>
      </div>
    </div>
  );
}