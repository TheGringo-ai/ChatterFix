'use client';

import { useState } from 'react';

export default function AIPage() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch('/api/ai/assist', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: input }),
      });

      if (!res.ok) {
        throw new Error('Failed to fetch AI response');
      }

      const data = await res.json();
      setResponse(data.result);
    } catch (error) {
      setResponse('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">AI Assistant</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask the assistant about your work orders, parts, or PMs..."
          className="w-full p-3 border border-gray-300 rounded-md shadow-sm"
          rows={5}
        />
        <button
          type="submit"
          disabled={loading || !input.trim()}
          className="bg-blue-600 text-white px-5 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? 'Thinking...' : 'Ask AI'}
        </button>
      </form>
      {response && (
        <div className="bg-white p-4 rounded shadow border border-gray-200">
          <h2 className="text-lg font-semibold mb-2">Response</h2>
          <p className="whitespace-pre-wrap text-gray-800">{response}</p>
        </div>
      )}
    </div>
  );
}
