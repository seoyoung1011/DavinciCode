import random, time

BlackChips = ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "BJ"]
WhiteChips = ["W0", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "WJ"]

class board:
    code = []
    opencode = ['x', 'x', 'x', 'x']

    def __init__(self):
        pass

    def print(self):
        str = ""
        for i in range(len(self.opencode)):
            if self.opencode[i] == 'o':
                str += self.code[i] + ' '
            elif self.opencode[i] == 'x':
                if self.code[i].find('B') == 0:
                    str += "B* "
                elif self.code[i].find('W') == 0:
                    str += "W* "
        print(str)

    def __str__(self):
        str = ""
        for i in range(len(self.opencode)):
            if self.opencode[i] == 'o':
                str += self.code[i] + ' '
            elif self.opencode[i] == 'x':
                if self.code[i].find('B') == 0:
                    str += "B* "
                elif self.code[i].find('W') == 0:
                    str += "W* "
        return str

class person(board):

    def start_sort(self):
        # 만약 조커가 있으면 code리스트에서 제외. 삽입 정렬 후 원하는 곳에 조커 배치
        J = 'N'
        if "BJ" in self.code and "WJ" in self.code:
            self.code.remove("BJ")
            self.code.remove("WJ")
            J = 'BW'
        elif "BJ" in self.code:
            self.code.remove("BJ")
            J = 'B'
        elif "WJ" in self.code:
            self.code.remove("WJ")
            J = 'W'
        for i in range(1, len(self.code)):
            for j in range(i, 0, -1):
                if int(self.code[j - 1][1:]) > int(self.code[j][1:]):
                    self.code[j - 1], self.code[j] = self.code[j], self.code[j - 1]
                elif int(self.code[j - 1][1:]) == int(self.code[j][1:]):
                    if self.code[j - 1][0] == 'W':
                        self.code[j - 1], self.code[j] = self.code[j], self.code[j - 1]
        if J == 'BW':
            print(f'{self.code}')
            index = int(input(f'검정색 조커를 몇번째에 놓으시겠습니까?(1~3) : '))
            self.code.insert(index-1, 'BJ')
            print(f'{self.code}')
            index = int(input(f'하양색 조커를 몇번째에 놓으시겠습니까?(1~4) : '))
            self.code.insert(index-1, 'WJ')
        elif J == 'B':
            print(f'{self.code}')
            index = int(input(f'검정색 조커를 몇번째에 놓으시겠습니까?(1~4) : '))
            self.code.insert(index-1, 'BJ')
        elif J == 'W':
            print(f'{self.code}')
            index = int(input(f'하양색 조커를 몇번째에 놓으시겠습니까?(1~4) : '))
            self.code.insert(index-1, 'WJ')

    def add_sort(self):
        # 조커소지여부 확인 후 조커 위치 기억. 조커를 code리스트에서 제거 후 검정색 칩이나 하양색 칩 골라서 가져옴.
        # 가져온 칩이 조커면 원하는 위치에 배치.
        # 조커가 있는 상태에서 정렬 시 정렬 후 조커 배치. 조커의 원래 위치보다 뒤에 있으면 원래 위치에 조커 배치. 아니면 조커위치인덱스+1 배치
        remember_BJ = -1
        remember_WJ = -1
        remember_C = ""
        if "BJ" in self.code and "WJ" in self.code:
            remember_BJ = self.code.index("BJ")
            self.code.remove("BJ")
            remember_WJ = self.code.index("WJ")
            self.code.remove("WJ")
        elif "BJ" in self.code:
            remember_BJ = self.code.index("BJ")
            self.code.remove("BJ")
        elif "WJ" in self.code:
            remember_WJ = self.code.index("WJ")
            self.code.remove("WJ")
        color = input("무슨 색 칩을 뽑으시겠습니까?(B, W) : ")
        if color == 'B':
            if BlackChips[0] == "BJ":
                print(f'{self.code}')
                index = int(input(f'검정색 조커를 몇번째에 놓으시겠습니까?(1~{len(self.code)+1}) : '))
                self.code.insert(index - 1, 'BJ')
                remember_C = BlackChips[0]
                BlackChips.remove(BlackChips[0])
                self.opencode.insert(self.code.index(remember_C), 'x')
                return None
            self.code.append(BlackChips[0])
            remember_C = BlackChips[0]
            BlackChips.remove(BlackChips[0])
        elif color == 'W':
            if WhiteChips[0] == "WJ":
                print(f'{self.code}')
                index = int(input(f'하양색 조커를 몇번째에 놓으시겠습니까?(1~{len(self.code)+1}) : '))
                self.code.insert(index - 1, 'WJ')
                remember_C = WhiteChips[0]
                WhiteChips.remove(WhiteChips[0])
                self.opencode.insert(self.code.index(remember_C), 'x')
                return None
            self.code.append(WhiteChips[0])
            remember_C = WhiteChips[0]
            WhiteChips.remove(WhiteChips[0])
        for i in range(1, len(self.code)):
            for j in range(i, 0, -1):
                if int(self.code[j - 1][1:]) > int(self.code[j][1:]):
                    self.code[j - 1], self.code[j] = self.code[j], self.code[j - 1]
                elif int(self.code[j - 1][1:]) == int(self.code[j][1:]):
                    if self.code[j - 1][0] == 'W':
                        self.code[j - 1], self.code[j] = self.code[j], self.code[j - 1]
        if remember_BJ > 0:
            if remember_BJ <= self.code.index(remember_C):
                self.code.insert(remember_BJ, "BJ")
            else:
                self.code.insert(remember_BJ+1, "BJ")
        if remember_WJ > 0:
            if remember_WJ <= self.code.index(remember_C):
                self.code.insert(remember_WJ, "WJ")
            else:
                self.code.insert(remember_WJ+1, "WJ")
        self.opencode.insert(self.code.index(remember_C), 'x')


    def guess(self, computer):
        num = 0
        while(True):
            num = int(input(f'몇번쩨 칩을 고르시겠습니까? (1~{len(computer.opencode)}) : '))
            chipnum = input(f'어떤 숫자(또는 조커)로 예측하십니까? : ')
            num -= 1
            if(num < len(computer.opencode)):
                break
        chip = computer.code[num][0] + chipnum
        if(computer.code[num] == chip):
            computer.opencode[num] = 'o'
        else:
            print("땡!")





