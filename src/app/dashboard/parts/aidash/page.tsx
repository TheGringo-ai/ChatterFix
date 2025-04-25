'use client';

import { useState } from 'react';
import axios from 'axios';

export default function AiDashboard() {
  const [mode, setMode] = useState<'generate' | 'improve' | 'analyze' | 'summarize'>('generate');
  const [task, setTask] = useState('');
  const [context, setContext] = useState('');
  const [filename, setFilename] = useState('App/generated/ai_code.py');
  const [existingCode, setExistingCode] = useState('');
  const [goal, setGoal] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const apiMap = {
    generate: 'generate-code',
    improve: 'improve-code',
    analyze: 'analyze-code',
    summarize: 'summarize'
  };

  const runAction = async () => {
    setLoading(true);
    setResult('');
    setError('');
    try {
      const payload: any = {};
      if (mode === 'generate') {
        payload.task = task;
        payload.context = context;
        payload.filename = filename;
      } else if (mode === 'improve') {
        payload.existing_code = existingCode;
        payload.goal = goal;
        payload.filename = filename;
      } else if (mode === 'analyze') {
        payload.code = existingCode;
      } else if (mode === 'summarize') {
        payload.notes = context;
      }

      const response = await axios.post(`http://localhost:8000/ai/${apiMap[mode]}`, payload);
      const key = mode === 'generate' ? 'code' : mode === 'improve' ? 'improved_code' : mode === 'analyze' ? 'analysis' : 'summary';
      setResult(response.data[key]);
    } catch (err: any) {
      console.error(err);
      setError(err.response?.data?.detail || 'Unexpected error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-6 bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">AI Assistant</h1>

      <div className="mb-4 space-x-2">
        {(['generate', 'improve', 'analyze', 'summarize'] as const).map((m) => (
          <button
            key={m}
            onClick={() => setMode(m)}
            className={`px-4 py-2 rounded ${mode === m ? 'bg-blue-700 text-white' : 'bg-gray-300'}`}
          >
            {m.charAt(0).toUpperCase() + m.slice(1)}
          </button>
        ))}
      </div>

      {mode === 'generate' && (
        <>
          <input
            className="block w-full max-w-xl p-2 mb-2 border rounded"
            placeholder="Describe the task..."
            value={task}
            onChange={(e) => setTask(e.target.value)}
          />
          <textarea
            className="block w-full max-w-xl p-2 mb-2 border rounded"
            placeholder="Context or examples..."
            value={context}
            onChange={(e) => setContext(e.target.value)}
            rows={4}
          />
          <input
            className="block w-full max-w-xl p-2 mb-4 border rounded"
            placeholder="Save to file (e.g. App/generated/code.py)"
            value={filename}
            onChange={(e) => setFilename(e.target.value)}
          />
        </>
      )}

      {mode === 'improve' && (
        <>
          <textarea
            className="block w-full max-w-xl p-2 mb-2 border rounded"
            placeholder="Paste existing code here..."
            value={existingCode}
            onChange={(e) => setExistingCode(e.target.value)}
            rows={6}
          />
          <input
            className="block w-full max-w-xl p-2 mb-2 border rounded"
            placeholder="What should be improved?"
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
          />
          <input
            className="block w-full max-w-xl p-2 mb-4 border rounded"
            placeholder="Save to file (e.g. App/generated/improved_code.py)"
            value={filename}
            onChange={(e) => setFilename(e.target.value)}
          />
        </>
      )}

      {mode === 'analyze' && (
        <textarea
          className="block w-full max-w-xl p-2 mb-4 border rounded"
          placeholder="Paste code for analysis..."
          value={existingCode}
          onChange={(e) => setExistingCode(e.target.value)}
          rows={6}
        />
      )}

      {mode === 'summarize' && (
        <textarea
          className="block w-full max-w-xl p-2 mb-4 border rounded"
          placeholder="Paste technician notes here..."
          value={context}
          onChange={(e) => setContext(e.target.value)}
          rows={6}
        />
      )}

      <button
        onClick={runAction}
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? 'Working...' : `Run ${mode}`}
      </button>

      {error && <div className="text-red-600 mt-4">{error}</div>}
      {result && (
        <pre className="bg-white border mt-4 p-4 rounded shadow w-full max-w-xl overflow-auto">
          {result}
        </pre>
      )}
    </main>
  );
}
