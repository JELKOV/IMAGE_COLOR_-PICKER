import numpy as np # 이미지를 숫자 배열로 변환
from sklearn.cluster import KMeans # scikit-learn의 KMeans를 활용
from PIL import Image # 이미지를 읽고 RGB로 변환

'''
color_utils -> 색상 분석 유틸
'''

def rgb_to_hex(rgb):
    """RGB 색상을 HEX 코드로 변환"""
    # {:02x}는 숫자를 2자리 16진수(HEX 코드)로 변환하는 포맷
    # 0, 0, 255 (파란색) → #0000FF 로 변환됨
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def extract_colors(image: Image, num_colors=10):
    """이미지에서 가장 많이 사용된 색상 추출"""
    image = image.convert("RGB") # RGB 모드로 변환
    img_array = np.array(image) # 이미지를 Numpy 배열로 변환

    # 크기 조정 (너비 또는 높이가 300px을 넘지 않도록 리사이징)
    image.thumbnail((300, 300))

    # 픽셀을 (R,G,B) 형태로 변환
    pixels = img_array.reshape(-1, 3)

    # k-means 클러스터링 적용
    kmeans = KMeans(n_clusters=num_colors, random_state=0, n_init=10)
    kmeans.fit(pixels)

    # 중심 색상 추출 후 HEX로 변환
    hex_colors = [rgb_to_hex(color) for color in kmeans.cluster_centers_.astype(int)]
    return hex_colors