export const dynamic = 'force-static';
import React from 'react';

export default function Home() {
  return (
    <>
      <header style={headerStyle}>
        <img
          src="/chatterfix-logo.png"
          alt="ChatterFix Logo"
          style={{ height: '48px' }}
        />
        <h1 style={{ marginLeft: '1rem', fontSize: '1.75rem', color: '#fff' }}>
          ChatterFix
        </h1>
      </header>

      <main style={mainStyle}>
        <h2 style={{ fontSize: '2rem', marginBottom: '1rem' }}>
          The AI-powered CMMS built for technicians.
        </h2>
        <p style={{ fontSize: '1.1rem', color: '#444', marginBottom: '2rem' }}>
          Voice-to-work order. OCR. Offline-ready. Lightning fast. Technician-first.
        </p>

        <div style={ctaContainer}>
          <a href="/dashboard/workorders" style={btnStyle}>
            🚧 View Work Orders
          </a>
          <a href="/request_work_order" style={btnStyle}>
            📋 Submit Request
          </a>
          <a href="/tour" style={btnStyle}>
            🧭 Product Tour
          </a>
        </div>
      </main>

      <footer style={footerStyle}>
        Built by Fred Taylor · Firebase Hosted · GPT Powered · v1.0.0
      </footer>
    </>
  );
}

const headerStyle: React.CSSProperties = {
  position: 'sticky',
  top: 0,
  backgroundColor: '#0d1117',
  display: 'flex',
  alignItems: 'center',
  padding: '1rem 2rem',
  boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
  zIndex: 999,
};

const mainStyle: React.CSSProperties = {
  padding: '3rem 1rem',
  maxWidth: '800px',
  margin: '0 auto',
  textAlign: 'center',
  fontFamily: 'Arial, sans-serif',
};

const ctaContainer: React.CSSProperties = {
  display: 'flex',
  flexDirection: 'column',
  gap: '1rem',
  alignItems: 'center',
};

const btnStyle: React.CSSProperties = {
  backgroundColor: '#0070f3',
  color: '#fff',
  padding: '0.8rem 1.6rem',
  borderRadius: '8px',
  textDecoration: 'none',
  fontWeight: 'bold',
  fontSize: '1rem',
  transition: 'all 0.2s',
};

const footerStyle: React.CSSProperties = {
  textAlign: 'center',
  padding: '2rem 0',
  fontSize: '0.85rem',
  color: '#666',
  borderTop: '1px solid #eee',
};
