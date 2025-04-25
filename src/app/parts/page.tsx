'use client';

import { useState } from 'react';
import axios from 'axios';

export default function PartsLookup() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const searchParts = async () => {
    if (!query) return;
    setLoading(true);
    setError(null);
    setResults([]);

    try {
      const response = await axios.post('http://localhost:8000/parts/lookup-description', {
        part_name: query,
        issue_context: 'Used in a repair where the technician noted vibration and heat.',
        priority: 'balanced',
      });

      const description = response.data.part_description;
      setResults([description]);
    } catch (err: any) {
      console.error('Error fetching part description:', err);
      setError('Failed to fetch description. Please make sure the backend is running and accessible.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-6 bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Parts Lookup</h1>

      <input
        type="text"
        placeholder="Enter part name (e.g. Bearing 6205Z)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="p-3 border border-gray-300 rounded-md w-full max-w-lg mb-4"
      />
      <button
        onClick={searchParts}
        disabled={loading}
        className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded disabled:opacity-50"
      >
        {loading ? 'Searching...' : 'Search Part'}
      </button>

      {error && (
        <div className="mt-4 text-red-600 font-medium">
          {error}
        </div>
      )}

      <div className="mt-6 space-y-4">
        {results.map((desc, index) => (
          <div key={index} className="bg-white rounded shadow p-4">
            <p className="text-gray-800">{desc}</p>
          </div>
        ))}
      </div>
    </main>
  );
}