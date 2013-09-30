import math


def checkinput(a,b,c):
    if type(a) is float and type(b) is float and type(c) is float :
        return True
    return False


def detect_triangle(a,b,c):
    if checkinput(a,b,c) :
        saiso = 0.00000001
        if (a+b>c and b+c>a and c+a>b) :
            if a==b and b==c and c==a:
                return "tam giac deu"
            elif a==b :
                if math.fabs(c-math.sqrt(a**2+b**2)) <= saiso :
                    return "tam giac vuong can"
                else :
                    return "tam giac can"
            elif b==c :
                if math.fabs(a-math.sqrt(c**2 + b**2)) <= saiso :
                    return "tam giac vuong can"
                else :
                    return "tam giac can"
            elif c==a :
                if math.fabs(b-math.sqrt(a**2 + c**2)) <=saiso :
                    return "tam giac vuong can"
                else :
                    return "tam giac can"
            elif a!=b and b!=c and c!=a :
                if math.fabs(a-math.sqrt(c**2 + b**2)) <=saiso :
                    return "tam giac vuong"
                if math.fabs(b-math.sqrt(a**2 + c**2)) <=saiso :
                    return "tam giac vuong"
                if math.fabs(c-math.sqrt(a**2 + b**2)) <=saiso :
                    return "tam giac vuong"
                else :
                    return "tam giac thuong"
        else :
            return "khong phai la tam giac"
    else :
        return "loi dau vao"
