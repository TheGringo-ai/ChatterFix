'use client';

import { useEffect, useState } from 'react';

type WorkOrder = {
  id: string;
  title: string;
  description: string;
};

export default function WorkOrdersPage() {
  const [workOrders, setWorkOrders] = useState<WorkOrder[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchWorkOrders() {
      try {
        const res = await fetch('/api/workorders');
        const data: WorkOrder[] = await res.json();
        setWorkOrders(data);
      } catch (error) {
        console.error('Error fetching work orders:', error);
      } finally {
        setLoading(false);
      }
    }

    fetchWorkOrders();
  }, []);

  if (loading) return <div className="p-4">Loading work orders...</div>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Work Orders</h1>
      <ul className="space-y-4">
        {workOrders.map((order) => (
          <li key={order.id} className="p-4 bg-white rounded shadow">
            <h2 className="text-lg font-bold">{order.title}</h2>
            <p className="text-sm text-gray-600">{order.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
