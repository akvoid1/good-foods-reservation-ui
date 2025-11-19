'use client';

import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { ArrowLeft, BarChart3, Users, Calendar, TrendingUp, RefreshCw } from 'lucide-react';
import Link from 'next/link';
import { AdminStatsCard } from '@/components/admin-stats-card';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || '/api';

interface Reservation {
  id: string;
  venue_name: string;
  datetime: string;
  party_size: number;
  status: string;
}

export default function AdminPage() {
  const [mounted, setMounted] = useState(false);
  const [loading, setLoading] = useState(true);
  const [reservations, setReservations] = useState<Reservation[]>([]);
  const [stats, setStats] = useState({
    totalReservations: 0,
    confirmedBookings: 0,
    occupancyRate: 0,
    avgPartySize: 0,
  });

  const fetchReservations = async () => {
    try {
      setLoading(true);
      // Fetch all reservations from backend (admin view)
      const response = await fetch(`${API_BASE}/reservations/admin`);
      if (response.ok) {
        const data = await response.json();
        setReservations(data);
        
        // Calculate stats from real data
        const confirmed = data.filter((r: Reservation) => r.status === 'confirmed').length;
        const avgSize = data.length > 0 
          ? Math.round(data.reduce((sum: number, r: Reservation) => sum + r.party_size, 0) / data.length)
          : 0;

        setStats({
          totalReservations: data.length,
          confirmedBookings: confirmed,
          occupancyRate: data.length > 0 ? Math.round((confirmed / data.length) * 100) : 0,
          avgPartySize: avgSize,
        });
      }
    } catch (error) {
      console.error('Failed to fetch reservations:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    setMounted(true);
    fetchReservations();
    
    // Auto-refresh every 30 seconds
    const interval = setInterval(fetchReservations, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card sticky top-0 z-40">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center gap-3">
          <Link href="/">
            <Button variant="ghost" size="sm" className="gap-2">
              <ArrowLeft className="w-4 h-4" />
              Back
            </Button>
          </Link>
          <div>
            <h1 className="font-bold text-xl flex items-center gap-2">
              <BarChart3 className="w-5 h-5 text-primary" />
              Manager Dashboard
            </h1>
            <p className="text-xs text-muted-foreground">Stub - Limited Data</p>
          </div>
        </div>
      </header>

      {/* Dashboard Content */}
      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Refresh Button */}
        <div className="flex justify-end mb-4">
          <Button
            variant="outline"
            size="sm"
            onClick={fetchReservations}
            disabled={loading}
            className="gap-2"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
            Refresh
          </Button>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
          <AdminStatsCard
            title="Total Reservations"
            value={stats.totalReservations}
            description="This week"
            icon={Calendar}
            trend={{ value: 12, positive: true }}
          />
          <AdminStatsCard
            title="Confirmed Bookings"
            value={stats.confirmedBookings}
            description={`${stats.occupancyRate}% of reservations`}
            icon={Users}
            trend={{ value: 5, positive: true }}
          />
          <AdminStatsCard
            title="Occupancy Rate"
            value={`${stats.occupancyRate}%`}
            description="Average utilization"
            icon={TrendingUp}
            trend={{ value: 3, positive: false }}
          />
          <AdminStatsCard
            title="Avg Party Size"
            value={stats.avgPartySize}
            description="Guests per booking"
            icon={Users}
          />
        </div>

        {/* Upcoming Reservations Table */}
        <div className="grid grid-cols-1 gap-6">
          <Card className="p-6">
            <h2 className="text-xl font-bold mb-4">Upcoming Reservations</h2>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-border">
                    <th className="text-left py-3 px-4 font-semibold text-muted-foreground">Venue</th>
                    <th className="text-left py-3 px-4 font-semibold text-muted-foreground">Date</th>
                    <th className="text-left py-3 px-4 font-semibold text-muted-foreground">Time</th>
                    <th className="text-left py-3 px-4 font-semibold text-muted-foreground">Party Size</th>
                    <th className="text-left py-3 px-4 font-semibold text-muted-foreground">Status</th>
                  </tr>
                </thead>
                <tbody>
                  {loading ? (
                    <tr>
                      <td colSpan={5} className="py-8 text-center text-muted-foreground">
                        Loading reservations...
                      </td>
                    </tr>
                  ) : reservations.length === 0 ? (
                    <tr>
                      <td colSpan={5} className="py-8 text-center text-muted-foreground">
                        No reservations yet
                      </td>
                    </tr>
                  ) : (
                    reservations.slice(0, 10).map(reservation => {
                      const date = new Date(reservation.datetime);
                      // Convert to IST (UTC+5:30)
                      const istDate = new Date(date.getTime() + (5.5 * 60 * 60 * 1000));
                      return (
                        <tr key={reservation.id} className="border-b border-border hover:bg-muted/50 transition-colors">
                          <td className="py-3 px-4 font-medium">{reservation.venue_name}</td>
                          <td className="py-3 px-4 text-muted-foreground">
                            {mounted ? istDate.toLocaleDateString('en-IN') : reservation.datetime}
                          </td>
                          <td className="py-3 px-4 text-muted-foreground">
                            {mounted ? istDate.toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit', hour12: true }) : ''}
                          </td>
                          <td className="py-3 px-4 text-muted-foreground">{reservation.party_size}</td>
                          <td className="py-3 px-4">
                            <span
                              className={`px-2 py-1 rounded-full text-xs font-medium ${
                                reservation.status === 'confirmed'
                                  ? 'bg-success/10 text-success'
                                  : reservation.status === 'cancelled'
                                  ? 'bg-destructive/10 text-destructive'
                                  : 'bg-accent/10 text-accent'
                              }`}
                            >
                              {reservation.status.charAt(0).toUpperCase() + reservation.status.slice(1)}
                            </span>
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </Card>

          {/* Performance Snapshot */}
          <Card className="p-6">
            <h2 className="text-xl font-bold mb-4">Venue Performance</h2>
            <div className="space-y-3">
              {loading ? (
                <div className="text-center py-4 text-muted-foreground">Loading...</div>
              ) : (() => {
                // Calculate venue performance from real data
                const venueStats = reservations.reduce((acc: any, r) => {
                  if (!acc[r.venue_name]) {
                    acc[r.venue_name] = { total: 0, confirmed: 0 };
                  }
                  acc[r.venue_name].total++;
                  if (r.status === 'confirmed') {
                    acc[r.venue_name].confirmed++;
                  }
                  return acc;
                }, {});

                const topVenues = Object.entries(venueStats)
                  .map(([name, stats]: [string, any]) => ({
                    name,
                    rate: stats.total > 0 ? Math.round((stats.confirmed / stats.total) * 100) : 0,
                  }))
                  .sort((a, b) => b.rate - a.rate)
                  .slice(0, 4);

                return topVenues.length > 0 ? (
                  topVenues.map(venue => (
                    <div key={venue.name} className="flex items-center justify-between pb-3 border-b border-border">
                      <span className="font-medium">{venue.name}</span>
                      <div className="flex items-center gap-4">
                        <div 
                          className="h-2 rounded-full"
                          style={{
                            background: 'linear-gradient(to right, var(--color-primary), var(--color-accent))',
                            width: `${Math.max(venue.rate * 1.2, 20)}px`,
                          }} 
                        />
                        <span className="text-sm text-muted-foreground w-12 text-right">
                          {venue.rate}%
                        </span>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="text-center py-4 text-muted-foreground">No data yet</div>
                );
              })()}
            </div>
          </Card>
        </div>
      </div>
    </main>
  );
}
