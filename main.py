# write your code here
def padel_court_cost(court_type) :
 if court_type == "indoor" :
    return 30
 elif court_type == "outdoor":
       return 20
 


 def rackets_cost(racket_brand):
    if racket_brand == "bullpadel":
       return(100)
    elif racket_brand == "Nox"
        return(140)
    elif racket_brand == "Siux":
        return(200)
    



 def padel_balls_cost(ball_boxes) :
     if ball_boxes == 1:
         return 2
     elif ball_boxes == 2:
         return 3.5
     elif ball_boxes == 3:
         return 5
     
     def padel_game_cost():
         type=(input("Enter the court type?"))
         brand=(input("Enter the racket brand"))
         ball=int(input("Enter the number of ball boxes"))

         total= padel_balls_cost(ball) + padel_court_cost(type) + rackets_cost(brand)
         return total
     print(padel_game_cost())
         
