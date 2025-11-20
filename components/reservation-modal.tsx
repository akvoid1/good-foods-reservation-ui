'use client';

import { useState } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Card } from '@/components/ui/card';
import { Loader2, Check, AlertCircle } from 'lucide-react';
import { createReservation } from '@/lib/api';

interface Venue {
  id: string;
  name: string;
}

interface ReservationModalProps {
  open: boolean;
  venue: Venue | null;
  onClose: () => void;
  onSuccess: (reservation: any) => void;
}

type Step = 'datetime' | 'contact' | 'confirm' | 'success';

export function ReservationModal({
  open,
  venue,
  onClose,
  onSuccess,
}: ReservationModalProps) {
  const [step, setStep] = useState<Step>('datetime');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  
  const [formData, setFormData] = useState({
    date: new Date().toISOString().split('T')[0],
    time: '19:00',
    party_size: 2,
    name: '',
    phone: '',
    email: '',
    notes: '',
  });

  const handleDateTimeNext = () => {
    if (!formData.date || !formData.time) {
      setError('Please select date and time');
      return;
    }
    setError(null);
    setStep('contact');
  };

  const handleContactNext = () => {
    if (!formData.name || !formData.phone || !formData.email) {
      setError('Please fill in all contact details');
      return;
    }
    setError(null);
    setStep('confirm');
  };

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);

    try {
      const datetime = `${formData.date}T${formData.time}:00`;
      const reservation = await createReservation({
        venue_id: venue?.id || '',
        datetime,
        party_size: formData.party_size,
        contact: {
          name: formData.name,
          phone: formData.phone,
          email: formData.email,
        },
        notes: formData.notes || undefined,
      });

      setStep('success');
      onSuccess(reservation);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create reservation');
    } finally {
      setLoading(false);
    }
  };

  const handleClose = () => {
    if (step === 'success') {
      setStep('datetime');
      setFormData({
        date: new Date().toISOString().split('T')[0],
        time: '19:00',
        party_size: 2,
        name: '',
        phone: '',
        email: '',
        notes: '',
      });
      setError(null);
    }
    onClose();
  };

  if (step === 'success') {
    return (
      <Dialog open={open} onOpenChange={handleClose}>
        <DialogContent className="text-center">
          <div className="flex justify-center mb-4">
            <Check className="w-16 h-16 text-success" />
          </div>
          <h2 className="text-2xl font-bold mb-2">Reservation Confirmed</h2>
          <p className="text-muted-foreground mb-4">
            Your booking ID is <span className="font-mono font-bold text-foreground">GF-{Math.random().toString(36).substring(7).toUpperCase()}</span>
          </p>
          <p className="text-sm text-muted-foreground mb-6">
            We've sent the details to {formData.email}
          </p>
          <Button onClick={handleClose} className="w-full">
            Done
          </Button>
        </DialogContent>
      </Dialog>
    );
  }

  return (
    <Dialog open={open && step !== 'success'} onOpenChange={handleClose}>
      <DialogContent className="max-w-md">
        <DialogHeader>
          <DialogTitle>Reserve at {venue?.name}</DialogTitle>
        </DialogHeader>

        {error && (
          <div className="flex gap-2 p-3 bg-destructive/10 text-destructive rounded-lg text-sm">
            <AlertCircle className="w-4 h-4 flex-shrink-0 mt-0.5" />
            {error}
          </div>
        )}

        {/* Step indicators */}
        <div className="flex gap-1 mb-6">
          {['datetime', 'contact', 'confirm'].map((s) => (
            <div
              key={s}
              className={`flex-1 h-1 rounded-full ${
                step === s ? 'bg-primary' : ['datetime', 'contact'].includes(step) && s === 'confirm' ? 'bg-border' : 'bg-border'
              }`}
            />
          ))}
        </div>

        {/* Date & Time Step */}
        {step === 'datetime' && (
          <div className="space-y-4">
            <div>
              <Label htmlFor="date">Date</Label>
              <Input
                id="date"
                type="date"
                value={formData.date}
                onChange={e => setFormData({ ...formData, date: e.target.value })}
              />
            </div>
            <div>
              <Label htmlFor="time">Time</Label>
              <Input
                id="time"
                type="time"
                value={formData.time}
                onChange={e => setFormData({ ...formData, time: e.target.value })}
              />
            </div>
            <div>
              <Label htmlFor="party_size">Party Size</Label>
              <Input
                id="party_size"
                type="number"
                min="1"
                max="20"
                value={formData.party_size}
                onChange={e => setFormData({ ...formData, party_size: parseInt(e.target.value) })}
              />
            </div>
            <Button onClick={handleDateTimeNext} className="w-full">
              Next
            </Button>
          </div>
        )}

        {/* Contact Step */}
        {step === 'contact' && (
          <div className="space-y-4">
            <div>
              <Label htmlFor="name">Full Name</Label>
              <Input
                id="name"
                value={formData.name}
                onChange={e => setFormData({ ...formData, name: e.target.value })}
              />
            </div>
            <div>
              <Label htmlFor="phone">Phone</Label>
              <Input
                id="phone"
                type="tel"
                value={formData.phone}
                onChange={e => setFormData({ ...formData, phone: e.target.value })}
              />
            </div>
            <div>
              <Label htmlFor="email">Email</Label>
              <Input
                id="email"
                type="email"
                value={formData.email}
                onChange={e => setFormData({ ...formData, email: e.target.value })}
              />
            </div>
            <div className="flex gap-2">
              <Button onClick={() => setStep('datetime')} variant="outline" className="flex-1">
                Back
              </Button>
              <Button onClick={handleContactNext} className="flex-1">
                Next
              </Button>
            </div>
          </div>
        )}

        {/* Confirm Step */}
        {step === 'confirm' && (
          <div className="space-y-4">
            <Card className="p-4 bg-muted/50">
              <div className="space-y-2 text-sm">
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Restaurant</span>
                  <span className="font-semibold">{venue?.name}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Date & Time</span>
                  <span className="font-semibold">
                    {new Date(`${formData.date}T${formData.time}`).toLocaleDateString()} at {formData.time}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Party Size</span>
                  <span className="font-semibold">{formData.party_size} {formData.party_size === 1 ? 'person' : 'people'}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Name</span>
                  <span className="font-semibold">{formData.name}</span>
                </div>
              </div>
            </Card>

            <div className="flex gap-2">
              <Button onClick={() => setStep('contact')} variant="outline" className="flex-1">
                Back
              </Button>
              <Button onClick={handleSubmit} disabled={loading} className="flex-1 gap-2">
                {loading && <Loader2 className="w-4 h-4 animate-spin" />}
                Confirm
              </Button>
            </div>
          </div>
        )}
      </DialogContent>
    </Dialog>
  );
}
