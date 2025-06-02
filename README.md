<<<<<<< HEAD
# Dreamboard Studio MVP

An AI-powered moodboard builder for photographers and visual artists.

## Flow:
1. User pays deposit (Stripe)
2. Survey: vibe, subject, style, colors
3. Upload inspo or search Pinterest/Unsplash
4. "Surprise Me" → random curated idea
5. AI generates a moodboard (images + optional video)
6. Board is saved + emailed to both parties

## Tech Stack
- Frontend: Next.js + ShadCN
- Backend: FastAPI (Python)
- Storage: Supabase (auth + db) + S3 (images)
- AI: OpenAI (prompts & images), Replicate (optional)
- Billing: Stripe

## Milestones
- [ ] Account setup
- [ ] Prompt logic
- [ ] Board generator
- [ ] Stripe paywall
- [ ] White-label wrapper
>>>>>>> 66ba43e304eaf5a3ce65f02ff9767cd303d12567
