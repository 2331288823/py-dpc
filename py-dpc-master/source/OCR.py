import pytesseract
import PIL

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def character_recognition(image_address: str) -> list:
    # 打开图片
    image = PIL.Image.open(image_address)
    # 图片识别
    data = pytesseract.image_to_string(image, lang='chi_sim')
    # 字符串转列表
    img_list = data.split("\n")
    return img_list
