// API integration layer with typed fetch helpers and centralized error handling

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || '/api';

export interface AgentMessage {
  session_id: string;
  message: string;
  context?: Record<string, unknown>;
}

export interface AgentResponse {
  type: 'llm_response' | 'tool_result';
  text: string;
  suggested_replies?: string[];
  structured?: {
    intent?: string;
    venues?: Array<{
      id: string;
      name: string;
      distance_km?: number;
      score?: number;
      cuisine?: string[];
      rating?: number;
      price_tier?: number;
      capacity?: number;
      image?: string;
      tags?: string[];
    }>;
  };
}

export interface RecommendRequest {
  city?: string;
  cuisine?: string;
  datetime?: string;
  party_size?: number;
  prefs?: Record<string, unknown>;
}

export interface Reservation {
  id: string;
  venue_id: string;
  venue_name: string;
  datetime: string;
  party_size: number;
  status: 'confirmed' | 'pending' | 'cancelled';
  contact: {
    name: string;
    phone: string;
    email: string;
  };
  notes?: string;
  booking_id: string;
}

export async function postMessage(request: AgentMessage): Promise<AgentResponse> {
  const res = await fetch(`${API_BASE}/agent/message`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request),
  });

  if (!res.ok) {
    throw new Error(`Agent API error: ${res.statusText}`);
  }

  return res.json();
}

export async function getRecommendations(request: RecommendRequest): Promise<AgentResponse> {
  const res = await fetch(`${API_BASE}/agent/recommend`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request),
  });

  if (!res.ok) {
    throw new Error(`Recommendations API error: ${res.statusText}`);
  }

  return res.json();
}

export async function createReservation(data: {
  venue_id: string;
  datetime: string;
  party_size: number;
  contact: { name: string; phone: string; email: string };
  notes?: string;
}): Promise<Reservation> {
  const sessionId = typeof window !== 'undefined' ? localStorage.getItem('goodfoods_session_id') || 'default_session' : 'default_session';
  
  const res = await fetch(`${API_BASE}/reservations/create?session_id=${sessionId}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    throw new Error(`Reservation API error: ${res.statusText}`);
  }

  return res.json();
}

export async function getReservations(sessionId: string): Promise<Reservation[]> {
  const res = await fetch(`${API_BASE}/reservations?session_id=${sessionId}`);

  if (!res.ok) {
    throw new Error(`Reservations API error: ${res.statusText}`);
  }

  return res.json();
}

export async function cancelReservation(reservationId: string): Promise<{ success: boolean }> {
  const res = await fetch(`${API_BASE}/reservations/${reservationId}/cancel`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
  });

  if (!res.ok) {
    throw new Error(`Cancel API error: ${res.statusText}`);
  }

  return res.json();
}
