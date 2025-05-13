'use client';

import { useEffect, useState } from 'react';

// Define the shape of each work order
type WorkOrder = {
  id: string;
  title: string;
  description: string;
};

export default function WorkOrdersPage() {
  const [workOrders, setWorkOrders] = useState<WorkOrder[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchWorkOrders() {
      try {
        const res = await fetch('/api/workorders');
        if (!res.ok) throw new Error('Failed to fetch work orders');
        const data: WorkOrder[] = await res.json();
        setWorkOrders(data);
      } catch (err) {
        setError((err as Error).message);
      } finally {
        setLoading(false);
      }
    }

    fetchWorkOrders();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Work Orders</h1>

      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">Error: {error}</p>}

      {!loading && !error && (
        <ul className="space-y-4">
          {workOrders.map((order) => (
            <li key={order.id} className="p-4 bg-white rounded shadow">
              <h2 className="font-bold text-lg">{order.title}</h2>
              <p className="text-sm text-gray-600">{order.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
