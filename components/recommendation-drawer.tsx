'use client';

import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { X, MapPin, Zap } from 'lucide-react';
import { VenueCard } from './venue-card';

interface Venue {
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
}

interface RecommendationDrawerProps {
  open: boolean;
  venues: Venue[];
  onClose: () => void;
  onVenueSelect: (venue: Venue) => void;
}

export function RecommendationDrawer({
  open,
  venues,
  onClose,
  onVenueSelect,
}: RecommendationDrawerProps) {
  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent className="max-w-2xl max-h-[80vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <Zap className="w-5 h-5 text-accent" />
            Recommended for You
          </DialogTitle>
        </DialogHeader>

        <div className="grid gap-4 py-4">
          {venues.map(venue => (
            <div key={venue.id} className="flex gap-3 p-3 border border-border rounded-lg hover:bg-muted/50 transition-colors">
              <div className="flex-1 min-w-0">
                <div className="flex items-start justify-between gap-2 mb-1">
                  <h4 className="font-semibold text-sm line-clamp-1">{venue.name}</h4>
                  {venue.score && (
                    <Badge variant="default" className="text-xs">
                      {Math.round(venue.score * 100)}% match
                    </Badge>
                  )}
                </div>
                <div className="flex items-center gap-2 text-xs text-muted-foreground mb-2">
                  {venue.cuisine && (
                    <span>{venue.cuisine.slice(0, 2).join(', ')}</span>
                  )}
                  {venue.distance_km && (
                    <>
                      <span>•</span>
                      <span className="flex items-center gap-1">
                        <MapPin className="w-3 h-3" />
                        {venue.distance_km.toFixed(1)} km
                      </span>
                    </>
                  )}
                </div>
                <Button
                  size="sm"
                  onClick={() => onVenueSelect(venue)}
                  className="text-xs"
                >
                  Book Now
                </Button>
              </div>
            </div>
          ))}
        </div>
      </DialogContent>
    </Dialog>
  );
}
