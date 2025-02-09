const API_URL = "https://my-fastapi.onrender.com";

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("upload").addEventListener("change", function(event) {
        let fileName;
        fileName = event.target.files.length > 0 ? event.target.files[0].name : "📂 파일 선택";
        document.getElementById("upload-label").textContent = fileName;
    });
});

async function uploadImage() {
    const fileInput = document.getElementById("upload");
    if (!fileInput.files.length) {
        alert("이미지를 선택하세요!");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("${API_URL}/upload/", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    displayColors(data.colors);
}

function displayColors(colors) {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = ""; // 기존 색상 목록 초기화

    colors.forEach(color => {
        const colorBox = document.createElement("div");
        colorBox.className = "color-box";
        colorBox.style.backgroundColor = color;
        colorBox.textContent = color;  // HEX 코드 표시

        // ✅ 밝기 확인하여 텍스트 색상 자동 조정
        if (isLightColor(color)) {
            colorBox.classList.add("light");
        } else {
            colorBox.classList.add("dark");
        }

        // ✅ 클릭하면 HEX 코드 복사 기능 추가
        colorBox.onclick = function () {
            navigator.clipboard.writeText(color).then(() => {
                alert(`색상 ${color}이(가) 복사되었습니다!`);
            });
        };

        resultDiv.appendChild(colorBox);
    });
}

// HEX 코드 밝기 계산하여 텍스트 색상 조정
function isLightColor(hex) {
    const rgb = hex.match(/\w\w/g).map(x => parseInt(x, 16));
    const brightness = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000;
    return brightness > 128;
}
