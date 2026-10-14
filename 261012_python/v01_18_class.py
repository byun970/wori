# 여러분들만의 클래스 정으
# 속성 3개 이상
# 메서드 2개 이상
# 객체 2개 이상

class Champion:
    def __init__(self, name, role, skill, gender):
        self.name = name
        self.role = role
        self.skill = skill
        self.gender = gender
    def attack_q(self):
        print(f"{self.name} Q스킬 사용!")
    def attack_w(self):
        print(f"{self.name} W스킬 사용!")
    def attack_e(self):
        print(f"{self.name} E스킬 사용!")
    def attack_r(self):
        print(f"{self.name} R스킬 사용!")

yone = Champion("요네", "전사", "검술", "남성")
ahri = Champion("아리", "마법사", "마법", "여성")
yone.attack_q()
ahri.attack_w()