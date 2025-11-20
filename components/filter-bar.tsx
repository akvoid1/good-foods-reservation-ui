'use client';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Card } from '@/components/ui/card';
import { Sliders } from 'lucide-react';

interface FilterBarProps {
  cuisine: string;
  onCuisineChange: (value: string) => void;
  priceMin: number;
  priceMax: number;
  onPriceChange: (min: number, max: number) => void;
  capacity: number;
  onCapacityChange: (value: number) => void;
  onReset: () => void;
}

const CUISINES = ['All', 'Indian', 'Italian', 'Chinese', 'French', 'Mediterranean', 'Asian', 'Japanese'];

export function FilterBar({
  cuisine,
  onCuisineChange,
  priceMin,
  priceMax,
  onPriceChange,
  capacity,
  onCapacityChange,
  onReset,
}: FilterBarProps) {
  return (
    <Card className="p-4 bg-card">
      <div className="flex items-center gap-2 mb-4">
        <Sliders className="w-4 h-4 text-muted-foreground" />
        <h3 className="font-semibold text-sm">Filters</h3>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Cuisine */}
        <div>
          <Label className="text-xs font-semibold mb-2 block">Cuisine</Label>
          <Select value={cuisine} onValueChange={onCuisineChange}>
            <SelectTrigger className="h-9">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {CUISINES.map(c => (
                <SelectItem key={c} value={c}>
                  {c}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        {/* Price Range */}
        <div>
          <Label className="text-xs font-semibold mb-2 block">Price Range</Label>
          <div className="flex gap-2">
            <Select value={priceMin.toString()} onValueChange={val => onPriceChange(parseInt(val), priceMax)}>
              <SelectTrigger className="h-9">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                {[1, 2, 3, 4].map(p => (
                  <SelectItem key={p} value={p.toString()}>
                    {'€'.repeat(p)}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
            <Select value={priceMax.toString()} onValueChange={val => onPriceChange(priceMin, parseInt(val))}>
              <SelectTrigger className="h-9">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                {[1, 2, 3, 4].map(p => (
                  <SelectItem key={p} value={p.toString()}>
                    {'€'.repeat(p)}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
        </div>

        {/* Capacity */}
        <div>
          <Label htmlFor="capacity" className="text-xs font-semibold mb-2 block">
            Party Size: {capacity}
          </Label>
          <Input
            id="capacity"
            type="range"
            min="1"
            max="20"
            value={capacity}
            onChange={e => onCapacityChange(parseInt(e.target.value))}
            className="h-9"
          />
        </div>

        {/* Reset Button */}
        <div className="flex items-end">
          <Button
            onClick={onReset}
            variant="outline"
            className="w-full h-9"
          >
            Reset Filters
          </Button>
        </div>
      </div>
    </Card>
  );
}
