'use client';

import Link from 'next/link';

export default function DashboardPage() {
  return (
    <main className="p-6 space-y-6">
      <header>
        <h1 className="text-3xl font-bold">ChatterFix Dashboard</h1>
        <p className="text-gray-700 text-lg">Select a tool below to continue:</p>
      </header>
      <nav>
        <ul className="list-disc list-inside space-y-2 text-blue-600">
          <li><Link href="/dashboard/ai">AI Assistant</Link></li>
          <li><Link href="/dashboard/deploy">Deploy Console</Link></li>
          <li><Link href="/dashboard/console">AI Console</Link></li>
          <li><Link href="/dashboard/assets">Assets</Link></li>
          <li><Link href="/dashboard/parts">Parts</Link></li>
          <li><Link href="/dashboard/pm">PM Schedule</Link></li>
        </ul>
      </nav>
    </main>
  );
}