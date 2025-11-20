'use client';

import { Card } from '@/components/ui/card';
import { MapPin } from 'lucide-react';

interface MapViewProps {
  venues: any[];
  selectedVenue: any;
  onVenueSelect: (venue: any) => void;
}

export function MapView({ venues, selectedVenue, onVenueSelect }: MapViewProps) {
  return (
    <Card className="h-full min-h-96 bg-muted/30 flex items-center justify-center relative overflow-hidden">
      {/* Placeholder for Leaflet/Mapbox integration */}
      <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-accent/5"></div>
      
      <div className="relative z-10 text-center px-4">
        <MapPin className="w-12 h-12 text-muted-foreground mx-auto mb-3 opacity-50" />
        <p className="text-muted-foreground text-sm mb-2">Map View</p>
        <p className="text-xs text-muted-foreground">
          {venues.length} venues in your area
        </p>
        <p className="text-xs text-muted-foreground mt-4">
          Integrate with Leaflet or Mapbox to show interactive map
        </p>
      </div>

      {/* Venue pins overlay */}
      {venues.map((venue, i) => (
        <div
          key={venue.id}
          className="absolute w-8 h-8 bg-primary rounded-full flex items-center justify-center text-white text-xs font-bold cursor-pointer hover:scale-110 transition-transform"
          style={{
            left: `${20 + (i * 15) % 60}%`,
            top: `${30 + (i * 20) % 40}%`,
          }}
          onClick={() => onVenueSelect(venue)}
          title={venue.name}
        >
          {i + 1}
        </div>
      ))}
    </Card>
  );
}
