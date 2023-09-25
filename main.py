'''import as qr
img = qr.make("https://www.youtube.com/channel/UCre1LhxAra5iHuB0cAt3v1A")
img.save("iota_spiting_facts.png")'''

import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, error_correction= qrcode.constants.ERROR_CORRECT_H,box_size=10, border=3)
qr.add_data("https://www.instagram.com/nidhi.saxena.98/")
qr.make(fit=True)
img = qr.make_image(fill_color = "blue", back_color ="pink")
img.save("insta_scan.png")

