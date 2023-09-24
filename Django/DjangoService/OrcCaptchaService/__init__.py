
import requests
class OrcCaptcha():
    def ImgtoText(base64, engine: int=1):
        url = 'https://api8.ocr.space/parse/image'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Apikey': 'K89411999788957',
            'Origin': 'https://ocr.space',
            'Referer': 'https://ocr.space/',
            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
        }
        data = {
            'url': '',  # Set the image URL if you want to provide an image URL
            'language': 'eng',
            'isOverlayRequired': True,
            'FileType': '.Auto',
            'base64Image': base64,
            'IsCreateSearchablePDF': False,
            'isSearchablePdfHideTextLayer': True,
            'detectOrientation': False,
            'isTable': False,
            'scale': True,
            'OCREngine': engine,  # Change OCREngine value if needed
            'detectCheckbox': False,
            'checkboxTemplate': 0
        }
        response = requests.post(url, headers=headers, data=data)
        print(response.json())
        if "TextOverlay" in str(response.text):
            if len(response.json()["ParsedResults"][0]["TextOverlay"]["Lines"]) > 0:
                result = response.json()["ParsedResults"][0]["TextOverlay"]["Lines"][0]["LineText"]
                return result
        return ""
     


# OrcCaptcha.ImgtoText(base64="data:image/png;base64,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")