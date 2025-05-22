import './globals.css';

export const metadata = {
  title: 'ChatterFix',
  description: 'AI-powered CMMS dashboard',
};

export default function Layout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head />
      <body className="bg-gray-100 text-black antialiased min-h-screen">
        <div className="max-w-screen-2xl mx-auto">{children}</div>
      </body>
    </html>
  );
}
