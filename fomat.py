# 문자열 포멧팅
age = 20
msg = "제 이름은 마샬이고, 나이는 {}살 입니다."
a = msg.format(age)
# print(a)

# name = "마샬"
txt = "저는 {name}이고, 나이는 {age}살 입니다."
# {0}, {1}이 생략된 형태
b = txt.format(name = "마샬", age = 20)
print(b)

# 자리수 지정 포멧팅
# 변수 앞으로 5 자리까지 확보하고 오른쪽 정렬
c = "저는 {:>5}마리의 닭을 기릅니다."
# print(c.format(5))
# print(c.format(50))
# print(c.format(500))
# print(c.format(50000))
# print(c.format(50000000))

# 가운데 정렬 공간 확보
d = "저는 {:^7}마리의 닭을 기릅니다."
# print(d.format(5))
# print(d.format(50))
# print(d.format(500))

# 음수 표시는 음수 표시, 양수 표시는 기호 없이 그냥 양수 표시
e = "저는 {:=6}마리의 닭을 기릅니다."
# print(e.format(-5))
# print(e.format(50))
# print(e.format(-500))

# :+ 기호를 붙일 경우, 양수 또는 없는 기호에도 플러스 기호가 붙지만, 음수에는 음수 기호가 붙는다.
f = "오늘의  최고 기온은 {:+}도 이고, 최저 기온은 {:+}도 입니다."
print(f.format(10, -5))

# {:,} - 천 단위로 콤마를 찍어준다.
g = "저는 {:,}원을 가지고 있습니다."
print(g.format(100000000))

# {:.0%} - 백분율로 표시
h = "오늘의 확률은 {:.0%}입니다."
print(h.format(0.4))