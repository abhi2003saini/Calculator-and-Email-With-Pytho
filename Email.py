email = input("Enter your email-id: ")  # Example: g@g.in
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in "_@.":
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong email: contains invalid characters")
                else:
                    print("Valid email")
            else:
                print("Wrong email: Invalid domain")
        else:
            print("Wrong email: Invalid '@' usage")
    else:
        print("Wrong email: First character is not alphabetic")
else:
    print("Wrong email: Too short")
