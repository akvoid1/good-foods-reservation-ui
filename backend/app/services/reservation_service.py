from sqlalchemy.orm import Session
from app.database import Reservation, Venue
from datetime import datetime
from typing import List, Optional
import uuid
import random
import string
from app.services.email_service import email_service


class ReservationService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_reservation(
        self,
        session_id: str,
        venue_id: str,
        datetime_str: str,
        party_size: int,
        contact_name: str,
        contact_phone: str,
        contact_email: str,
        notes: Optional[str] = None
    ) -> Reservation:
        """
        Create a new reservation
        """
        # Get venue name
        venue = self.db.query(Venue).filter(Venue.id == venue_id).first()
        venue_name = venue.name if venue else "Unknown Venue"
        
        # Parse datetime
        reservation_datetime = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
        
        # Generate booking ID
        booking_id = f"GF-{''.join(random.choices(string.ascii_uppercase + string.digits, k=6))}"
        
        reservation = Reservation(
            id=f"res_{uuid.uuid4().hex[:12]}",
            booking_id=booking_id,
            venue_id=venue_id,
            venue_name=venue_name,
            session_id=session_id,
            datetime=reservation_datetime,
            party_size=party_size,
            status="confirmed",
            contact_name=contact_name,
            contact_phone=contact_phone,
            contact_email=contact_email,
            notes=notes
        )
        
        self.db.add(reservation)
        self.db.commit()
        self.db.refresh(reservation)
        
        # Send confirmation email
        try:
            email_service.send_reservation_confirmation_sync(
                to_email=contact_email,
                to_name=contact_name,
                booking_id=booking_id,
                venue_name=venue_name,
                reservation_datetime=datetime_str,
                party_size=party_size,
                notes=notes
            )
        except Exception as e:
            import traceback
            print(f"❌ Warning: Failed to send confirmation email: {e}")
            print(f"   Full error: {traceback.format_exc()}")
            # Don't fail the reservation if email fails
        
        return reservation
    
    def get_reservations(self, session_id: str) -> List[Reservation]:
        """
        Get all reservations for a session
        """
        return self.db.query(Reservation).filter(
            Reservation.session_id == session_id,
            Reservation.status != "cancelled"
        ).order_by(Reservation.datetime.desc()).all()
    
    def get_reservation(self, reservation_id: str) -> Optional[Reservation]:
        """
        Get a specific reservation
        """
        return self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
    
    def cancel_reservation(self, reservation_id: str) -> bool:
        """
        Cancel a reservation
        """
        reservation = self.get_reservation(reservation_id)
        if not reservation:
            return False
        
        reservation.status = "cancelled"
        self.db.commit()
        return True
    
    def get_all_reservations(self, limit: int = 100) -> List[Reservation]:
        """
        Get all reservations (for admin)
        """
        return self.db.query(Reservation).order_by(
            Reservation.datetime.desc()
        ).limit(limit).all()
