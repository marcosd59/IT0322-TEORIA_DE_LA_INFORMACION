# https://github.com/NabilLDZ/RunLengthEncoding_py/tree/main

__author__ = "NabilLDZ"

#text = input("Masukkan Text:")

text = "WWWWBBBWWWWBWBW"

def encode_message(text):
   encoded_string = ""
   i = 0
   while( i <= len(text)-1 ):
      count = 1
      ch = text[i]
      j = i
      while( j < len(text)-1 ):
         if(text[j] == text[j+1]):
            count = count + 1
            j = j + 1
         else:
            break
      encoded_string = encoded_string + str(count) + ch
      i = j + 1
   return encoded_string

print(encode_message(text))

texto_encoded = encode_message(text)

#chipper = input("Massukkan chipper text: ")

def decode(chipper_text):
   decoded_message = ""
   i = 0
   run_count=""
   while( i <= len(chipper_text) -1 ):
      if (chipper_text[i].isdigit()):
         run_count += chipper_text[i]
      else:
         run_ch = chipper_text[i]
         run_count = int(run_count)
         decoded_message +=  run_count * run_ch
         run_count=""
      i = i + 1
   return decoded_message

print(decode(texto_encoded))