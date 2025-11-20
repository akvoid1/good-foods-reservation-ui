'use client';

import { Card } from '@/components/ui/card';
import { type LucideIcon } from 'lucide-react';

interface AdminStatsCardProps {
  title: string;
  value: string | number;
  description?: string;
  icon: LucideIcon;
  trend?: { value: number; positive: boolean };
}

export function AdminStatsCard({
  title,
  value,
  description,
  icon: Icon,
  trend,
}: AdminStatsCardProps) {
  return (
    <Card className="p-6">
      <div className="flex items-start justify-between">
        <div>
          <p className="text-sm text-muted-foreground mb-1">{title}</p>
          <p className="text-3xl font-bold">{value}</p>
          {description && <p className="text-xs text-muted-foreground mt-2">{description}</p>}
        </div>
        <div className="w-10 h-10 bg-accent/10 rounded-lg flex items-center justify-center">
          <Icon className="w-5 h-5 text-accent" />
        </div>
      </div>
      {trend && (
        <div className={`text-xs mt-3 ${trend.positive ? 'text-success' : 'text-destructive'}`}>
          {trend.positive ? '↑' : '↓'} {Math.abs(trend.value)}% vs last week
        </div>
      )}
    </Card>
  );
}
