from fastapi import UploadFile, File
from s3_client import upload_file

@app.post("/upload-test")
async def upload_test(file: UploadFile = File(...)):
    local_path = f"/tmp/{file.filename}"
    with open(local_path, "wb") as f:
        f.write(await file.read())
    url = upload_file(local_path, f"uploads/{file.filename}")
    return {"url": url}

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
