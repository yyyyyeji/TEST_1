import pandas as pd
class ScoreBoard: # 스코어보드 만드는 클래스
    @staticmethod
    def score():
        df = pd.DataFrame(columns=['Player1', 'Player2'], index=['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Bonus', 'Four_of_a_kind', 'Full_House',
            'Little_Straight', 'Big_Straight', 'Yacht', 'Choice','TOTAL SCORE'])
        df = df.fillna(0)
        return df