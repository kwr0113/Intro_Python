# boolean 불리언

print(bool(True))

print(bool(False))

print(bool(1))

print(bool(45))

print(bool(-2))

print(bool(0))



# integer 정수

# 오류 - 숫자 앞에는 0을 사용할 수 없음
# print(01)

print(123)
print(+123)
print(-123)

a = 1,000,000
print(a)
print(type(a))  # 튜플이 됨

print(1_2_34)   # 콤마 대신 언더바를 사용하여 숫자 구분 가능

print(0b10)
print(0o10)
print(0x10)

num = 65
print(bin(num))
print(oct(num))
print(hex(num))

googol = 10**100
print(googol)
print(googol*googol)



# float 부동소수점

print(5.)
print(5.0)
print(05.0)
print(5e0)
print(5e1)
print(5.0e1)