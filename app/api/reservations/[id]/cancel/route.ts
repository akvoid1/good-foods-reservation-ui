// Proxy to Python backend
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';

export async function POST(
  request: Request,
  context: { params: Promise<{ id: string }> }
) {
  try {
    const params = await context.params;
    const { id } = params;

    if (!id) {
      return Response.json(
        { error: 'Reservation ID required' },
        { status: 400 }
      );
    }

    // Forward request to Python backend
    const response = await fetch(`${BACKEND_URL}/api/reservations/${id}/cancel`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Backend cancel error:', response.status, errorText);
      return Response.json(
        { error: 'Failed to cancel reservation' },
        { status: response.status }
      );
    }

    const data = await response.json();
    return Response.json(data);
  } catch (error) {
    console.error('Cancellation error:', error);
    return Response.json(
      { error: 'Failed to cancel reservation' },
      { status: 500 }
    );
  }
}
