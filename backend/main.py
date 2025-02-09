import os
import uvicorn
from fastapi import FastAPI, File, UploadFile
import io
from PIL import Image
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.color_utils import extract_colors
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🚀 `static` 폴더의 절대 경로를 지정 (Render 배포 환경에서도 정상 동작)
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
print(f"📂 Static directory path: {static_dir}")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 (HTML/JS) 제공
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def home():
    """index.html 변환"""
    return FileResponse(os.path.join(static_dir, "index.html"))

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """사용자가 업로드한 이미지를 받아서 색상 추출"""
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    colors = extract_colors(image)
    return {"colors": colors}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
