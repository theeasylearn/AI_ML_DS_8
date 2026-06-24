import re #regular expression 

def extract_emails(text: str) -> list:
    """
    Extract all email addresses from a given string using regular expression.
    
    Args:
        text (str): The input string that may contain email addresses.
    
    Returns:
        list: A list of all valid email addresses found in the string.
    """
    # Comprehensive email regex pattern
    email_pattern = r'''
        [a-zA-Z0-9._%+-]+      # Local part (username)
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # Domain name
        \.                     # Dot
        [a-zA-Z]{2,}           # Top-level domain
    '''
    
    # Find all matches (case insensitive)
    emails = re.findall(email_pattern, text, re.IGNORECASE | re.VERBOSE)
    
    return emails


# Example usage:
if __name__ == "__main__":
    sample_text = """
    Hello, you can contact us at support@example.com or 
    sales@company.co.in. Also reach out to admin@sub.domain.org
    or invalid-email@com (this should not match).
    My personal email is john.doe123+test@my-domain.com
    """
    
    result = extract_emails(sample_text)
    print(result)
    # Output: ['support@example.com', 'sales@company.co.in', 'admin@sub.domain.org', 'john.doe123+test@my-domain.com']