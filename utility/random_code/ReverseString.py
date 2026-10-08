def reverse_string(string):
    string_len = len(string)
    return "".join([string[string_len-i-1] for i in range(string_len)])

if __name__ == "__main__":
    string = "text_"
    print(reverse_string(string))
