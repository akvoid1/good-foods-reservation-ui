'use client';

import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { ArrowLeft, Calendar } from 'lucide-react';
import Link from 'next/link';
import { getReservations, Reservation } from '@/lib/api';
import { getSessionId } from '@/lib/session';
import { ReservationListItem } from '@/components/reservation-list-item';
import { Skeleton } from '@/components/ui/skeleton';

export default function ReservationsPage() {
  const [reservations, setReservations] = useState<Reservation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadReservations = async () => {
      try {
        setLoading(true);
        // For demo purposes, show all reservations (admin view)
        // In production, this would be filtered by authenticated user
        const response = await fetch('/api/reservations/admin');
        if (response.ok) {
          const data = await response.json();
          setReservations(data);
        } else {
          throw new Error('Failed to load reservations');
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load reservations');
      } finally {
        setLoading(false);
      }
    };

    loadReservations();
  }, []);

  const upcomingReservations = reservations.filter(r => new Date(r.datetime) > new Date());
  const pastReservations = reservations.filter(r => new Date(r.datetime) <= new Date());

  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card sticky top-0 z-40">
        <div className="max-w-4xl mx-auto px-4 py-4 flex items-center gap-3">
          <Link href="/">
            <Button variant="ghost" size="sm" className="gap-2">
              <ArrowLeft className="w-4 h-4" />
              Back
            </Button>
          </Link>
          <div>
            <h1 className="font-bold text-xl flex items-center gap-2">
              <Calendar className="w-5 h-5 text-primary" />
              My Reservations
            </h1>
          </div>
        </div>
      </header>

      {/* Content */}
      <div className="max-w-4xl mx-auto px-4 py-8">
        {error && (
          <div className="p-4 bg-destructive/10 text-destructive rounded-lg mb-6 text-sm">
            {error}
          </div>
        )}

        {loading ? (
          <div className="space-y-4">
            {[1, 2, 3].map(i => (
              <Skeleton key={i} className="h-48 rounded-lg" />
            ))}
          </div>
        ) : reservations.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-16 px-4">
            <Calendar className="w-16 h-16 text-muted-foreground mb-4 opacity-50" />
            <p className="text-lg font-semibold mb-2">No reservations yet</p>
            <p className="text-muted-foreground text-center mb-6">
              Find and book a restaurant to see your reservations here.
            </p>
            <Link href="/discover">
              <Button>Discover Restaurants</Button>
            </Link>
          </div>
        ) : (
          <div className="space-y-8">
            {/* Upcoming Reservations */}
            {upcomingReservations.length > 0 && (
              <section>
                <h2 className="text-xl font-bold mb-4">Upcoming Reservations</h2>
                <div className="grid gap-4">
                  {upcomingReservations.map(reservation => (
                    <ReservationListItem
                      key={reservation.id}
                      reservation={reservation}
                      onCancel={id => setReservations(prev => prev.filter(r => r.id !== id))}
                    />
                  ))}
                </div>
              </section>
            )}

            {/* Past Reservations */}
            {pastReservations.length > 0 && (
              <section>
                <h2 className="text-xl font-bold mb-4">Past Reservations</h2>
                <div className="grid gap-4">
                  {pastReservations.map(reservation => (
                    <ReservationListItem
                      key={reservation.id}
                      reservation={reservation}
                      onCancel={id => setReservations(prev => prev.filter(r => r.id !== id))}
                    />
                  ))}
                </div>
              </section>
            )}
          </div>
        )}
      </div>
    </main>
  );
}
