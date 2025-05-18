# captcha_recognition.py
# @author 赖有洲
# @description 
# @created 2024/11/21 15:51
# @last-modified 2024/11/21 15:51

from PIL import Image, ImageFilter
import ddddocr
import io


class CaptchaRecognition:

    @classmethod
    def recognize_captcha(cls, image_path):
        """
        识别验证码，包含预处理和识别步骤。
        """
        ocr = ddddocr.DdddOcr(show_ad=False)

        # 预处理图像，灰度化和去噪。
        image = Image.open(image_path)
        # 转换为灰度图像
        image = image.convert('L')
        # 去噪处理
        image = image.filter(ImageFilter.MedianFilter())

        # 将处理后的图像转换为二进制格式
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        # 调用 ddddocr 进行识别
        result = ocr.classification(img_bytes)
        return result


# test code
if __name__ == "__main__":
    # 本地图像测试
    image_path = r"C:\Users\admin\Desktop\captcha.png"
    result = CaptchaRecognition.recognize_captcha(image_path)
    print(result, type(result))
