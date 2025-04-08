# User Registration and Login System

## Description

This is a simple Python program that allows users to:
1. Create an account with a username and password
2. Login using their credentials

The program includes validation for both username and password to ensure they meet specific requirements.

## Features

### Account Creation
- Username must be exactly 5 characters long
- Password must be:
  - Exactly 6 characters long
  - Contain at least one digit
  - Contain at least one lowercase letter
  - Contain at least one uppercase letter

### Login System
- Users can login with their previously created credentials
- System verifies if the entered username and password match the stored credentials

## How to Use

1. Run the program
2. When prompted, choose whether to create an account by entering "yes" or "no"
3. If creating an account:
   - Enter a username that is exactly 5 characters long
   - Enter a password that meets all requirements
4. After account creation, you'll be prompted to login with your new credentials
5. If credentials match, you'll see a success message

## Requirements

- Python 3.x

## Usage Example

```
Welcome to User Registration System
do you want to make an account(yes/no) : yes
enter username : Alice
enter password 6 character long : Pass1
account successfully created
Enter username: Alice
Enter password: Pass1
Hi Alice you are logged in.
```

## Notes

- The program stores credentials only during the current session
- All password requirements must be met for successful account creation
- Username is case-sensitive during login
