text1=input("Enter to write to the file: ")
file= open('output.txt','a')
write=file.write(f"{text1} \n")
file.close()
print("Data successfully written to output.txt.")

text2=input("Enter additional text to append : ")
file= open('output.txt','a')
write=file.write(text2)
file.close()
print("Data successfully appended.")

print("Final content of output.txt: ")
file= open('output.txt','r')
read= file.read()
print(read)
file.close()
