import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
};

export default nextConfig;
export interface Technician {
  id: string;
  name: string;
  skills: string[];
  status: string;
}
