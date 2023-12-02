from pkg.ScoreBoard import *
from pkg.Yacht_Dice import *
from pkg.next_phase import *
from pkg.motion import *
import pandas as pd

if __name__ == '__main__' :
  chance = 6              # 총 6번의 플레이 찬스
  me_score_method = []     # 이미 선택한 점수계산방식들이 들어갈 리스트(나의)
  enemy_score_method = []  # 이미 선택한 점수계산방식들이 들어갈 리스트(적의)
  df = ScoreBoard.score()  # 텅 빈 스코어보드 생성
  score_method = ['Ones', 'Twos','Threes','Fours','Fives','Sixes','Four_of_a_kind','Full_House','Little_Straight','Big_Straight','Yacht','Choice','Nothing']
  lower_score_method = ['ones', 'twos','threes','fours','fives','sixes','four_of_a_kind','full_house','little_straight','big_straight','yacht','choice','nothing']

  while chance > 0 :
    me = Yacht_Dice.getdice(Yacht_Dice.random()) # 내 주사위 굴리기
    chance -= 1
    main()

    print('\n')
    print('<scoreboard>')
    print(df,'\n')
    print('<chance> : ', chance)
    print('<Player1의 try>')
    while me.retry > 0 : # 1번의 chance (나의)
      for i in me.dice1 :
        print([i], end = ', ')
      print('\n')
      print('이 중 원하는 주사위는 남겨두고, 나머지 주사위들을 다시 던질 수 있습니다.')

      try :
        again = list(map(int, input('🎅다시 던지고 싶지 않다면 0를, \n던지고 싶다면 던지고 싶은 주사위 넘버를 공백으로 구분하여 쓰세요.🎅').strip().split(' ')))
        if 0 not in again and 1 not in again and 2 not in again and 3 not in again and 4 not in again and 5 not in again :
          raise ValueError('--🚨0 또는 1에서 5사이의 값을 입력하세요.🚨--')  # 예외구문 1

      except ValueError as e :
        print(e,'\n')
        continue

      else :
        if again == [0] : # 다시 돌리고 싶지 않을 때
          me.possible()   # 가능한 점수계산 방법 반환
          while True :
            try :
              score = input('🎄하나의 점수 계산 방법을 선택해주세요.\n 만약 선택하고 싶은 것이 없다면 Nothing을 적어주세요. 단, 점수는 0점입니다.🎄') # 점수계산 방법 선택

              if score.lower() in lower_score_method and score not in score_method :
                raise ValueError('--🚨대소문자를 알맞게 입력하였는지 확인하세요.🚨--')  # 예외구문 2

              if score not in score_method :
                raise AttributeError('--🚨가능한 점수계산 방법만 써주세요.🚨--')  # 예외구문 3

              if score in me_score_method :
                raise ValueError('--🚨이미 선택했던 점수계산 방법입니다.🚨--')  # 예외구문 4

            except AttributeError as e :
              print(e,'\n')
              continue

            except ValueError as e :
              print(e,'\n')
              continue

            else :
              break

          if score not in me_score_method :  # 이미 선택했던 방식이 아닐 때
            if score == 'Nothing' :
              me.score = 0
              break

            else :
              score_final = getattr(me, score)  # 입력받은 문자열 형태의 메소드를 메소드로 변환
              score_final()                     # 실행
              me_score_method.append(score)     # 사용한 점수계산방식 리스트에 추가
          df.loc[score,'Player1'] = me.score    # 스코어 보드에 score 추가
          next_phase.Bonus(df, 'Player1')       # 보너스 계산
          next_phase.Total_Score(df, 'Player1') # 총합 계산
          break

        else : # 다시 돌리고 싶을 때
          main()

          retry = [x-1 for x in again] # 주사위 넘버를 각각 -1해서 인덱스로 변환
          remains = [value for index, value in enumerate(me.dice1) if index not in retry] # 남아있는 주사위
          again_dice = Yacht_Dice.randomchoice(len(retry)) # 바뀐 주사위
          me.dice1 = remains + again_dice
          me.retry -= 1
          main()

          if me.retry == 0 : # 끝
            for i in me.dice1 :
              print([i], end = ', ')
            print('\n')
            me.possible()   # 가능한 점수계산 방법 반환
            while True :
              try :
                score = input('🎄하나의 점수 계산 방법을 선택해주세요.\n 만약 선택하고 싶은 것이 없다면 Nothing을 적어주세요. 단, 점수는 0점입니다.🎄') # 점수계산 방법 선택
                if score.lower() in lower_score_method and score not in score_method :
                  raise ValueError('--🚨대소문자를 알맞게 입력하였는지 확인하세요.🚨--')

                if score not in score_method :
                  raise AttributeError('--🚨가능한 점수계산 방법만 써주세요.🚨--')

                if score in me_score_method :
                  raise ValueError('--🚨이미 선택했던 점수계산 방법입니다.🚨--')

              except AttributeError as e :
                print(e,'\n')
                continue

              except ValueError as e :
                print(e,'\n')
                continue

              else :
                break

            if score not in me_score_method :
              if score == 'Nothing' :
                me.score = 0
                print(df,'\n')
                break
              else :
                score_final = getattr(me, score)
                score_final()
                me_score_method.append(score)
            df.loc[score,'Player1'] = me.score
            next_phase.Bonus(df, 'Player1')
            next_phase.Total_Score(df, 'Player1')
            print(df,'\n')
          continue

  # 1번의 chance (적의)
    main()

    print('<scoreboard>')
    print(df,'\n')
    enemy = Yacht_Dice.getdice(Yacht_Dice.random()) # 적 주사위 굴리기
    print('<Player2의 try>')

    while enemy.retry > 0 : # 1번의 chance (적의)
      for i in enemy.dice1 :
        print([i], end = ', ')
      print('\n')
      print('이 중 원하는 주사위는 남겨두고, 나머지 주사위들을 다시 던질 수 있습니다.')
      try :
        again = list(map(int, input('🔔다시 던지고 싶지 않다면 0를, \n던지고 싶다면 던지고 싶은 주사위 넘버를 공백으로 구분하여 쓰세요.🔔').strip().split(' ')))
        if 0 not in again and 1 not in again and 2 not in again and 3 not in again and 4 not in again and 5 not in again :
          raise ValueError('--🚨0 또는 1에서 5사이의 값을 입력하세요.🚨--')

      except ValueError as e :
        print(e,'\n')
        continue

      else :
        if again == [0] : # 다시 돌리고 싶지 않을 때
          enemy.possible()   # 가능한 점수계산 방법 반환
          while True :
            try :
              score = input('🎁하나의 점수 계산 방법을 선택해주세요.\n 만약 선택하고 싶은 것이 없다면 Nothing을 적어주세요. 단, 점수는 0점입니다.🎁') # 점수계산 방법 선택
              if score.lower() in lower_score_method and score not in score_method :
                raise ValueError('--🚨대소문자를 알맞게 입력하였는지 확인하세요.🚨--')

              if score not in score_method :
                raise AttributeError('--🚨가능한 점수계산 방법만 써주세요.🚨--')

              if score in enemy_score_method :
                raise ValueError('--🚨이미 선택했던 점수계산 방법입니다.🚨--')

            except AttributeError as e :
              print(e,'\n')
              continue

            except ValueError as e :
              print(e,'\n')
              continue

            else :
              break

          if score not in enemy_score_method :
            if score == 'Nothing' :
              enemy.score = 0
              print(df,'\n')
              break
            else :
              score_final = getattr(enemy, score)
              score_final()
              enemy_score_method.append(score)
          df.loc[score,'Player2'] = enemy.score
          next_phase.Bonus(df, 'Player2')
          next_phase.Total_Score(df, 'Player2')
          print(df,'\n')
          break

        else : # 다시 돌리고 싶을 때
          main()
          retry = [x-1 for x in again] # 인덱스로 변환
          remains = [value for index, value in enumerate(enemy.dice1) if index not in retry] # 남아있는 주사위
          again_dice = Yacht_Dice.randomchoice(len(retry)) # 바뀐 주사위
          enemy.dice1 = remains + again_dice
          enemy.retry -= 1
          main()

          if enemy.retry == 0 : # 끝
            for i in enemy.dice1 :
              print([i], end = ', ')
            enemy.possible()   # 가능한 점수계산 방법 반환
            while True :
              try :
                score = input('🎁하나의 점수 계산 방법을 선택해주세요.\n 만약 선택하고 싶은 것이 없다면 Nothing을 적어주세요. 단, 점수는 0점입니다.🎁') # 점수계산 방법 선택
                if score.lower() in lower_score_method and score not in score_method :
                  raise ValueError('--🚨대소문자를 알맞게 입력하였는지 확인하세요.🚨--')

                if score not in score_method :
                  raise AttributeError('--🚨가능한 점수계산 방법만 써주세요.🚨--')

                if score in enemy_score_method :
                  raise ValueError('--🚨이미 선택했던 점수계산 방법입니다.🚨--')

              except AttributeError as e :
                print(e,'\n')
                continue

              except ValueError as e :
                print(e,'\n')
                continue

              else :
                break

            if score not in enemy_score_method :
              if score == 'Nothing' :
                enemy.score = 0
                print(df,'\n')
                break
              else :
                score_final = getattr(enemy, score)
                score_final()
                enemy_score_method.append(score)
            df.loc[score,'Player2'] = enemy.score
            next_phase.Bonus(df, 'Player2')
            next_phase.Total_Score(df, 'Player2')
          continue

  if df.loc['TOTAL SCORE', 'Player1'] > df.loc['TOTAL SCORE', 'Player2'] :
    print('🏆Player1이 이겼습니다. Player2은 분발하세요!🗡️')
  elif df.loc['TOTAL SCORE', 'Player1'] < df.loc['TOTAL SCORE', 'Player2'] :
    print('🏆Player2이 이겼습니다. Player1은 분발하세요!🗡️')
  else :
    print('🏋️비겼습니다. 둘 다 분발하세요.🏋️')