'use client';
import { useState, useEffect } from 'react';
import { fetchPms } from '../apiClient';
type PM = {
  id: string;
  title: string;
  frequency_days: number;
  asset_id: string;
  description?: string;
};


export default function PMsPage() {
  const [pms, setPms] = useState<PM[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    const loadPMs = async () => {
      try {
        const data = await fetchPms();
        setPms(data);
      } catch (err) {
        console.error('Faile          d to fetch PMs:', err);
        setError('Failed to load PMs.');
      } finally {
        setLoading(false);
      }
    };

    loadPMs();
  }, []);

  if (loading) {
    return <div>Loading PMs...</div>;
  }

  if (error) {
    return <div className="text-red-600">{error}</div>;
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Preventive Maintenance (PM)</h1>
      <ul className="space-y-4">
        {pms.map((pm) => (
          <li key={pm.id} className="border p-4 rounded shadow">
            <h2 className="text-lg font-semibold">{pm.title}</h2>
            <p className="text-gray-700">Frequency: every {pm.frequency_days} days</p>
            <p className="text-sm text-gray-500">Asset ID: {pm.asset_id}</p>
            {pm.description && (
              <p className="text-sm text-gray-600 mt-2">{pm.description}</p>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
