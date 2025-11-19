// Proxy to Python backend
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const sessionId = searchParams.get('session_id') || 'default_session';

    // Forward request to Python backend
    const response = await fetch(`${BACKEND_URL}/api/reservations?session_id=${sessionId}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`Backend error: ${response.statusText}`);
    }

    const data = await response.json();
    return Response.json(data);
  } catch (error) {
    console.error('Reservations list error:', error);
    return Response.json(
      { error: 'Failed to fetch reservations' },
      { status: 500 }
    );
  }
}
