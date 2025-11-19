import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings
from datetime import datetime


class EmailService:
    """
    Email service for sending reservation confirmations
    
    Note: SMTP must be configured in .env for emails to actually send.
    If SMTP is not configured, emails will be logged but not sent.
    """
    
    def __init__(self):
        self.enabled = settings.smtp_enabled
        self.host = settings.smtp_host
        self.port = settings.smtp_port
        self.user = settings.smtp_user
        self.password = settings.smtp_password
        self.from_email = settings.smtp_from_email
        self.from_name = settings.smtp_from_name
    
    async def send_reservation_confirmation(
        self,
        to_email: str,
        to_name: str,
        booking_id: str,
        venue_name: str,
        reservation_datetime: str,
        party_size: int,
        notes: str = None
    ) -> bool:
        """
        Send reservation confirmation email
        
        Returns True if email was sent successfully, False otherwise
        """
        if not self.enabled:
            print(f"📧 Email disabled in config - Would send confirmation to {to_email}")
            print(f"   Booking ID: {booking_id}")
            print(f"   Venue: {venue_name}")
            return False
        
        # Check if credentials are configured
        if not self.user or not self.password or self.user == "your_email@gmail.com":
            print(f"⚠️  Email credentials not configured - Skipping email to {to_email}")
            print(f"   To enable emails, update SMTP_USER and SMTP_PASSWORD in backend/.env")
            print(f"   See SETUP_EMAIL_CREDENTIALS.md for instructions")
            return False
        
        try:
            # Parse datetime for better formatting
            try:
                dt = datetime.fromisoformat(reservation_datetime.replace('Z', '+00:00'))
                formatted_date = dt.strftime("%A, %B %d, %Y")
                formatted_time = dt.strftime("%I:%M %p")
            except:
                formatted_date = reservation_datetime
                formatted_time = ""
            
            # Create email
            message = MIMEMultipart("alternative")
            message["Subject"] = f"Reservation Confirmed - {venue_name}"
            message["From"] = f"{self.from_name} <{self.from_email}>"
            message["To"] = to_email
            
            # HTML email body
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: linear-gradient(135deg, #0d9488 0%, #f59e0b 100%); 
                              color: white; padding: 30px; text-align: center; border-radius: 8px 8px 0 0; }}
                    .content {{ background: #f9fafb; padding: 30px; border-radius: 0 0 8px 8px; }}
                    .booking-details {{ background: white; padding: 20px; border-radius: 8px; 
                                       margin: 20px 0; border-left: 4px solid #0d9488; }}
                    .detail-row {{ padding: 10px 0; border-bottom: 1px solid #e5e7eb; }}
                    .detail-label {{ font-weight: bold; color: #6b7280; }}
                    .detail-value {{ color: #111827; }}
                    .booking-id {{ font-size: 24px; font-weight: bold; color: #0d9488; 
                                  text-align: center; padding: 15px; background: #f0fdfa; 
                                  border-radius: 8px; margin: 20px 0; }}
                    .footer {{ text-align: center; padding: 20px; color: #6b7280; font-size: 14px; }}
                    .button {{ display: inline-block; padding: 12px 24px; background: #0d9488; 
                              color: white; text-decoration: none; border-radius: 6px; 
                              margin: 20px 0; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1 style="margin: 0;">🎉 Reservation Confirmed!</h1>
                        <p style="margin: 10px 0 0 0;">Your table is reserved</p>
                    </div>
                    
                    <div class="content">
                        <p>Dear {to_name},</p>
                        
                        <p>Great news! Your reservation at <strong>{venue_name}</strong> has been confirmed.</p>
                        
                        <div class="booking-id">
                            Booking ID: {booking_id}
                        </div>
                        
                        <div class="booking-details">
                            <div class="detail-row">
                                <span class="detail-label">📍 Restaurant:</span>
                                <span class="detail-value">{venue_name}</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">📅 Date:</span>
                                <span class="detail-value">{formatted_date}</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">🕐 Time:</span>
                                <span class="detail-value">{formatted_time}</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">👥 Party Size:</span>
                                <span class="detail-value">{party_size} {"person" if party_size == 1 else "people"}</span>
                            </div>
                            {f'<div class="detail-row"><span class="detail-label">📝 Notes:</span><span class="detail-value">{notes}</span></div>' if notes else ''}
                        </div>
                        
                        <p><strong>Important Information:</strong></p>
                        <ul>
                            <li>Please arrive 10 minutes before your reservation time</li>
                            <li>If you need to cancel or modify, please do so at least 2 hours in advance</li>
                            <li>Keep your booking ID handy when you arrive</li>
                        </ul>
                        
                        <p>We look forward to serving you!</p>
                        
                        <p>Best regards,<br>
                        <strong>The GoodFoods Team</strong></p>
                    </div>
                    
                    <div class="footer">
                        <p>This is an automated confirmation email from GoodFoods.</p>
                        <p>If you have any questions, please contact the restaurant directly.</p>
                    </div>
                </div>
            </body>
            </html>
            """
            
            # Attach HTML content
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            
            # Send email
            await aiosmtplib.send(
                message,
                hostname=self.host,
                port=self.port,
                username=self.user,
                password=self.password,
                start_tls=True
            )
            
            print(f"✅ Email sent successfully to {to_email}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to send email to {to_email}: {e}")
            return False
    
    def send_reservation_confirmation_sync(self, *args, **kwargs):
        """
        Synchronous wrapper for sending emails
        Used when async context is not available
        """
        import asyncio
        import threading
        
        result = [None]
        exception = [None]
        
        def run_async():
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result[0] = loop.run_until_complete(
                    self.send_reservation_confirmation(*args, **kwargs)
                )
                loop.close()
            except Exception as e:
                exception[0] = e
        
        thread = threading.Thread(target=run_async)
        thread.start()
        thread.join(timeout=10)  # 10 second timeout
        
        if exception[0]:
            raise exception[0]
        
        return result[0]


# Global email service instance
email_service = EmailService()
