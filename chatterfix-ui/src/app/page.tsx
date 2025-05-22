'use client';

import Link from 'next/link';

export default function HomePage() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">Welcome to ChatterFix</h1>
      <p className="text-gray-700 text-lg">
        Your AI-powered CMMS platform for smarter maintenance management.
      </p>
      <div>
        <Link
          href="/dashboard"
          className="inline-block bg-blue-600 text-white px-5 py-2 rounded hover:bg-blue-700"
        >
          Go to Dashboard
        </Link>
      </div>
    </div>
  );
}