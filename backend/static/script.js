async function uploadImage() {
    const fileInput = document.getElementById("upload");
    if (!fileInput.files.length) {
        alert("이미지를 선택하세요!");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("http://localhost:8000/upload/", {
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
        const box = document.createElement("div");
        box.className = "color-box";
        box.style.backgroundColor = color;
        box.textContent = color;  // HEX 코드 표시
        resultDiv.appendChild(box);
    });
}
