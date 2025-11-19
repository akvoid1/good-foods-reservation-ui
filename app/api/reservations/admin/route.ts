// Proxy to Python backend - Admin endpoint
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';

export async function GET(request: Request) {
  try {
    // Forward request to Python backend
    const response = await fetch(`${BACKEND_URL}/api/reservations/admin`, {
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
    console.error('Admin reservations error:', error);
    return Response.json(
      { error: 'Failed to fetch admin reservations' },
      { status: 500 }
    );
  }
}
