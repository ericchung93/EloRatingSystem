# EloRatingSystem
A simple demonstration of common matchmaking systems and how they update after a win or loss. Such a system can be used to rate the skill level in competitor vs. competitor games like chess, football, tennis, and even video game ladders.
## Elo takes two factors into consideration:
1. Performance of each player/team is a normal distribution of random variables
2. The mean value of players/teams irrespective of their performance in an individual game increases slowly.
## How the system works:
  This system is used to determine the outcome of a game by comparing Elo ratings, and is all based on probability. Players with a higher Elo rating have a higher probability of winning a game than players with a lower Elo rating.

  After the game, the winner takes points from the loser, thereby increasing the rating of the winner and decreasing the rating of the loser. This allows for the construction of a ranking ladder, common in many sports and games to determine overall skill level.

  If a highly-rated player wins, only a few points are transferred from the loser. However, if a lowly-rated player wins (commonly known as an upset), then a much larger number of points are transferred from the loser.
## Equations to build the system:
  Before any games are played (i.e. at the very beginning of a ladder) everyone begins with the same rating. For this demonstration, every player starts at a base rating of 1400. 

  To understand the extent to which a player is more likely to win based on rating, we use the following equations:

<p align="center"><img src="https://user-images.githubusercontent.com/26446009/130845658-5844f567-cb79-4fe9-901b-bfb75006ca6c.png">

<p align="center"><img src="https://user-images.githubusercontent.com/26446009/130845697-36dbe75a-6460-44ee-a38c-1131373c37d0.png">

  In this equation, EA and EB are the expectations of players A and B, respectively. Likewise, RA and RB stand for the current ratings of players A and B, respectively.
  
  Therefore, if Player A has an expectation of 0.85, the probability of this player winning against Player B is 85%. After a match, both players have their rating adjusted, whether the outcome exceeds or falls short of the expected score.

  The updated Rating for a player is represented in the following equation:

<p align="center"><img src="https://user-images.githubusercontent.com/26446009/130847350-bf869e64-a347-436f-b40d-5ebdf362bc17.png">

  In this equation, R'A is the updated rating of player A; K is an arbitrary constant to adjust how strongly a match influences player rating; SA represents the actual score in the match. A '1' is usually given for wins, a '0' for losses, and a '0.5' may be given for ties. This allows for games like chess, where draws are common, to still have an effect on player rating.

## How this application works
  This application stores a list of players and their ratings in a list. Currently, the "default.csv" list serves as a demonstration. 

  The application will randomly draw two opponents from the list to match against eachother and record the updated ratings as a result of that match. Currently, wins and losses are decided randomly, giving both players equal probability of victory.

  Depending on the value set for the variable 'n', the application can run any number of simulations and will provide a finalized ladder based on the results of all of the comparisons, from highest rating to lowest.

