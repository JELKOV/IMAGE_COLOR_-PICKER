# IMAGE COLOR PICKER

## 프로젝트 개요
IMAGE COLOR PICKER는 사용자가 이미지를 업로드하면 주요 색상을 추출해주는 웹 애플리케이션입니다. FastAPI 백엔드와 HTML/CSS/JavaScript 기반의 프론트엔드를 사용하여 구현되었습니다.

## 기술 스택
- **프론트엔드**: HTML, CSS, JavaScript
- **백엔드**: FastAPI (Python)
- **데이터 처리**: Pillow, NumPy, scikit-learn
- **서버 배포**: Render (백엔드 + 정적 파일 배포)

## 프로젝트 구조
```
IMAGE_COLOR_PICKER/
│── backend/            # 백엔드 FastAPI 서버 코드
│   ├── main.py         # FastAPI 서버 실행 코드
│   ├── color_utils.py  # 색상 추출 로직
│── static/             # 정적 파일 (HTML, CSS, JS)
│   ├── index.html      # 메인 페이지
│   ├── styles.css      # 스타일시트
│   ├── script.js       # 클라이언트 로직
│── requirements.txt    # 프로젝트 의존성 목록
│── README.md           # 프로젝트 설명 문서
```

## 🚀 배포

본 프로젝트는 **Render**를 통해 배포되었습니다.

🔗 **배포된 서비스 URL**: [배포사이트 링크](https://image-color-picker-gv37.onrender.com/)

## 💡 기능

- **이미지 업로드**: 사용자가 이미지를 업로드하면 색상 분석을 진행합니다.
- **색상 추출**: K-Means 클러스터링을 활용하여 주요 색상을 분석합니다.
- **FastAPI 기반 백엔드**: 이미지 처리를 위한 API를 제공합니다.
- **JS + HTML 프론트엔드**: 간단한 인터페이스를 통해 사용자 경험을 제공합니다.

## 🛠️ 기술 스택

- **프론트엔드**: HTML, CSS, JavaScript
- **백엔드**: FastAPI, Uvicorn
- **이미지 처리**: Pillow
- **머신러닝 알고리즘**: Scikit-learn (K-Means 사용)
- **배포**: Render

## 📜 사용법

1. 웹페이지에서 **파일 선택 버튼**을 클릭하여 이미지를 업로드합니다.
2. "색상 추출" 버튼을 누르면 대표 색상이 추출됩니다.
3. 추출된 색상 정보가 화면에 표시됩니다.

## API 엔드포인트
| Method | Endpoint | 설명 |
|--------|---------|------|
| `GET`  | `/` | 메인 페이지 (`index.html`) 반환 |
| `POST` | `/upload/` | 이미지 업로드 후 색상 추출 |

## 🔧 로컬 실행 방법

1. 저장소 클론
   ```bash
   git clone https://github.com/JELKOV/IMAGE_COLOR_PICKER.git
   cd IMAGE_COLOR_PICKER
   ```
2. 가상환경 생성 및 패키지 설치
   ```bash
   python -m venv venv
   source venv/bin/activate  # (Windows에서는 `venv\Scripts\activate`)
   pip install -r backend/requirements.txt
   ```
3. 서버 실행
   ```bash
   uvicorn backend.main:app --reload
   ```
4. 브라우저에서 `http://127.0.0.1:8000/` 접속

## 👨‍💻 제작자

- GitHub: [JELKOV](https://github.com/JELKOV)

---

필요한 수정 사항이 있으면 언제든지 알려주세요! 🚀

