"use client";

import { useState } from "react";
import axios from "axios";

export default function AIAssistPage() {
  const [input, setInput] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:8000/ai/summarize", {
        notes: input,
      });
      setSummary(response.data.summary);
    } catch (err) {
      setSummary("Error summarizing notes.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6">AI Assistant</h1>
      <form onSubmit={handleSubmit} className="mb-6">
        <textarea
          className="w-full p-3 rounded shadow border border-gray-300"
          rows={6}
          placeholder="Paste technician notes here..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        ></textarea>
        <button
          type="submit"
          className="mt-4 px-4 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700"
        >
          Summarize Notes
        </button>
      </form>
      {loading && <p>Summarizing...</p>}
      {summary && (
        <div className="bg-white p-4 rounded shadow">
          <h2 className="font-semibold text-lg mb-2">AI Summary:</h2>
          <p className="text-gray-800 whitespace-pre-wrap">{summary}</p>
        </div>
      )}
    </main>
  );
}