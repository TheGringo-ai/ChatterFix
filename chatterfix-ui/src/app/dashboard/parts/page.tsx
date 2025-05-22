'use client';

export default function DashboardPage() {
  return (
    <div className="p-6 space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">ChatterFix Dashboard</h1>
        <p className="text-gray-600">Welcome to your maintenance control center.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Work Orders</h2>
          <p className="text-gray-700 mb-4">View and manage active and completed work orders.</p>
          <a href="/dashboard/workorders" className="text-blue-600 hover:underline">Go to Work Orders →</a>
        </div>

        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">Parts Inventory</h2>
          <p className="text-gray-700 mb-4">Browse and manage parts available for repairs and PMs.</p>
          <a href="/dashboard/parts" className="text-blue-600 hover:underline">View Parts →</a>
        </div>

        <div className="bg-white shadow-md rounded-lg p-5 hover:shadow-lg transition">
          <h2 className="text-xl font-semibold mb-2">AI Assistant</h2>
          <p className="text-gray-700 mb-4">Get help troubleshooting or summarizing maintenance data.</p>
          <a href="/dashboard/ai" className="text-blue-600 hover:underline">Ask the Assistant →</a>
        </div>
      </div>
    </div>
  );
}