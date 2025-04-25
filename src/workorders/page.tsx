"use client";

import { useEffect, useState } from "react";
import axios from "axios";

interface WorkOrder {
  id: string;
  asset: string;
  status: string;
  priority: string;
  scheduled_date: string;
  technician: string;
  description: string;
}

export default function DashboardPage() {
  const [workOrders, setWorkOrders] = useState<WorkOrder[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchWorkOrders = async () => {
      try {
        const response = await axios.get("http://localhost:8000/workorders");
        setWorkOrders(response.data);
      } catch (err) {
        setError("Failed to load work orders");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchWorkOrders();
  }, []);

  return (
    <main className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6">Technician Dashboard</h1>

      {loading && <p className="text-gray-600">Loading work orders...</p>}
      {error && <p className="text-red-600">{error}</p>}

      {!loading && !error && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {workOrders.map((order) => (
            <div
              key={order.id}
              className="bg-white rounded-xl shadow p-4 border border-gray-200"
            >
              <h2 className="text-lg font-semibold mb-2">{order.asset}</h2>
              <p className="text-sm text-gray-500">Status: {order.status}</p>
              <p className="text-sm text-gray-500">Priority: {order.priority}</p>
              <p className="text-sm text-gray-500">
                Scheduled: {new Date(order.scheduled_date).toLocaleString()}
              </p>
              <p className="text-sm text-gray-500">Tech: {order.technician}</p>
              <p className="text-sm mt-2 text-gray-700">{order.description}</p>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}