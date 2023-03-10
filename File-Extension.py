user = input("Type a format:").lower()


match user:
    case "cat.gif":
     print("image/jpeg")
    case "cat.jpg":
     print("image/jpg")
    case "cat.jpeg":
     print("image/jpeg")
    case "dog.jpg":
     print("image/jpg")
    case _:
     print("application/octet-stream")

    

