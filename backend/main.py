from fastapi import FastAPI, File, UploadFile # 서버 프레임 라이브러리
import io # 바이너리 데이터를 이미지로 변환
from PIL import Image
from color_utils import extract_colors # 색상 추출 라이브러리 가져오기
from fastapi.middleware.cors import CORSMiddleware # JS에서 API 호출을 허용

app = FastAPI()

# CORS 설정 (JS에서 API 호출 가능하도록 허용)
# 이 설정을 하면 프론트엔드(HTML/JS)에서 백엔드(FastAPI) API를 호출할 수 있음.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (테스트용)
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """사용자가 업로드한 이미지를 받아서 색상 추출"""
    contents = await file.read() # 파일 읽기
    image = Image.open(io.BytesIO(contents)) # 바이너리 데이터
    colors = extract_colors(image) # 색상 추출 함수 실행
    return {"colors": colors} # JSON 변환
