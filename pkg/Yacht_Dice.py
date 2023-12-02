import random
import pandas as pd
class Yacht_Dice : # 점수기록 및 플레이 클래스
  def __init__(self, list_) :
    self.dice1 = list_
    self.retry = 2
    self.score = 0

  @staticmethod
  def random() :  # 주사위 5개 랜덤으로 돌리기
    return random.choices([1, 2, 3, 4, 5, 6], k = 5)

  @staticmethod
  def randomchoice(n) : # 주사위 n개만 선택해서 랜덤으로 돌리기
    return random.choices([1, 2, 3, 4, 5, 6], k = n)

  @classmethod
  def getdice(cls, list_) :
    return cls(list_)

  def possible(self) : # 주사위 눈에 따라 가능한 점수계산방법을 반환하는 메소드
    if self.dice1.count(1) :
      print('Ones', end = ', ')

    if self.dice1.count(2) :
      print('Twos', end = ', ')

    if self.dice1.count(3) :
      print('Threes', end = ', ')

    if self.dice1.count(4) :
      print('Fours', end = ', ')

    if self.dice1.count(5) :
      print('Fives', end = ', ')

    if self.dice1.count(6) :
      print('Sixes', end = ', ')

    for i in range(6) :
        if self.dice1.count(i+1) >= 4 :
          print('Four_of_a_kind', end = ', ')

        if self.dice1.count(i+1) == 3 :
          for j in range(6) :
            if self.dice1.count(j+1) == 2 :
              print('Full_House', end = ', ')

        if self.dice1.count(i+1) == 5 :
          print('Yacht', end = ', ')

    if [True for i in [1,2,3,4] if i in self.dice1] == [True, True, True, True] \
    or [True for i in [2,3,4,5] if i in self.dice1] == [True, True, True, True] \
    or [True for i in [3,4,5,6] if i in self.dice1] == [True, True, True, True] :
      print('Little_Straight', end = ', ')

    if sorted(self.dice1) == [2,3,4,5,6] or sorted(self.dice1) == [1,2,3,4,5]:
      print('Big_Straight', end = ', ')

    print('Choice', end = ', ')

  def Ones(self) : # 1이 나온 주사위 눈의 총합. 최대 5점
    count_ones = self.dice1.count(1)
    self.score = min(count_ones, 5)

  def Twos(self) : # 2가 나온 주사위 눈의 총합. 최대 10점
    count_twos = self.dice1.count(2)*2
    self.score = min(count_twos, 10)

  def Threes(self) : # 3이 나온 주사위 눈의 총합. 최대 15점
    count_threes = self.dice1.count(3)*3
    self.score = min(count_threes, 15)

  def Fours(self) : # 4가 나온 주사위 눈의 총합. 최대 20점
    count_fours = self.dice1.count(4)*4
    self.score = min(count_fours, 20)

  def Fives(self) : # 5가 나온 주사위 눈의 총합. 최대 25점
    count_fives = self.dice1.count(5)*5
    self.score = min(count_fives, 25)

  def Sixes(self) : # 6이 나온 주사위 눈의 총합. 최대 30점
    count_sixes = self.dice1.count(6)*6
    self.score = min(count_sixes, 30)

  def Four_of_a_kind(self) : # 동일한 주사위 눈이 4개 이상일 때, 주사위 눈의 총합. 최대 30점
    for i in range(6) :
      if self.dice1.count(i+1) >= 4 :
        self.score = min(sum(self.dice1), 30)

  def Full_House(self) : # 동일한 주사위 눈이 각각 3개, 2개일 때, 5개의 총합. 최대 30점
    for i in range(6) :
      if self.dice1.count(i+1) == 3 :
        for j in range(6) :
          if self.dice1.count(j+1) == 2 :
            self.score = min(3*(i+1) + 2*(j+1), 30)

  def Little_Straight(self) : # 주사위 눈이 각각 1,2,3,4 or 2,3,4,5 or 3,4,5,6일 때, 고정 15점
    if [True for i in [1,2,3,4] if i in self.dice1] == [True, True, True, True] \
    or [True for i in [2,3,4,5] if i in self.dice1] == [True, True, True, True] \
    or [True for i in [3,4,5,6] if i in self.dice1] == [True, True, True, True] :
      self.score = 15

  def Big_Straight(self) : # 주사위 눈이 각각 2,3,4,5,6일 때, 고정 30점
    if sorted(self.dice1) == [2,3,4,5,6] or sorted(self.dice1) == [1,2,3,4,5]:
      self.score = 30

  def Yacht(self) : # 동일한 주사위 눈이 5개일 때, 고정 50점
    for i in range(6) :
      if self.dice1.count(i+1) == 5 :
        self.score = 50

  def Choice(self) : # 주사위 눈 54개의 총합. 최대 30점
    self.score = min(sum(self.dice1), 30)