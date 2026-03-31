import streamlit as st
import qrcode
from PIL import Image
import os

# Title
st.title("🔳 QR Code Generator")
st.write("Generate and download your QR code easily")

# Inputs
text = st.text_input("Enter Text / URL")
file_name = st.text_input("Enter File Name", "qr_code")
size = st.slider("Select Size (1–40)", 1, 40, 5)

# Generate Button
if st.button("Generate QR Code"):
    if text == "":
        st.error("⚠️ Please enter text or URL")
    else:
        # Create QR Code
        qr = qrcode.QRCode(
            version=size,
            box_size=10,
            border=5
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")

        # Save file
        file_path = f"{file_name}.png"
        img.save(file_path)

        # Show image
        st.image(img, caption="Generated QR Code", use_column_width=True)

        # Download button
        with open(file_path, "rb") as file:
            st.download_button(
                label="📥 Download QR Code",
                data=file,
                file_name=file_path,
                mime="image/png"
            )

        st.success("✅ QR Code generated successfully!")
