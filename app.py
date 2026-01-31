import streamlit as st
from email_service import send_email


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Email Sender App",
    page_icon="📧",
    layout="centered"
)


# --------------------------------------------------
# App Title
# --------------------------------------------------
st.title("📧 Simple Email Sender")
st.markdown(
    "Send emails directly from a web interface using **Python + Gmail SMTP**."
)

st.divider()


# --------------------------------------------------
# Secrets (Secure)
# --------------------------------------------------
try:
    EMAIL_SENDER = st.secrets["EMAIL_SENDER"]
    EMAIL_PASSWORD = st.secrets["EMAIL_PASSWORD"]
except KeyError:
    st.error("Email credentials not found in secrets.")
    st.stop()


# --------------------------------------------------
# Input Form
# --------------------------------------------------
with st.form("email_form"):
    receiver = st.text_input("Receiver Email")
    subject = st.text_input("Subject")
    body = st.text_area("Email Body", height=150)

    submit = st.form_submit_button("🚀 Send Email")


# --------------------------------------------------
# Send Email Logic
# --------------------------------------------------
if submit:
    if not receiver or not subject or not body:
        st.warning("Please fill in all fields.")
    else:
        try:
            send_email(
                sender=EMAIL_SENDER,
                password=EMAIL_PASSWORD,
                receiver=receiver,
                subject=subject,
                body=body
            )
            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"Failed to send email: {e}")

