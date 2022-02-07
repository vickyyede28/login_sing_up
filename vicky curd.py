import json,os
# # g= open("newfile.txt","w")
# # g.write("he is a boy an a khinching")
# # g=open("newfile.txt","r")
# # print(g.read())
# # g=open("newfile.txt","w")
# # g.write("")
# # import json
# # def insert():
# #     with open("oldfile.json","a") as h:
# #             c={}
# #             c["name"]=input("enter your name::--  ")
# #             c["email"]=input("enter your email::--  ")
# #             with open("oldfile.json","a") as g:
# #                 json.dump(c,g,indent=4)
# # insert()


# # *******************CRUD MAKING************

def insert():
    if (os.path.exists("win.json")):
        with open("win.json","r") as q:
            b=json.load(q)
            w={}
            w["name"]=input("enter your name:--")
            w["email"]=input("enter your email:--")
            w["password"]=input("enter your password:--")
            w["mobile"]=int(input("enter your mobile:--"))
            b.append(w)
            with open("win.json","w") as e:
                json.dump(b,e,indent=4)
    else:
        with open("win.json","w") as r:
            r.write("[]")
# insert() 

def update():
    if (os.path.exists("win.json")):
        with open("win.json","r") as r:
            t=json.load(r)
            m=int(input("enter your mobile "))
            for y in t:
                for u in y.values():
                    if m==u: 
                        y["name"]=input("enter your new name:-- ")
                        y["email"]=input("enter your new email:--")
                        y["password"]=input("enter your new password:-- ")

                        # t.append(y)
                with open("win.json","w") as i:
                    json.dump(t,i,indent=4)
    else:
        with open("win.json","w") as o:
            o.write("it is wrong")

# update()

def delete():
    if (os.path.exists("win.json")):
        with open("win.json","r") as p:
            a=json.load(p)
            s=+0
            d=input("enter your del email:--  ")
            for f in a:
                s=+1
                for g in f.values():
                    if g==d:
                        a.pop(s-1)
                        with open("win.json","w") as j:
                            json.dump(a,j,indent=4)
    else:
        with open("win.json","w") as k:
            k.write("[]")


# delete()

z=int(input("1 insert\n2 update\n3 delete\n"))
if z==1:
    insert()
elif z==2:
    update()
else:
    delete()


# # *************************  SIGN UP //////////////   LOG IN     \\\\\\\\\\\\\\\
# # print("login\nsignup\n")
# import json,os
# def signup():
#     if (os.path.exists("account.json")):
#         with open ("account.json","r") as q:
#             w=json.load(q)
#             e={}
#             e["name"]=input("enter your name: ")
#             e["email"]=input("enter your email: ")
#             e["password"]=input("enter your password: ")
#             e["mobile"]=input("enter your mobile: ")
#             # e["YOU HAVE SUCCESSFULLY SIGN UP IN  "]
#             w.append(e)
#             with open("account.json","w") as r:
#                 json.dump(w,r,indent=4)
#     else:
#         with open("account.json","w") as t:
#             t.write("[]")

# # signup()

# def login():
#     if (os.path.exists("account.json")):
#         with open("account.json","r") as y:
#             u=json.load(y)
#             i=input("enter your mobile: ")
#             for s in u:
#                 if i in s.values():
#                     print("SUCCESSFULLY LOGGIED IN : ",u)
#                 else:
#                     print("DIDN'T LOGGED IN SUCCESFULLY: ")
#                     u.append(i)
#                     with open("account.json","w") as p:
#                         json.dump(u,p,indent=4)
#     else:
#         with open("account.json","w") as a:
#             a.write("[]")

# b=int(input("1.sign up 2. login "))
# if b==1:
#     signup()
# elif b==2:
#     login()



#             import mymodule 
# # # import platform
# def greeting(name):
#   print("Hello, " + name)
# mymodule.greeting("janethem")

#  def pattern(n):
#     if n==0:
#         return 1
#     else:
#         pattern(n-1)
#         for i in range(1,n+1):
#             print(i,end="")
# pattern(4)