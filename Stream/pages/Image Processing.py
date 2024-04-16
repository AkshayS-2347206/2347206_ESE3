import streamlit as st
from PIL import Image

def main():
    st.title("Image Processing and Filtering")

    st.sidebar.header("Choose an Option")
    filter_option = st.sidebar.selectbox(
        "Filter",
        ["Original Image", "Grayscale", "Resize", "Rotate", "Crop"]
    )

    if filter_option in ["Resize", "Rotate"]:
        parameters = get_filter_parameters(filter_option)
    elif filter_option == "Crop":
        cropped_image = crop_image()
        st.image(cropped_image, caption="Cropped Image", use_column_width=True)
        return
    else:
        parameters = None

    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        pil_image = Image.open(uploaded_file)
        image = apply_filters(pil_image, filter_option, parameters)
        st.image(image, caption=filter_option, use_column_width=True)

def get_filter_parameters(filter_option):
    if filter_option == "Resize":
        width = st.sidebar.number_input("Enter Width", min_value=1)
        height = st.sidebar.number_input("Enter Height", min_value=1)
        return {"width": width, "height": height}
    elif filter_option == "Rotate":
        angle = st.sidebar.slider("Angle", min_value=0, max_value=360, value=0)
        return {"angle": angle}

def apply_filters(image, filter_option, parameters=None):
    if filter_option == "Original Image":
        return image
    elif filter_option == "Grayscale":
        return image.convert("L")
    elif filter_option == "Resize":
        return image.resize((parameters["width"], parameters["height"]))
    elif filter_option == "Rotate":
        return image.rotate(parameters["angle"], expand=True)

def crop_image():
    uploaded_file = st.sidebar.file_uploader("Upload an image to crop", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        pil_image = Image.open(uploaded_file)
        cropped_image = st.sidebar.st_cropper(pil_image)
        return cropped_image

if __name__ == "__main__":
    main()
