

'use client';

export default function AssetsPage() {
  return (
    <div className="p-6 space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">Asset Management</h1>
        <p className="text-gray-600">Track, organize, and manage your facility’s assets and equipment.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">All Assets</h2>
          <p className="text-gray-700 mb-4">Browse your complete asset register by location, type, or status.</p>
          <a href="/dashboard/assets/list" className="text-blue-600 hover:underline">View Assets →</a>
        </div>

        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Asset Categories</h2>
          <p className="text-gray-700 mb-4">Group assets into categories for better tracking and reporting.</p>
          <a href="/dashboard/assets/categories" className="text-blue-600 hover:underline">Manage Categories →</a>
        </div>

        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Maintenance History</h2>
          <p className="text-gray-700 mb-4">Review all maintenance and repair logs per asset.</p>
          <a href="/dashboard/assets/history" className="text-blue-600 hover:underline">View History →</a>
        </div>
      </div>
    </div>
  );
}