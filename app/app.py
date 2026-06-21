import streamlit as st

st.set_page_config(
    page_title="Blood Smear Screening",
    layout="wide"
)

st.title(
    "🩸 Low-Cost AI Blood Smear Screening"
)

uploaded_file = st.file_uploader(
    "Upload Blood Smear Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(
        uploaded_file,
        use_container_width=True
    )

    st.subheader("Pipeline Status")

    st.success("Image Uploaded")

    st.info("Preprocessing Ready")

    st.info("Segmentation Pending")

    st.info("Morphology Pending")

    st.info("Screening Pending")

    st.subheader("Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Healthy Cells", "--")

    with col2:
        st.metric("Abnormal Cells", "--")

    st.warning(
        "Awaiting Analysis"
    )