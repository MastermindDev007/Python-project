import subprocess

# Get the list of profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Extract profile names
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Loop through the profiles
for i in profiles:
    # Get the profile details, including the key (password)
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    # Extract the key content
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        # Print the profile name and its corresponding key (password)
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        # If no key content is found, print just the profile name
        print("{:<30}| {:<}".format(i, ""))
