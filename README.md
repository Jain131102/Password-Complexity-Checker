# Password Complexity Checker

This user-friendly Streamlit application empowers you to evaluate the strength of your passwords based on various criteria, helping you create more secure login credentials.

## Features

* **Strength Assessment:** Analyzes your password against essential factors like lowercase, uppercase, numeric, whitespace, and special characters.
* **Detailed Feedback:** Provides a breakdown of character types and assigns a strength score (1-5) with a corresponding remark (e.g., "Very Bad" or "Excellent").
* **Criteria Explanation:** Offers a clear explanation of the criteria used for password evaluation, aiding in understanding and improvement.
* **Intuitive Interface:** Leverages Streamlit for a clean and interactive experience, making password strength checks effortless.

## How it Works

1. **Launch the Application:** 
Ensure you have Python (version 3.6 or later) and Streamlit installed. 
```bash
pip install python streamlit
```
Access the code for this app from your preferred source control system or download the files directly.
```bash
git clone https://github.com/Jain131102/Password-Complexity-Checker.git
``` 
Navigate to the directory containing the Python script nd execute it .
```bash
cd Password-Complexity-Checker
streamlit run app.py
```

2. **Enter Your Password:** In the designated text field, securely enter your password (characters will be hidden while typing).
3. **Check Password Strength:** Click the "Check Password" button to initiate the evaluation.
4. **Analyze Results:** If you entered a password, you'll see a detailed breakdown highlighting the number of characters in each category (lowercase, uppercase, etc.), the calculated strength score, and a remark indicating the overall password security.
5. **Learn More (Optional):** Click the "Learn" button to access a section explaining the different criteria considered for password strength assessment. This knowledge can help you create stronger and more secure passwords in the future.

## Usage Example

1. Open the application and enter a password in the text field (e.g., "password123").
2. Click "Check Password."
3. Observe the results: You might see something like:
```
Your Password Analysis:
Lowercase characters: 8
Uppercase characters: 0
Numeric characters: 3
Whitespace characters: 0
Special characters: 0
Password Strength: 2
Hint: Not good enough! Change ASAP
```

## Additional Notes

* This app prioritizes core password complexity evaluation. For enhanced security, consider using password managers and employing more intricate password creation methods.
* Basic CSS styling is included for a visually appealing interface. Feel free to customize it further for a more personalized experience.

Such Password Complexity Checker empowers you with valuable insights into strengthening your passwords and securing your online accounts

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

