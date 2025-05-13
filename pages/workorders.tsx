
import { useEffect, useState } from 'react'
import axios from 'axios'

export default function WorkOrdersPage() {
  const [workOrders, setWorkOrders] = useState([])
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    fetchWorkOrders()
  }, [])

  const fetchWorkOrders = async () => {
    try {
      const res = await axios.get('http://localhost:8000/workorders')
      setWorkOrders(res.data)
    } catch (err) {
      console.error('Failed to fetch work orders:', err)
    }
  }

  const createWorkOrder = async () => {
    setLoading(true)
    try {
      await axios.post('http://localhost:8000/workorders', {
        title,
        description,
      })
      setTitle('')
      setDescription('')
      fetchWorkOrders()
    } catch (err) {
      console.error('Failed to create work order:', err)
    }
    setLoading(false)
  }

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Work Orders</h1>

      <div className="mb-6">
        <input
          className="block w-full border p-2 mb-2"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          className="block w-full border p-2 mb-2"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
          onClick={createWorkOrder}
          disabled={loading || !title || !description}
        >
          {loading ? 'Creating...' : 'Create Work Order'}
        </button>
      </div>

      <ul className="space-y-4">
        {workOrders.map((order) => (
          <li key={order.id} className="p-4 bg-white rounded shadow">
            <h2 className="font-bold text-lg">{order.title}</h2>
            <p className="text-sm text-gray-600">{order.description}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

