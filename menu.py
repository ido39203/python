menu = ["피자", "치킨", "햄버거", "스테이크", "샐러드"]

print("다음 중 원하는 메뉴를 선택하세요:")
for i, item in enumerate(menu):
    print(f"{i + 1}. {item}")
    
choice = int(input("선택한 메뉴의 번호를 입력하세요: "))

if choice < 1 or choice > len(menu):
    print("잘못된 입력입니다.")
else:
    print(f"선택한 메뉴: {menu[choice-1]}")
