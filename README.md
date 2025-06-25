# stripe_key_finder


🏃‍♂️ How to Run It
Save as stripe_key_finder.py.

Install dependencies:


pip install requests
Make executable:

b
chmod +x stripe_key_finder.py
Run scan:


./stripe_key_finder.py ~/projects/myapp
Output example:

swift

[VALID] sk_live... – found at /home/user/myapp/.env:5
[INVALID] sk_live_12345... – found at /home/user/other/script.js:42
