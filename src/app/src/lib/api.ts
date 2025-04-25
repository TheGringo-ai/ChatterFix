// src/lib/api.ts
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export const getWorkOrders = async () => {
  const response = await axios.get(`${API_BASE_URL}/workorders`);
  return response.data;
};

export const getPMs = async () => {
  const response = await axios.get(`${API_BASE_URL}/pm`);
  return response.data;
};

export const getAssets = async () => {
  const response = await axios.get(`${API_BASE_URL}/assets`);
  return response.data;
};

export const summarizeNotes = async (notes: string) => {
  const response = await axios.post(`${API_BASE_URL}/ai/summarize`, {
    notes,
  });
  return response.data;
};