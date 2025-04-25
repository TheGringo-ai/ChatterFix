'use client';

import { useEffect, useState } from 'react';
import axios from 'axios';

export default function PartsLookup() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const searchParts = async () => {
    if (!query) return;
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/parts/lookup-description', {
        part_name: query,
        issue_context: 'Used in a repair where the technician noted vibration and heat.',
        priority: 'balanced'
      });
      const description = response.data.part_description;
      setResults([description]);
    } catch (err) {
      console.error('Error fetching description:', err);
      setResults(['Failed to fetch description.']);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-4 bg-gray-50">
      <h1 className="text-3xl font-bold mb-4">Parts Lookup</h1>

      <input
        type="text"
        placeholder="Enter part name..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="p-2 border rounded w-full max-w-md mb-4"
      />
      <button
        onClick={searchParts}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
        disabled={loading}
      >
        {loading ? 'Searching...' : 'Search'}
      </button>

      <div className="mt-6">
        {results.map((desc, index) => (
          <div key={index} className="bg-white p-4 rounded shadow mt-2">
            <p>{desc}</p>
          </div>
        ))}
      </div>
    </main>
  );
}