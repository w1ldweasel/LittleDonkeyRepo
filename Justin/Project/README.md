# PASSWORD STRENGTH ASSESSOR

The traditional approach to assessing the strength of a password is to apply arbitrary rules about the length and character choice of passwords. This naively increases password entropy by limiting the options for low entropy passwords. It does however lead to patterns in how passwords are formed with simple rules often applied to fit the character limitations such as adding a number (password1) and common text exchanges (pa55word).

The intention of this project is to take lists of common passwords, understand what makes them tick and then assess new password against these newfound rules.

For this, I'll be using the alleged-gmail-passwords.txt list availble from here:
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/alleged-gmail-passwords.txt

The adobe 100 list is being used for development (much smaller dataset)