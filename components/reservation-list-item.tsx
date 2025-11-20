'use client';

import { Reservation } from '@/lib/api';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Calendar, Users, MapPin, Phone, Mail, Trash2 } from 'lucide-react';
import { useState } from 'react';
import { cancelReservation } from '@/lib/api';

interface ReservationListItemProps {
  reservation: Reservation;
  onCancel: (id: string) => void;
}

export function ReservationListItem({ reservation, onCancel }: ReservationListItemProps) {
  const [deleting, setDeleting] = useState(false);

  const handleCancel = async () => {
    setDeleting(true);
    try {
      await cancelReservation(reservation.id);
      onCancel(reservation.id);
    } catch (error) {
      console.error('Failed to cancel reservation', error);
    } finally {
      setDeleting(false);
    }
  };

  const reservationDate = new Date(reservation.datetime);
  const isUpcoming = reservationDate > new Date();

  return (
    <Card className="p-4">
      <div className="flex items-start justify-between gap-4 mb-3">
        <div>
          <h3 className="font-semibold text-lg">{reservation.venue_name}</h3>
          <p className="text-sm text-muted-foreground">Booking ID: {reservation.booking_id}</p>
        </div>
        <Badge variant={isUpcoming ? 'default' : 'secondary'}>
          {isUpcoming ? 'Upcoming' : 'Past'}
        </Badge>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mb-4 text-sm">
        <div className="flex items-center gap-2 text-muted-foreground">
          <Calendar className="w-4 h-4" />
          {reservationDate.toLocaleDateString()} at {reservationDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
        </div>
        <div className="flex items-center gap-2 text-muted-foreground">
          <Users className="w-4 h-4" />
          {reservation.party_size} {reservation.party_size === 1 ? 'person' : 'people'}
        </div>
      </div>

      <div className="space-y-2 mb-4 text-sm">
        <div className="flex items-center gap-2 text-muted-foreground">
          <Phone className="w-4 h-4" />
          {reservation.contact.phone}
        </div>
        <div className="flex items-center gap-2 text-muted-foreground">
          <Mail className="w-4 h-4" />
          {reservation.contact.email}
        </div>
      </div>

      {isUpcoming && (
        <Button
          onClick={handleCancel}
          disabled={deleting}
          variant="destructive"
          size="sm"
          className="w-full gap-2"
        >
          <Trash2 className="w-4 h-4" />
          Cancel Reservation
        </Button>
      )}
    </Card>
  );
}
