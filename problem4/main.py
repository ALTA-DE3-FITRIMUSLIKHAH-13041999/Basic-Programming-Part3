def palindrome(input_string):
    #return 'error response'

 # hapus spasi input string dan mengonversinya menjadi huruf kecil
    input_string = input_string.replace(" ", "").lower()
 # Memeriksa apakah string dan string yang dibalik sama
    return input_string == input_string[::-1]

if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False

