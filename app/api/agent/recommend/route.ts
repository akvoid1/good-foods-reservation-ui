// Proxy to Python backend
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';

export async function POST(request: Request) {
  try {
    const body = await request.json();

    // Forward request to Python backend
    const response = await fetch(`${BACKEND_URL}/api/agent/recommend`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      throw new Error(`Backend error: ${response.statusText}`);
    }

    const data = await response.json();
    return Response.json(data);
  } catch (error) {
    console.error('Recommendation error:', error);
    return Response.json(
      { error: 'Failed to generate recommendations' },
      { status: 500 }
    );
  }
}
