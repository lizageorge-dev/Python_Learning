# The corrupted satellite data feed
satellite_feed = [
    "72-69-76-76-79",       # Encrypted Word 1 (ASCII decimal codes)
    "87-79-82-76-68",       # Encrypted Word 2 (ASCII decimal codes)
    42,                     # Global positioning float code (Corrupted data!)
    "  _sYstEm_oNlInE_  ",  # System status string
    "0"                     # Battery critical override multiplier
]
def decrypt_ascii_codes(codes):
    """Decrypts a list of ASCII decimal codes into a string."""
    decrypted_string = ""
    for code in codes:
        decrypted_string += chr(int(code))
    return decrypted_string
print(decrypt_ascii_codes(satellite_feed[0].split('-')))  # Decrypt the first word
print(decrypt_ascii_codes(satellite_feed[1].split('-')))  # Decrypt the second word
formatted_word=satellite_feed[3].replace("_", " ").lower().strip()  # Clean up the system status string
print(formatted_word)  # Print the formatted system status string
try:
    for item in satellite_feed:
        decrypt_ascii_codes(item.split('-'))
except (ValueError, TypeError, AttributeError) as e:
    print(f"Error occurred while decrypting data: {e}")
counter = 0
try:
    for item in satellite_feed:
      counter += 1
      print(f"Processing item {counter}: {item}")
      if counter == 5:
          print(100/int(item))

except (ZeroDivisionError, ValueError) as e:
    print(f"Error occurred while processing data: {e}")