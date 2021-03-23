from hashlib import sha256


secret_phrase = "cevap"

def get_hash(input_data, secret_phrase):
    combined = input_data + secret_phrase
    return sha256(combined.encode()).hexdigest()

data = "sorunun cavabı : "


if __name__ == "__main__":
    result = get_hash(data, secret_phrase)
    print(result)