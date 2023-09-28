import hashlib

def get_id(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode())
    id_based_on_string = md5_hash.hexdigest()
    remove_non_alphanumeric = str.maketrans('', '', '!@#$%^&*()_+[]{}|;:",.<>?/\\`~ ')
    cleaned_id = id_based_on_string.translate(remove_non_alphanumeric)
    return cleaned_id
