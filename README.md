# Word to Digits Converter

## Overview
This project was inspired by a challenge from a friend (@oladayotech) to convert word numbers into digits using Python. It pushed me to explore number formatting for large values such as millions, billions, and trillions for better readability. Additionally, I learned how using multiplication logic simplifies the process compared to creating a dictionary for every possible number up to a trillion.

## What This Code Does
The Word to Digits Converter is a Python program that:
- Converts word-based numbers (e.g., "two hundred thousand") into their digit equivalents (e.g., "200,000").
- Handles numbers ranging from single digits to trillions.
- Formats large numbers with commas for improved readability (e.g., "2000000" becomes "2,000,000").
- Provides a user-friendly way to enter word numbers and get the corresponding digit value.

### Key Features:
1. **Base Numbers:** Recognizes numbers like "one," "two," etc.
2. **Tens:** Handles numbers like "twenty," "thirty," etc.


## How to Use
1. Run the script in a Python environment or on Google Colab.
2. The program will prompt you to input a word number (e.g., "two hundred thousand").
3. The digit equivalent will be displayed in the console. For example:
   - Input: `two hundred thousand`
   - Output: `200,000`

### Example Outputs:
| Input                  | Output    |
|------------------------|-----------|
| "two"                 | 2         |
| "twenty"              | 20        |
| "two hundred"         | 200       |
| "two thousand"        | 2,000     |
| "one million"         | 1,000,000 |
| "two billion three"   | 2,000,000,003 |

## How to Play
Try it here on: [Google Colab](https://tinyurl.com/gaji-word-to-digit-converter)

1. Click on the link to open the Colab notebook.
2. Run the notebook and follow the on-screen instructions to input word numbers.

3. Enjoy converting words to digits with ease!


## Lessons Learned
- **Number Formatting:** I learned how to use Python’s f-strings with the `:,` specifier to format large numbers for readability.
- **Simplified Logic:** Multiplication logic proved to be a more efficient and scalable approach compared to creating a dictionary for all possible numbers up to a trillion.
- **String Manipulation:** Working with string inputs and splitting them into parts enhanced my understanding of text processing in Python.

---
Feel free to use and modify the code as needed! Contributions and feedback are welcome.

