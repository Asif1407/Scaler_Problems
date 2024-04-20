import time

# Define your text
text = "This is an example sentence with delays between words."

# Split the text into words
words = text.split()

# Define the delay duration in seconds
delay_seconds = 0.30  # Adjust this value to control the pace (0.5 seconds in this example)

# Loop through the words and print them with delays
for word in words:
    print(word, end=' ', flush=True)  # Use flush=True to ensure immediate output
    time.sleep(delay_seconds)

# Print a newline character at the end
print()