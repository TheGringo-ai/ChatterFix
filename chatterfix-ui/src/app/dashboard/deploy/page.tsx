'use client';

import { useState } from 'react';

export default function DeployPage() {
  const [status, setStatus] = useState<'idle' | 'deploying' | 'success' | 'error'>('idle');

  const triggerDeploy = async () => {
    setStatus('deploying');
    try {
      const res = await fetch('/api/deploy-webhook', { method: 'POST' });
      if (!res.ok) throw new Error();
      setStatus('success');
    } catch {
      setStatus('error');
    }
  };

  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">Deploy Backend</h1>
      <p className="text-gray-700">This triggers your GitHub Actions deploy workflow.</p>
      <button
        onClick={triggerDeploy}
        className="bg-green-600 text-white px-5 py-2 rounded hover:bg-green-700 disabled:opacity-50"
        disabled={status === 'deploying'}
      >
        {status === 'deploying' ? 'Deploying...' : 'Trigger Deploy'}
      </button>
      {status === 'success' && <p className="text-green-600">Deploy triggered successfully.</p>}
      {status === 'error' && <p className="text-red-600">Failed to trigger deploy.</p>}
    </div>
  );
}
