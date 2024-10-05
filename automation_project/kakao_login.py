import pyautogui
import pyautogui as pg
import pyperclip
from time import sleep

x, y = pg.position()
print(x, y)
# login - id입력 1645 664

# 마우스 특정 위치로 이동
pg.moveTo(1645, 664)

# 마우스 클릭
pg.click()

# keyboard입력
pg.typewrite('***@***.com', interval=0.1)

# password입력
# 1647 698
pg.moveTo(1647, 698) #패스워드 입력
pg.click()
pg.typewrite('djkxclvkj', interval=0.1)

#로그인 버튼
pg.moveTo(1734, 748)
sleep(0.5)
pg.click()