# 매개변수 관련 팁

def welcome(city, name = "Guest", room = []):
    room.append(100)
    print(f"Hello, {name}! This is {city}. You can use {room}")


welcome("New York") # room = 100
welcome("Seattle", "Hyo") # room = 100 , 100 이런식으로 기본값으로 설정된 room 이 모든 함수 호출에서 동일한 리스트 객체를 공유하게 된다.


# 해결 방법
def welcome(city, name = "Guest", room = None):
    if room is None:
        room = []
    room.append(100)
    print(f"Hello, {name}! This is {city}. You can use {room}")

welcome("New York")
welcome("Seattle" , "Sik")