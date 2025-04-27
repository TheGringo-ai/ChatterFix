import axios from 'axios';

const backendUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const fetchWorkorders = async () => {
  const response = await axios.get(`${backendUrl}/workorders/all`);
  return response.data;
};

export const fetchAssets = async () => {
  const response = await axios.get(`${backendUrl}/assets/all`);
  return response.data;
};

export const fetchParts = async () => {
  const response = await axios.get(`${backendUrl}/parts/all`);
  return response.data;
};

export const fetchTechnicians = async () => {
  const response = await axios.get(`${backendUrl}/technicians/all`);
  return response.data;
};

export const fetchPms = async () => {
  const response = await axios.get(`${backendUrl}/pm/all`);
  return response.data;
};