# my python module to group functions like a library of resuable code or code 
# library that we make available to others
club = [["PSG", 136, "France"],
       ["MillWall",101,"England"],
       ["Milan",180,"Italy"]
       ]


def greeting(name):
  print("Hello, " + name + ", thanks for using my module")


def select_club(club_choice):
  result = club[club_choice][0]
  return result