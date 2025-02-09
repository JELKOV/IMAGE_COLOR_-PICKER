import numpy as np # 이미지를 숫자 배열로 변환
import cv2 # 이미지 처리를 위한 라이브러리
from collections import Counter # 색상의 빈도를 계산
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

    # 픽셀을 (R,G,B) 형태로 변환
    pixels = img_array.reshape(-1, 3)

    # 색상 카운트 (빈도가 높은 색상 찾기)
    color_counts = Counter(map(tuple, pixels))
    most_common_colors = color_counts.most_common(num_colors)

    # RGB -> HEX 변환
    hex_colors = [rgb_to_hex(color[0]) for color in most_common_colors]
    return hex_colors