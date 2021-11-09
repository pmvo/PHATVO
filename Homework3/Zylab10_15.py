#Name: Phat Vo
#PSID: 2024127
#LAB 10.15

class Team:
    def __init__(self):
        self.name='none'
        self.team_wins=0
        self.team_losses=0
    def get_win_percentage(self):
        return self.team_wins/(self.team_wins+self.team_losses)

if __name__=="__main__":
    team=Team()
    team.name=input()
    team.team_wins=int(input())
    team.team_losses=int(input())

    if(team.get_win_percentage()>=0.5):
        print('Congratulations, Team {} has a winning average!'.format(team.name))
    else:
        print('Team {} has a losing average.'.format(team.name))