class computer(board):

    def start_sort(self):
        # 만약 조커가 있으면 code리스트에서 제외. 삽입 정렬 후 랜덤으로 조커 배치
        J = 'N'
        if "BJ" in self.code and "WJ" in self.code:
            self.code.remove("BJ")
            self.code.remove("WJ")
            J = 'BW'
        elif "BJ" in self.code:
            self.code.remove("BJ")
            J = 'B'
        elif "WJ" in self.code:
            self.code.remove("WJ")
            J = 'W'
        for i in range(1, len(self.code)):
            for j in range(i, 0, -1):
                if int(self.code[j - 1][1:]) > int(self.code[j][1:]):
                    self.code[j - 1], self.code[j] = self.code[j], self.code[j - 1]
                elif int(self.code[j - 1][1:]) == int(self.code[j][1:]):
                    if self.code[j - 1][0] == 'W':
                        self.code[j - 1], self.code[j] = self.code[j], self.code[j - 1]
        if J == 'BW':
            print(f'{self.code}')
            index = random.randrange(3)
            self.code.insert(index, 'BJ')
            print(f'{self.code}')
            index = random.randrange(4)
            self.code.insert(index, 'WJ')
        elif J == 'B':
            print(f'{self.code}')
            index = random.randrange(4)
            self.code.insert(index, 'BJ')
        elif J == 'W':
            print(f'{self.code}')
            index = random.randrange(4)
            self.code.insert(index, 'WJ')

    def add_sort(self):
        # 조커소지여부 확인 후 조커 위치 기억. 조커를 code리스트에서 제거 후 검정색 칩이나 하양색 칩 골라서 가져옴.
        # 가져온 칩이 조커면 랜덤 위치에 배치.
        # 조커가 있는 상태에서 정렬 시 정렬 후 조커 배치. 조커의 원래 위치보다 뒤에 있으면 원래 위치에 조커 배치. 아니면 조커위치인덱스+1 배치
        remember_BJ = -1
        remember_WJ = -1
        remember_C = ""
        if "BJ" in self.code and "WJ" in self.code:
            remember_BJ = self.code.index("BJ")
            self.code.remove("BJ")
            remember_WJ = self.code.index("WJ")
            self.code.remove("WJ")
        elif "BJ" in self.code:
            remember_BJ = self.code.index("BJ")
            self.code.remove("BJ")
        elif "WJ" in self.code:
            remember_WJ = self.code.index("WJ")
            self.code.remove("WJ")
        color = random.choice(['B', 'W'])
        if color == 'B':
            if BlackChips[0] == "BJ":
                print(f'{self.code}')
                index = random.randrange(len(self.code))
                self.code.insert(index, 'BJ')
                remember_C = BlackChips[0]
                BlackChips.remove(BlackChips[0])
                self.opencode.insert(self.code.index(remember_C), 'x')
                return None
            self.code.append(BlackChips[0])
            remember_C = BlackChips[0]
            BlackChips.remove(BlackChips[0])
        elif color == 'W':
            if WhiteChips[0] == "WJ":
                print(f'{self.code}')
                index = random.randrange(len(self.code))
                self.code.insert(index, 'WJ')
                remember_C = WhiteChips[0]
                WhiteChips.remove(WhiteChips[0])
                self.opencode.insert(self.code.index(remember_C), 'x')
                return None
            self.code.append(WhiteChips[0])
            remember_C = WhiteChips[0]
            WhiteChips.remove(WhiteChips[0])
        for i in range(1, len(self.code)):
            for j in range(i, 0, -1):
                if int(self.code[j - 1][1:]) > int(self.code[j][1:]):
                    self.code[j - 1], self.code[j] = self.code[j], self.code[j - 1]
                elif int(self.code[j - 1][1:]) == int(self.code[j][1:]):
                    if self.code[j - 1][0] == 'W':
                        self.code[j - 1], self.code[j] = self.code[j], self.code[j - 1]
        if remember_BJ > 0:
            if remember_BJ <= self.code.index(remember_C):
                self.code.insert(remember_BJ, "BJ")
            else:
                self.code.insert(remember_BJ + 1, "BJ")
        if remember_WJ > 0:
            if remember_WJ <= self.code.index(remember_C):
                self.code.insert(remember_WJ, "WJ")
            else:
                self.code.insert(remember_WJ + 1, "WJ")
        self.opencode.insert(self.code.index(remember_C), 'x')

    def guess(self, p_code, p_opencode):
        guess_list = {}
        bNum = 0; wNum = 0; guessC = ''
        # 검정 칩과 하양 칩의 개수를 구함
        for c in self.code:
            if c[0] == 'B':
                bNum += 1
            elif c[0] == 'W':
                wNum += 1
        # 검청 칩의 개수가 더 많거나 같으면 검정 칩을 추리, 하양칩이 더 많으면 하양 칩을 추리
        if bNum >= wNum:
            guessC = 'B'
        elif wNum > bNum:
            guessC = 'W'
        # guess_list 에 1~j의 값을 넣어줌
        for i in range(len(self.code)):
            guess_list[i + 1] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'J']
        if self.opencode == ['x', 'x', 'x', 'x']:
            spot = random.randrange(1, len(self.opencode)+1)
            guessC


def shuffle_card():
    p_list = []
    c_list = []

    for i in range(5 + 1):
        random.shuffle(BlackChips)
        random.shuffle(WhiteChips)
    for i in range(0, 1+1):
        p_list.append(BlackChips[i])
        BlackChips.remove(BlackChips[i])
        p_list.append(WhiteChips[i])
        WhiteChips.remove(WhiteChips[i])
    for i in range(2, 3+1):
        c_list.append(BlackChips[i])
        BlackChips.remove(BlackChips[i])
        c_list.append(WhiteChips[i])
        WhiteChips.remove(WhiteChips[i])
    return p_list, c_list

