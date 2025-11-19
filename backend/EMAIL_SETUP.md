# Email Setup Guide

Email confirmation functionality has been added to the GoodFoods reservation system. Follow these steps to enable it.

## Current Status

- ✅ Email service implemented
- ✅ Integrated with reservation creation
- ⚠️ **Disabled by default** (SMTP_ENABLED=false)
- ✅ System works perfectly without emails (for demo purposes)

## How It Works

When a reservation is created:
1. Reservation is saved to database
2. Booking ID is generated
3. **If SMTP is enabled**: Beautiful HTML confirmation email is sent
4. **If SMTP is disabled**: Email is logged but not sent (current behavior)
5. User sees confirmation on screen regardless

## To Enable Email Sending

### Option 1: Gmail (Easiest for Testing)

#### Step 1: Get Gmail App Password

1. Go to: https://myaccount.google.com/apppasswords
2. Sign in to your Google account
3. Click "Select app" → Choose "Mail"
4. Click "Select device" → Choose "Other" → Type "GoodFoods"
5. Click "Generate"
6. Copy the 16-character password (e.g., `abcd efgh ijkl mnop`)

#### Step 2: Update backend/.env

```env
SMTP_ENABLED=true
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=abcd efgh ijkl mnop
SMTP_FROM_EMAIL=your_email@gmail.com
SMTP_FROM_NAME=GoodFoods Reservations
```

#### Step 3: Install Dependency (if not already installed)

```bash
cd backend
pip install aiosmtplib==3.0.2
```

#### Step 4: Restart Backend

```bash
python run.py
```

#### Step 5: Test

Make a reservation and check your email!

---

### Option 2: Outlook/Hotmail

```env
SMTP_ENABLED=true
SMTP_HOST=smtp-mail.outlook.com
SMTP_PORT=587
SMTP_USER=your_email@outlook.com
SMTP_PASSWORD=your_password
SMTP_FROM_EMAIL=your_email@outlook.com
SMTP_FROM_NAME=GoodFoods Reservations
```

---

### Option 3: Custom SMTP Server

```env
SMTP_ENABLED=true
SMTP_HOST=your_smtp_host.com
SMTP_PORT=587
SMTP_USER=your_username
SMTP_PASSWORD=your_password
SMTP_FROM_EMAIL=noreply@yourdomain.com
SMTP_FROM_NAME=GoodFoods Reservations
```

---

## Email Template

The confirmation email includes:
- ✅ Beautiful HTML design with GoodFoods branding
- ✅ Booking ID prominently displayed
- ✅ Restaurant name
- ✅ Date and time (formatted nicely)
- ✅ Party size
- ✅ Special notes (if provided)
- ✅ Important reminders
- ✅ Professional footer

## Testing Email

### Test with Real Booking

1. Enable SMTP in `.env`
2. Restart backend
3. Make a reservation through the UI
4. Check your email inbox

### Test Programmatically

```bash
cd backend
python -c "
from app.services.email_service import email_service
import asyncio

async def test():
    result = await email_service.send_reservation_confirmation(
        to_email='your_email@example.com',
        to_name='Test User',
        booking_id='TEST-123',
        venue_name='Test Restaurant',
        reservation_datetime='2024-12-25T19:00:00',
        party_size=4,
        notes='Window seat please'
    )
    print('Email sent!' if result else 'Email failed')

asyncio.run(test())
"
```

## Troubleshooting

### "Authentication failed"
- **Gmail**: Make sure you're using an App Password, not your regular password
- **Outlook**: Check if 2FA is enabled, may need app-specific password
- Verify username and password are correct

### "Connection refused"
- Check SMTP_HOST and SMTP_PORT are correct
- Verify firewall isn't blocking port 587
- Try port 465 with SSL instead

### "Email not received"
- Check spam/junk folder
- Verify recipient email is correct
- Check email service logs in backend terminal

### "Module not found: aiosmtplib"
```bash
cd backend
pip install aiosmtplib==3.0.2
```

## For Demo/Submission

**You don't need to enable emails for the challenge submission.**

The system works perfectly without emails:
- ✅ Reservations are created
- ✅ Saved to database
- ✅ Confirmation shown on screen
- ✅ Booking ID provided
- ✅ Can be verified in backend

Email is a **bonus feature** that shows production-readiness.

## Security Notes

- ⚠️ Never commit `.env` file with real credentials to Git
- ⚠️ Use App Passwords, not regular passwords
- ⚠️ For production, use dedicated email service (SendGrid, AWS SES)
- ⚠️ Current implementation is for demo/development only

## Production Recommendations

For production deployment:
1. Use SendGrid, AWS SES, or Mailgun (more reliable)
2. Implement email queue (Celery, Redis)
3. Add retry logic for failed emails
4. Track email delivery status
5. Add unsubscribe functionality
6. Use email templates from database

## Summary

- ✅ Email functionality is implemented
- ✅ Disabled by default (SMTP_ENABLED=false)
- ✅ Easy to enable (just update .env)
- ✅ Beautiful HTML email template
- ✅ Graceful fallback if email fails
- ✅ System works perfectly without it

**To enable**: Set `SMTP_ENABLED=true` and configure SMTP settings in `backend/.env`
