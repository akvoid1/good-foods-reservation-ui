'use client';

import { useState } from 'react';
import { ChatPane } from '@/components/chat-pane';
import { RecommendationDrawer } from '@/components/recommendation-drawer';
import { ReservationModal } from '@/components/reservation-modal';
import { VenueCard } from '@/components/venue-card';
import { Button } from '@/components/ui/button';
import { Utensils, Zap, Search, Bookmark, BarChart3 } from 'lucide-react';
import Link from 'next/link';

// Sample venue data
const SAMPLE_VENUES = [
  {
    id: 'v001',
    name: 'Saffron House',
    cuisine: ['Indian', 'South Indian'],
    rating: 4.8,
    capacity: 120,
    price_tier: 2,
    distance_km: 1.2,
    image: '/upscale-indian-restaurant-interior.jpg',
    tags: ['Outdoor seating', 'Vegetarian'],
  },
  {
    id: 'v002',
    name: 'The Oak',
    cuisine: ['Mediterranean', 'Italian'],
    rating: 4.6,
    capacity: 80,
    price_tier: 3,
    distance_km: 2.1,
    image: '/modern-italian-restaurant-ambiance.jpg',
    tags: ['Wine selection', 'Quiet'],
  },
  {
    id: 'v003',
    name: 'Dragon Palace',
    cuisine: ['Chinese', 'Asian'],
    rating: 4.5,
    capacity: 150,
    price_tier: 2,
    distance_km: 0.8,
    image: '/elegant-asian-dining-space.jpg',
    tags: ['Private rooms', 'Group friendly'],
  },
  {
    id: 'v004',
    name: 'Le Blanc',
    cuisine: ['French', 'Fine Dining'],
    rating: 4.9,
    capacity: 60,
    price_tier: 4,
    distance_km: 3.5,
    image: '/luxury-french-restaurant-elegant.jpg',
    tags: ['Premium', 'Romantic'],
  },
];

export default function Home() {
  const [showChat, setShowChat] = useState(true);
  const [recommendedVenues, setRecommendedVenues] = useState<any[]>([]);
  const [selectedVenue, setSelectedVenue] = useState<any>(null);
  const [showReservation, setShowReservation] = useState(false);
  const [showRecommendations, setShowRecommendations] = useState(false);

  const handleVenueSelect = (venues: any[]) => {
    setRecommendedVenues(venues);
    setShowRecommendations(true);
  };

  const handleRecommendationSelect = (venue: any) => {
    setSelectedVenue(venue);
    setShowReservation(true);
    setShowRecommendations(false);
  };

  const handleVenueCardClick = (venue: any) => {
    setSelectedVenue(venue);
    setShowReservation(true);
  };

  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-primary rounded-lg flex items-center justify-center">
              <Utensils className="w-6 h-6 text-primary-foreground" />
            </div>
            <div>
              <h1 className="font-bold text-xl">GoodFoods</h1>
              <p className="text-xs text-muted-foreground">AI-powered reservations</p>
            </div>
          </div>
          <div className="flex gap-2">
            <Link href="/reservations">
              <Button variant="outline" size="sm" className="gap-2">
                <Bookmark className="w-4 h-4" />
                <span className="hidden sm:inline">Bookings</span>
              </Button>
            </Link>
            <Link href="/admin">
              <Button variant="outline" size="sm" className="gap-2">
                <BarChart3 className="w-4 h-4" />
                <span className="hidden sm:inline">Admin</span>
              </Button>
            </Link>
          </div>
        </div>
      </header>

      {/* Hero + Chat Section */}
      <section className="border-b border-border bg-gradient-to-b from-muted/30 to-background py-8 md:py-12">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-8">
            <h2 className="text-3xl md:text-4xl font-bold mb-3 text-balance">
              Find the Perfect Table — Fast
            </h2>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Chat with our AI to get personalized restaurant recommendations or browse our curated venues.
            </p>
          </div>

          {/* Quick Actions */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mb-8">
            <Button variant="outline" className="gap-2 h-12">
              <Search className="w-4 h-4" />
              Find Near Me
            </Button>
            <Button variant="outline" className="gap-2 h-12">
              <Zap className="w-4 h-4" />
              Make a Reservation
            </Button>
            <Button variant="outline" className="gap-2 h-12">
              <Bookmark className="w-4 h-4" />
              View Bookings
            </Button>
          </div>

          {/* Chat Widget */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <ChatPane onVenueSelect={handleVenueSelect} />
            </div>

            {/* Featured Venues Sidebar */}
            <div className="space-y-3">
              <h3 className="font-semibold text-sm text-muted-foreground uppercase">Featured Venues</h3>
              {SAMPLE_VENUES.slice(0, 3).map(venue => (
                <div
                  key={venue.id}
                  className="p-3 border border-border rounded-lg hover:bg-muted/50 cursor-pointer transition-colors"
                  onClick={() => handleVenueCardClick(venue)}
                >
                  <h4 className="font-semibold text-sm line-clamp-1">{venue.name}</h4>
                  <p className="text-xs text-muted-foreground line-clamp-1">
                    {venue.cuisine.join(', ')}
                  </p>
                  <div className="flex items-center gap-1 mt-1 text-xs">
                    <span className="text-accent">★</span>
                    <span>{venue.rating}</span>
                    <span className="text-muted-foreground">•</span>
                    <span className="text-muted-foreground">{venue.price_tier}€</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Venues Grid */}
      <section className="py-12 md:py-16">
        <div className="max-w-7xl mx-auto px-4">
          <h2 className="text-2xl md:text-3xl font-bold mb-2">Explore Venues</h2>
          <p className="text-muted-foreground mb-8">Browse our collection of hand-picked restaurants</p>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {SAMPLE_VENUES.map(venue => (
              <VenueCard
                key={venue.id}
                {...venue}
                onSelect={() => handleVenueCardClick(venue)}
              />
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border bg-card py-8">
        <div className="max-w-7xl mx-auto px-4 text-center text-sm text-muted-foreground">
          <p>© 2025 GoodFoods. All rights reserved.</p>
        </div>
      </footer>

      {/* Modals */}
      <RecommendationDrawer
        open={showRecommendations}
        venues={recommendedVenues}
        onClose={() => setShowRecommendations(false)}
        onVenueSelect={handleRecommendationSelect}
      />

      <ReservationModal
        open={showReservation}
        venue={selectedVenue}
        onClose={() => {
          setShowReservation(false);
          setSelectedVenue(null);
        }}
        onSuccess={(reservation) => {
          setShowReservation(false);
          setSelectedVenue(null);
        }}
      />
    </main>
  );
}
