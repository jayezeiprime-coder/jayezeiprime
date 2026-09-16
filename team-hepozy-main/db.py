from supabase import create_client, Client

SUPABASE_URL = "https://ptqrlqukrpluzospayyh.supabase.co"

SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB0cXJscXVrcnBsdXpvc3BheXloIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4OTQ4NDMwMiwiZXhwIjoyMTA1MDYwMzAyfQ.qWKW8vpOUyT-U2kNqvV8CIbYYq_i1crF5gZ6pNS2W0U"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


