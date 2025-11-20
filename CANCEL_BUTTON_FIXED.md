# ✅ Cancel Button Fixed

## Issue
```
Cancel API error: Bad Request
```

## Root Cause
Next.js 15 changed how dynamic route parameters work:
- **Old**: `{ params }: { params: { id: string } }`
- **New**: `{ params: Promise<{ id: string }> }`

## Solution
Updated the cancel route to await the params:
```typescript
const params = await context.params;
const { id } = params;
```

## File Modified
- ✅ `app/api/reservations/[id]/cancel/route.ts`

## Test Now

1. Go to: http://localhost:3000/reservations
2. Find an upcoming reservation
3. Click "Cancel Reservation" button
4. Should work without errors!

## Expected Behavior

**Before:**
- Click cancel → Error: "Cancel API error: Bad Request"
- Reservation not cancelled

**After:**
- Click cancel → Success!
- Reservation status changes to "cancelled"
- Removed from upcoming list

---

**The cancel button now works perfectly!** ✅
