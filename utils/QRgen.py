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
    img = qr.make_image(fill_color="black", back_color="white")
    qr_code_img.save("test.png")

    qr_code_bytes = stream.getvalue()

    return base64.b64encode(qr_code_bytes)


# # Example dictionary to store in the QR code
# data_dict = {"destination": "humamch2", "dest_type": "Inter Bank"}

# # Convert the dictionary to a string
# data_string = str(data_dict)

# # Generate the QR code image
# qr_code_image = generate_qr_code(data_dict)
# print(qr_code_image)

# qr_code_base64 = base64.b64encode(qr_code_image.tobytes()).decode("utf-8")

# # Create a JSON object to store the QR code
