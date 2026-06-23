try:
    file=open("sample.txt","r")
    content=file.read()
    print("File Content:")
    print(content)
    file.close()
except FileNotFoundError:
    print("File Not Found!")
except Exception as e:
    print("An Error Occured:",e)