'use client';

import { useState, useMemo } from 'react';
import { MapView } from '@/components/map-view';
import { FilterBar } from '@/components/filter-bar';
import { VenueCard } from '@/components/venue-card';
import { ReservationModal } from '@/components/reservation-modal';
import { Button } from '@/components/ui/button';
import { ArrowLeft } from 'lucide-react';
import Link from 'next/link';

// Sample venue data (same as home page, extended)
const ALL_VENUES = [
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
  {
    id: 'v005',
    name: 'Curry Corner',
    cuisine: ['Indian'],
    rating: 4.4,
    capacity: 100,
    price_tier: 1,
    distance_km: 1.5,
    image: '/placeholder.svg?key=x7k2p',
    tags: ['Budget-friendly', 'Family'],
  },
  {
    id: 'v006',
    name: 'Bella Italia',
    cuisine: ['Italian'],
    rating: 4.7,
    capacity: 90,
    price_tier: 2,
    distance_km: 2.8,
    image: '/placeholder.svg?key=m9n4l',
    tags: ['Pasta', 'Romantic'],
  },
  {
    id: 'v007',
    name: 'Tokyo Kitchen',
    cuisine: ['Japanese'],
    rating: 4.6,
    capacity: 70,
    price_tier: 3,
    distance_km: 1.9,
    image: '/placeholder.svg?key=q5w8r',
    tags: ['Sushi', 'Modern'],
  },
  {
    id: 'v008',
    name: 'Mediterranean Grill',
    cuisine: ['Mediterranean', 'Greek'],
    rating: 4.5,
    capacity: 110,
    price_tier: 2,
    distance_km: 2.3,
    image: '/placeholder.svg?key=e3t6y',
    tags: ['Seafood', 'Outdoor'],
  },
];

export default function DiscoverPage() {
  const [cuisine, setCuisine] = useState('All');
  const [priceMin, setPriceMin] = useState(1);
  const [priceMax, setPriceMax] = useState(4);
  const [capacity, setCapacity] = useState(2);
  const [selectedVenue, setSelectedVenue] = useState<any>(null);
  const [showReservation, setShowReservation] = useState(false);

  // Filter venues based on criteria
  const filteredVenues = useMemo(() => {
    return ALL_VENUES.filter(venue => {
      const cuisineMatch = cuisine === 'All' || venue.cuisine.includes(cuisine);
      const priceMatch = venue.price_tier >= priceMin && venue.price_tier <= priceMax;
      const capacityMatch = venue.capacity >= capacity;
      return cuisineMatch && priceMatch && capacityMatch;
    });
  }, [cuisine, priceMin, priceMax, capacity]);

  const handleReset = () => {
    setCuisine('All');
    setPriceMin(1);
    setPriceMax(4);
    setCapacity(2);
  };

  const handleVenueSelect = (venue: any) => {
    setSelectedVenue(venue);
    setShowReservation(true);
  };

  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center gap-3">
          <Link href="/">
            <Button variant="ghost" size="sm" className="gap-2">
              <ArrowLeft className="w-4 h-4" />
              Back
            </Button>
          </Link>
          <h1 className="font-bold text-xl">Discover Venues</h1>
        </div>
      </header>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 py-8">
        {/* Filters */}
        <div className="mb-8">
          <FilterBar
            cuisine={cuisine}
            onCuisineChange={setCuisine}
            priceMin={priceMin}
            priceMax={priceMax}
            onPriceChange={(min, max) => {
              setPriceMin(min);
              setPriceMax(max);
            }}
            capacity={capacity}
            onCapacityChange={setCapacity}
            onReset={handleReset}
          />
        </div>

        {/* Split Layout: Map + List */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Map (left on desktop, top on mobile) */}
          <div className="lg:col-span-1">
            <MapView
              venues={filteredVenues}
              selectedVenue={selectedVenue}
              onVenueSelect={handleVenueSelect}
            />
          </div>

          {/* Venue List (right on desktop, bottom on mobile) */}
          <div className="lg:col-span-2">
            {filteredVenues.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {filteredVenues.map(venue => (
                  <VenueCard
                    key={venue.id}
                    {...venue}
                    onSelect={() => handleVenueSelect(venue)}
                  />
                ))}
              </div>
            ) : (
              <div className="flex flex-col items-center justify-center py-12 px-4">
                <p className="text-muted-foreground mb-2">No matches found</p>
                <p className="text-sm text-muted-foreground text-center mb-4">
                  Widen your filters or try a different search
                </p>
                <Button onClick={handleReset} variant="outline">
                  Reset Filters
                </Button>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Reservation Modal */}
      <ReservationModal
        open={showReservation}
        venue={selectedVenue}
        onClose={() => {
          setShowReservation(false);
          setSelectedVenue(null);
        }}
        onSuccess={() => {
          setShowReservation(false);
          setSelectedVenue(null);
        }}
      />
    </main>
  );
}
