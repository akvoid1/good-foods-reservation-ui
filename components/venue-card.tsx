'use client';

import Image from 'next/image';
import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { MapPin, Users, DollarSign, Star } from 'lucide-react';

interface VenueCardProps {
  id: string;
  name: string;
  cuisine: string[];
  rating?: number;
  capacity?: number;
  price_tier?: number;
  distance_km?: number;
  image?: string;
  tags?: string[];
  onSelect: () => void;
}

export function VenueCard({
  id,
  name,
  cuisine,
  rating,
  capacity,
  price_tier,
  distance_km,
  image,
  tags,
  onSelect,
}: VenueCardProps) {
  const priceDisplay = price_tier ? '€'.repeat(price_tier) : 'N/A';

  return (
    <Card className="overflow-hidden hover:shadow-lg transition-shadow cursor-pointer" onClick={onSelect}>
      {image && (
        <div className="relative h-48 w-full bg-muted">
          <Image
            src={image || "/placeholder.svg"}
            alt={name}
            fill
            className="object-cover"
            loading="lazy"
          />
        </div>
      )}
      <div className="p-4">
        <div className="flex items-start justify-between gap-2 mb-2">
          <h3 className="font-semibold text-lg text-balance">{name}</h3>
          {rating && (
            <div className="flex items-center gap-1 text-sm text-accent">
              <Star className="w-4 h-4 fill-accent" />
              {rating.toFixed(1)}
            </div>
          )}
        </div>

        <div className="flex flex-wrap gap-1 mb-3">
          {cuisine.slice(0, 2).map(c => (
            <Badge key={c} variant="secondary" className="text-xs">
              {c}
            </Badge>
          ))}
        </div>

        <div className="grid grid-cols-3 gap-2 mb-3 text-sm text-muted-foreground">
          {distance_km !== undefined && (
            <div className="flex items-center gap-1">
              <MapPin className="w-4 h-4" />
              <span>{distance_km.toFixed(1)} km</span>
            </div>
          )}
          {capacity && (
            <div className="flex items-center gap-1">
              <Users className="w-4 h-4" />
              <span>{capacity} seats</span>
            </div>
          )}
          {price_tier && (
            <div className="flex items-center gap-1">
              <DollarSign className="w-4 h-4" />
              <span>{priceDisplay}</span>
            </div>
          )}
        </div>

        {tags && tags.length > 0 && (
          <div className="flex flex-wrap gap-1 mb-3">
            {tags.slice(0, 2).map(tag => (
              <span key={tag} className="text-xs bg-accent/10 text-accent px-2 py-1 rounded">
                {tag}
              </span>
            ))}
          </div>
        )}

        <Button onClick={onSelect} className="w-full">
          View Details
        </Button>
      </div>
    </Card>
  );
}
