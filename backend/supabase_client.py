import os

print("SUPABASE_URL:", os.environ.get("SUPABASE_URL"))
print("SUPABASE_ANON_KEY:", os.environ.get("SUPABASE_ANON_KEY"))

from supabase import create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
