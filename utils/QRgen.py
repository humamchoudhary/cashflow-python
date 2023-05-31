import qrcode
import base64
from io import BytesIO


def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_code_img = qr.make_image(fill_color="black", back_color="white")

    stream = BytesIO()
    qr_code_img.save(stream)
    qr_code_bytes = stream.getvalue()
    qr_code_base64 = base64.b64encode(qr_code_bytes).decode("utf-8")

    return qr_code_base64

