"use client";

import { useEffect, useState } from "react";
import axios from "axios";

interface PMTask {
  id: string;
  task: string;
  due_date: string;
  asset: string;
  frequency: string;
}

export default function PMPage() {
  const [pmTasks, setPmTasks] = useState<PMTask[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchPMs = async () => {
      try {
        const response = await axios.get("http://localhost:8000/pm");
        setPmTasks(response.data);
      } catch (err) {
        setError("Failed to load PM tasks");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchPMs();
  }, []);

  return (
    <main className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6">Preventive Maintenance</h1>

      {loading && <p>Loading PM tasks...</p>}
      {error && <p className="text-red-600">{error}</p>}

      {!loading && !error && (
        <ul className="space-y-4">
          {pmTasks.map((task) => (
            <li key={task.id} className="bg-white shadow p-4 rounded">
              <h2 className="text-xl font-semibold">{task.task}</h2>
              <p className="text-sm text-gray-600">Asset: {task.asset}</p>
              <p className="text-sm text-gray-600">
                Due: {new Date(task.due_date).toLocaleString()} | Frequency: {task.frequency}
              </p>
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}