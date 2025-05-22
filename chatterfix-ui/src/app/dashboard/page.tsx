'use client';

import { useEffect, useState } from 'react';
import { fetchAssets } from '@/lib/apiClient';

export default function AssetsPage() {
  const [assets, setAssets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const loadAssets = async () => {
      try {
        const data = await fetchAssets();
        setAssets(data);
      } catch (err: any) {
        console.error('Failed to fetch assets:', err);
        setError('Failed to load assets.');
      } finally {
        setLoading(false);
      }
    };

    loadAssets();
  }, []);

  if (loading) return <div>Loading assets...</div>;
  if (error) return <div className="text-red-600">{error}</div>;

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Assets</h1>
      <ul className="space-y-4">
        {assets.map((asset: any) => (
          <li key={asset.id} className="border p-4 rounded shadow">
            <h2 className="text-lg font-semibold">{asset.name}</h2>
            <p className="text-gray-700">Location: {asset.location}</p>
            <p className="text-sm text-gray-500">Status: {asset.status}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}