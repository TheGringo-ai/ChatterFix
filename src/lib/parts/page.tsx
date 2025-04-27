'use client';

import { useEffect, useState } from 'react';
import { fetchTechnicians } from '@/lib/apiClient';

export default function TechniciansPage() {
  const [technicians, setTechnicians] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect((): any => {
    const loadTechnicians = async () => {
      try {
        const data = await fetchTechnicians();
        setTechnicians(data);
      } catch (err) {
        console.error('Failed to fetch technicians:', err);
        setError('Failed to load technicians.');
      } finally {
        setLoading(false);
      }
    }

    loadTechnicians();[]
  }, []);

  if (loading) return <div>Loading technicians...</div>;
  if (error) return <div className="text-red-600">{error}</div>;

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Technicians</h1>
      <ul className="space-y-4">
        {technicians.map((tech: any) => (
          <li key={tech.id} className="border p-4 rounded shadow">
            <h2 className="text-lg font-semibold">{tech.name}</h2>
            <p className="text-gray-700">Skills: {tech.skills?.join(', ')}</p>
            <p className="text-sm text-gray-500">Status: {tech.status}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
