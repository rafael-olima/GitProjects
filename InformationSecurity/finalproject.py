import random
import streamlit as st
from basic.RSA import myRSA
from basic.Encryption import myEncryption

if __name__ == "__main__":

    if 'rsa' not in st.session_state or 'enc' not in st.session_state:
        # Object that manage the public and private keys.
        st.session_state['rsa'] = myRSA()
        # Stores the object to encrypt and decrypt in the session.
        # Take the public and private keys as arguments.
        st.session_state['enc'] = myEncryption(st.session_state['rsa'].get_private_key(), st.session_state['rsa'].get_public_key())

    # Menu
    st.sidebar.title('Sender')
    st.sidebar.write('Select your file to encrypt or decrypt')
    uploaded_file = st.sidebar.file_uploader('Select the file', type=['txt', 'csv'])

    # Verify if the file was uploaded and store the content.
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.session_state['file_contents'] = file_contents

    if st.sidebar.button("Encrypt File"):
        st.session_state['cipher'] = st.session_state['enc'].encrypt_file(st.session_state['file_contents'])
        st.write("Encrypted content\n")
        st.write(str(st.session_state['cipher']))

    if st.sidebar.button("Generate Hash"):
        st.session_state['hash'] = st.session_state['enc'].generate_hash(st.session_state['file_contents'])
        st.write(st.session_state['hash'])

    # Optional action to modify the generated hash
    if st.sidebar.button("Shuffle Hash (Optional)"):
        prev = st.session_state['hash']
        lst = list(prev)
        random.shuffle(lst)
        st.session_state['hash'] = "".join(lst)
        st.write("Previous hash")
        st.write(prev)
        st.write("Modified hash")
        st.write(st.session_state['hash'])

    st.sidebar.title('Recipient')

    if st.sidebar.button("Decrypt File"):
        st.session_state['original'] = st.session_state['enc'].decrypt_file(st.session_state['cipher'])
        str_msg = str(st.session_state['original'],encoding='utf-8')
        st.write(str_msg)

    if st.sidebar.button("Verify Hash"):
        st.write("Hash OK ?")
        verify = st.session_state['enc'].verify_hash(st.session_state['hash'], st.session_state['file_contents'])
        st.write(verify)
