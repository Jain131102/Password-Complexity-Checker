import string
import streamlit as st

def check_pwd(password):
    """
    Checks the strength of a given password based on various criteria.

    Args:
        password (str): The password to be checked.

    Returns:
        tuple: A tuple containing the following information:
            - lower_count: Number of lowercase characters.
            - upper_count: Number of uppercase characters.
            - num_count: Number of numeric characters.
            - wspace_count: Number of whitespace characters.
            - special_count: Number of special characters.
            - strength: Overall password strength (1-5).
            - remarks: A descriptive remark about the password strength.
    """
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    # Calculate strength based on character types
    strength += 1 if lower_count >= 1 else 0
    strength += 1 if upper_count >= 1 else 0
    strength += 1 if num_count >= 1 else 0
    strength += 1 if wspace_count >= 1 else 0
    strength += 1 if special_count >= 1 else 0

    # Assign remarks based on strength
    if strength == 1:
        remarks = "Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength == 3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    return lower_count, upper_count, num_count, wspace_count, special_count, strength, remarks

def display_criteria():
    """Displays the criteria for password strength evaluation."""
    st.write("""
        ### What Is This App About?

        This Password Complexity Checker helps you assess the strength of your password based on several criteria. 

        **Criteria for Judging Your Password:**
        - **Lowercase characters**: Presence of letters like a, b, c, etc.
        - **Uppercase characters**: Presence of letters like A, B, C, etc.
        - **Numeric characters**: Presence of numbers like 1, 2, 3, etc.
        - **Whitespace characters**: Presence of spaces.
        - **Special characters**: Presence of symbols like !, @, #, etc.

        **How We Determine Strength:**
        - **1 Point**: Very Bad Password! Immediate change recommended.
        - **2 Points**: Not Good Enough! Needs improvement.
        - **3 Points**: Weak Password. Consider making it more complex.
        - **4 Points**: Strong Password, but there’s room for improvement.
        - **5 Points**: Excellent Password! Well done.

        This app provides a simple way to ensure your passwords are strong and secure.
        """)

def main():
    """Main function to create the Streamlit app."""
    st.set_page_config(
        page_title="Password Complexity Checker",
        page_icon=":lock:",
        layout="wide"
    )

    st.title('Password Complexity Checker')

    st.write("""
        Welcome to the Password Complexity Checker! Use this tool to evaluate how strong your password is based on various factors.
        """)

    # Styling for the input and buttons
    st.markdown("""
        <style>
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 2px solid #4CAF50;
            padding: 12px;
            font-size: 18px;
        }
        .stButton>button {
            border-radius: 8px;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True)

    password = st.text_input("Enter Password:", type="password")

    # Layout for buttons
    col1, col2 = st.columns([3, 1])

    with col1:
        check = st.button('Check Password', use_container_width=True)
    with col2:
        learn = st.button('Learn', use_container_width=True)

    if check:
        if password:
            lower_count, upper_count, num_count, wspace_count, special_count, strength, remarks = check_pwd(password)
            st.write('### Your Password Analysis :')
            st.write(f"**Lowercase characters :** {lower_count}")
            st.write(f"**Uppercase characters :** {upper_count}")
            st.write(f"**Numeric characters :** {num_count}")
            st.write(f"**Whitespace characters :** {wspace_count}")
            st.write(f"**Special characters :** {special_count}")
            st.write(f"**Password Strength :** {strength}")
            st.write(f"**Hint :** {remarks}")
        else:
            st.write("Please enter a password to check its strength.")

    if learn:
        display_criteria()

if __name__ == '__main__':
    main()
