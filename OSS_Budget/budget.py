import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")






    def spending_mbti(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        food = sum(e.amount for e in self.expenses if "식" in e.category)
        transport = sum(e.amount for e in self.expenses if "교통" in e.category)
        shopping = sum(e.amount for e in self.expenses if "쇼핑" in e.category or "의류" in e.category)

        total = food + transport + shopping
        if total == 0:
            print("분석할 지출이 충분하지 않습니다.\n")
            return

        traits = []
        traits.append("F" if food / total > 0.4 else "T")  # 감성소비 vs 실용소비
        traits.append("S" if shopping / total > 0.3 else "N")  # 현실/감각 vs 절제/이상
        traits.append("P" if transport / total < 0.2 else "J")  # 즉흥 vs 계획

        mbti = "".join(traits)

        print("\n [소비 성향 분석 결과]")
        print(f"당신의 소비 MBTI는: {mbti}")

        types = {
        "FSP": "감성적이고 즉흥적인 소비자",
        "TNP": "실용적이지만 자유로운 소비자",
        "FSJ": "감각적이고 계획적인 소비자",
        "TNJ": "이성적이고 전략적인 소비자",
        }
        
        print(f"→ {types.get(mbti, '독특한 소비 성향을 가졌네요!')}\n")