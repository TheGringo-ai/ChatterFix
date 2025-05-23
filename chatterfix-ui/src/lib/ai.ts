export async function getAIResponse(prompt: string) {
  const res = await fetch('/api/ai/assist', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });

  if (!res.ok) {
    throw new Error('Failed to fetch AI response');
  }

  const data = await res.json();

  if (data.error) {
    throw new Error(data.error || 'Unknown AI error');
  }

  return {
    result: data.result,
    model: data.engine,
  };
}