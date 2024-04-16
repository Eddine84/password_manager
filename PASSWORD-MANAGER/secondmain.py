

# #FileNotFound

# try:
#     file = open("filedata.txt")
#     a_dictionary = {"key":"vallue"}
#     print(a_dictionary["key"]) 
# except FileNotFoundError as error_message:
#     file = open("filedata.txt", "w")
#     file.write("Somthing")

# except KeyError as error_key_message:
#     print(f"thi is  {error_key_message} i dont find your key")
   

# else:
#     content = file.read()  
#     print(content)

# finally:
#     file.close()

dic = {
    "dictionnaire":{
        "name":"djamel",
        "age":39
    }
}

print(type(dic))