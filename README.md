pip install streamlit |
streamlit run app.py

# Password Complexity Checker with Streamlit

This user-friendly Streamlit application empowers you to evaluate the strength of your passwords based on various criteria, helping you create more secure login credentials.

## Key Features

* **Strength Assessment:** Analyzes your password against essential factors like lowercase, uppercase, numeric, whitespace, and special characters.
* **Detailed Feedback:** Provides a breakdown of character types and assigns a strength score (1-5) with a corresponding remark (e.g., "Very Bad" or "Excellent").
* **Criteria Explanation:** Offers a clear explanation of the criteria used for password evaluation, aiding in understanding and improvement.
* **Intuitive Interface:** Leverages Streamlit for a clean and interactive experience, making password strength checks effortless.

## How it Works

1. **Launch the Application:** Ensure you have Python (version 3.6 or later) and Streamlit installed. Execute `pip install python streamlit` if necessary. Then, navigate to the directory containing the Python script (`main.py`) and run it using `python main.py`.
2. **Enter Your Password:** In the designated text field, securely enter your password (characters will be hidden while typing).
3. **Check Password Strength:** Click the "Check Password" button to initiate the evaluation.
4. **Analyze Results:** If you entered a password, you'll see a detailed breakdown highlighting the number of characters in each category (lowercase, uppercase, etc.), the calculated strength score, and a remark indicating the overall password security.
5. **Learn More (Optional):** Click the "Learn" button to access a section explaining the different criteria considered for password strength assessment. This knowledge can help you create stronger and more secure passwords in the future.

## Usage Example

1. Open the application and enter a password in the text field (e.g., "password123").
2. Click "Check Password."
3. Observe the results: You might see something like:
