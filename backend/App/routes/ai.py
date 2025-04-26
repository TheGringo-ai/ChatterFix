'use client';

import { useEffect, useState } from 'react';
import axios from 'axios';

export default function DailyPMTasks() {
  const [tasks, setTasks] = useState<any[]>([]);
  const [date, setDate] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/generated/daily-pm-tasks')
      .then(res => {
        setTasks(res.data.tasks || []);
        setDate(res.data.date || '');
      })
      .catch(err => {
        console.error('Failed to fetch daily PM tasks:', err);
      });
  }, []);

  return (
    <main className="min-h-screen p-4 bg-gray-50">
      <h1 className="text-2xl font-bold mb-4">PM Tasks for {date}</h1>
      {tasks.length > 0 ? (
        <ul className="space-y-4">
          {tasks.map((task, index) => (
            <li key={index} className="bg-white rounded p-4 shadow">
              <p><strong>Task:</strong> {task.task}</p>
              <p><strong>Asset:</strong> {task.asset}</p>
              <p><strong>Due Time:</strong> {task.due_time}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No PM tasks found for today.</p>
      )}
    </main>
  );
}
