from fastapi import FastAPI
from supabase_client import supabase

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Dreamboard API is live!"}

@app.post("/seed-vibe")
def seed_vibe():
    data = {
        "title": "Sunlit Jazz Club",
        "description": "Soft light, smoky bar, golden brass instruments and timeless warmth",
        "tags": ["jazz", "warm", "golden", "retro"],
        "source": "curated"
    }
    res = supabase.table("vibe_prompts").insert(data).execute()
    return {"status": "inserted", "response": res.data}
