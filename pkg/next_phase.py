import pandas as pd
class next_phase:
    def Bonus(df, player_name): # 상단 스코어 보드의 총합이 63점 이상이면 35점의 보너스 점수를 받는 메소드
        num = df[player_name].iloc[:6].sum()
        if num >= 63 :
            df.loc['Bonus', player_name] = 35
            return df
        else:
            pass

    def Total_Score(df,player_name): # 총합 계산 메소드
        num = df[player_name].iloc[:13].sum()
        df.loc['TOTAL SCORE', player_name] = num
        return df