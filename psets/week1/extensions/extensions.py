def main():
    print("File name: ", end="")
    # here to protect against unnecessary spaces , leading or trailing
    checkextension(input().strip())


# check extension checks the extensions and prints the appropriate response
def checkextension(filename):
    if "." in filename:
        name, type = filename.split(".")
        # print(name)
        type = type.lower()
        # print(type.lower())
        if type == "gif":
            print("image/gif")
        elif type == "jpg" or type == "jpeg":
            print("image/jpeg")
        # elif type == "jpeg":
        #     print("image/jpeg")
        elif type == "png":
            print("image/png")
        elif type == "pdf":
            print("application/pdf")
        elif type == "txt":
            print("text/plain")
        elif type == "zip":
            print("application/zip")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")


main()

