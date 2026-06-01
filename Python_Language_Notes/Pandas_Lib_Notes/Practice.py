import pandas as pd
import bcrypt as bc

# Generating Hash-Salted Passwords
salt = bc.gensalt()
hashedPasswords = [
    bc.hashpw(b'Never', salt),
    bc.hashpw(b'Gonna', salt),
    bc.hashpw(b'Give', salt),
    bc.hashpw(b'You', salt),
    bc.hashpw(b'Up', salt),
]

# Generating the Data
data = {
    'Name': ['Joshua', 'Scott', 'Samantha', 'Erick', 'Matthew'],
    'DateOfBirth': ['5/12/2004', '12/4/1998', '8/9/2001', '2/3/2010', '10/10/1993'],
    'Username': ['JBolen', 'SCawthon', 'SGarreth', 'EBrockolith', 'MHindolah'],
    'Password': hashedPasswords
}

df = pd.DataFrame(data)

print(df)


username = 'JBolen'
password = 'Never'

# Can pair with HashSalting or just regular Hashing to handle passwords for logging in without recieving data.
# Can also filter by multiple values, put each "if" inside parentheses then add an "&" or "|" symbol for AND and OR.
loggedInUser = df[(df['Username'] == username) & (df['Password'] == bc.hashpw(password.encode(), salt))]
print(loggedInUser)

