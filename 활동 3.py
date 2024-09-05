#활동3-1
a,b=map(int,input().split())
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}//{b}={a//b}")
print(f"{a}%{b}={a%b}")


#활동3-2
width,height=map(float,input().split())
print(width*height/2)


#활동3-3
r=float(input("반지름을 입력해주세요:"))
print(f"넓이는 {round(r**2*3.14,1)} 입니다.")
