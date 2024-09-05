#실습1
print("5*3/2")
print("7*7*3.14")
print("4.5*4.5*4.5")


#실습3
print(5+3)
print(7*2-4)
print(15/2)


#실습4
print(f"5+3={5+3}")
print(f"7*2-4의 결과는 {7*2-4}입니다.")
print(f"15 나누기 2의 결과는 {15//2}입니다")  #교과서에는 정수형 몫으로 나와서 정수형으로 나눔, 7띄어쓰기 안해서 걍 함.


#p.133, 문자열 포맷 쓰니깐 간단해짐!!!
a=int(input("원하는 단을  입력하시오: "))
print(f"{a}*9={a*9}") 
print(f"{a}*8={a*8}")
print(f"{a}*7={a*7}")
print(f"{a}*6={a*6}")
print(f"{a}*5={a*5}")
print(f"{a}*4={a*4}")
print(f"{a}*3={a*3}")
print(f"{a}*2={a*2}")
print(f"{a}*1={a}")


#실습5
num1=input()
print("입력받은 값="+num1)


#실습6
num2=input()
num3=input()
print("입력받은 값={0},{1}".format(num2,num3))


#실습7
num4=float(input())
print(f"입력받은 값={num4}")


#실습8
x,y=map(float,input().split())
print(f"입력값={round(x,2)},{round(y,2)}")
#round 한번에 못함? 
'''
map->float를 x,y 두 개에 할당할 때 필요
split->input 값을 x,y로 자를 때 필요
round->n자리까지 반올림하여 출력 ex)round(a,3)->a값을 반올림하여 셋째 자리까지 출력
'''


















