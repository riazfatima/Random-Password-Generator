**Created by: Fatima Riaz**

# Random Password Generator

**Random Password Generator** is a lightweight, secure, and easy-to-use Python script that generates strong random passwords instantly. Built with Python's standard library, this tool requires no external dependencies and works on any platform with Python 3.6+ installed.

## Why use this password generator?

In today's digital world, weak passwords are one of the biggest security risks. Many people still use simple passwords like "password123" or "qwerty" across multiple accounts. This tool solves that problem by generating truly random passwords that are:

- **Unpredictable** - Uses random character selection from a pool of 94 characters
- **Complex** - Includes uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and symbols (!@#$% etc.)
- **Customizable** - Change length easily by modifying a single variable
- **Instant** - Generates passwords in milliseconds (<0.001 seconds)
- **Secure** - High entropy with 94^12 ≈ 475 septillion combinations (for 12-character passwords)

## What makes it different?

Unlike online password generators that could potentially log your passwords, this script runs entirely on your local machine. No data is sent anywhere. You have complete control over the generation process. Plus, the code is simple and transparent - you can see exactly how your password is being generated.

## Perfect for:

- Creating strong passwords for new online accounts
- Generating temporary passwords for employees or users
- Bulk password generation for software testing
- Learning Python's random and string modules
- Quick, offline password generation without internet
- Understanding ASCII character encoding and its role in computing

## One line of code. Infinite possibilities.

The core generation logic is just one line of Python code using list comprehension, making it both elegant and efficient:

```python
result = "".join([random.choice(char_values) for i in range(pass_len)])
