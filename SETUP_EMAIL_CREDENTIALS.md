# 📧 Email Setup - Quick Guide

## ⚠️ ACTION REQUIRED: Add Your Email Credentials

Email sending is **ENABLED by default** but requires your Gmail credentials to work.

## Quick Setup (2 minutes)

### Step 1: Get Gmail App Password

1. Go to: **https://myaccount.google.com/apppasswords**
2. Sign in to your Google account
3. Click **"Select app"** → Choose **"Mail"**
4. Click **"Select device"** → Choose **"Other"** → Type **"GoodFoods"**
5. Click **"Generate"**
6. Copy the 16-character password (looks like: `abcd efgh ijkl mnop`)

### Step 2: Update backend/.env

Open `backend/.env` and replace these lines:

```env
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password_here
SMTP_FROM_EMAIL=your_email@gmail.com
```

With your actual credentials:

```env
SMTP_USER=yourname@gmail.com
SMTP_PASSWORD=abcd efgh ijkl mnop
SMTP_FROM_EMAIL=yourname@gmail.com
```

### Step 3: Restart Backend

```bash
cd backend
python run.py
```

### Step 4: Test

Make a reservation and check your email inbox! 📬

---

## What Happens If You Don't Configure Email?

If you don't add your credentials:
- ✅ Reservations still work perfectly
- ✅ Confirmation shown on screen
- ✅ Booking ID provided
- ⚠️ Email won't be sent (logged as warning)
- ✅ No errors or crashes

The system is designed to work with or without email!

---

## Alternative: Disable Email

If you don't want to use email at all, set in `backend/.env`:

```env
SMTP_ENABLED=false
```

---

## Email Template Preview

When configured, users receive a beautiful HTML email with:
- 🎨 GoodFoods branding
- 🎫 Booking ID
- 📍 Restaurant details
- 📅 Date and time
- 👥 Party size
- 📝 Special notes
- ℹ️ Important reminders

---

## Troubleshooting

### "Authentication failed"
- Make sure you're using an **App Password**, not your regular Gmail password
- App passwords are 16 characters with spaces: `abcd efgh ijkl mnop`

### "Email not received"
- Check spam/junk folder
- Verify email address is correct
- Check backend terminal for error messages

### "Module not found: aiosmtplib"
```bash
cd backend
pip install -r requirements.txt
```

---

## For Demo/Testing

**Option 1: Use Your Gmail** (Recommended)
- Takes 2 minutes to setup
- Shows full production experience
- Emails actually sent

**Option 2: Skip Email Setup**
- System works perfectly without it
- Confirmation shown on screen
- Good for quick demo

---

## Security Note

⚠️ **Never commit your `.env` file with real credentials to Git!**

The `.env` file is already in `.gitignore` to protect your credentials.

---

**Need help?** Check `backend/EMAIL_SETUP.md` for detailed instructions.
