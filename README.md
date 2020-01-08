# The Monty Hall Problem

## Preface
I have read about [The Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) many times over the years, it’s very famous, but no matter how many times I read the problem and various explanations I couldn’t understand the advantage in switching doors. Many of the explanations weren't clear and some of them were simply wrong. This is my effort to provide a clear and accurate explanation.


## Introduction / Problem Background
The Monty Hall problem is a probability conundrum famously personified in a TV game show format.

A contest is presented with three doors. Behind two doors is a booby prize, traditionally a goat, and behind a third door is a highly desired prize, typically a sports car.

The contestant chooses one of the three doors thinking that they will have a one in three chance of choosing the sports car. Monty, the game show host, opens a different one of the doors and reveals a goat. It is really important to note here that Monty knows what is behind each door and will always reveal a goat. Some explanations I have seen on this problem either don’t state whether the host knows what each door masks and others have explicitly stated that the host doesn’t know, or it doesn’t matter if they know and it’s random. The host must know what is behind each door and will reveal a goat, otherwise they may reveal the car and the game is over and there is no conundrum.

Two out of three doors mask a goat and one goat has been revealed by the host opening a door other than the initial door chosen by the contestant. Of the remaining two closed doors (one of which was the contestant’s original choice); one definitely masks a goat and one definitely masks the sports car. The contestant is asked if they would like to change their original door choice to the other remaining unopened door or stick with their initial choice, before their door of choosing is opened and their prize revealed.

The conundrum unfolds after the contestant initially had a one in three chance of choosing the sports car before any doors were opened, and after one of the goat masking doors has been opened, they are offered the chance to switch to the remaining closed door or stick with their initial choice of door; The contestant believes that they still have a one in three chance of either their initial choice in door or the other remaining door masking the sports car, meaning that there is no benefit in switching doors after the first door is opened. Alternatively, they may think they have a one in two chance because they have two doors to choose from instead of three and again, there is no benefit in switching the other closed door.

Counter intuitively though, the contestant actually has a two in three chance of winning the sports car after the first door has been revealed if they switch their choice of door from their initial choice to the other unopened door, and only a one in three chance of revealing the sports car if they don’t switch doors and request their initial choice of door be opened.


## Answer Criterion & Modern Exclusions
It has been said before that actually some people may want the goat (as per the [XKCD episode](https://www.xkcd.com/1282/)) perhaps as a kind of joke, to flip the probability of The Monty Hall problem around and imply that actually, two out of three doors would reveal a highly sought after item or that the probability was always in the players favour if they decided which outcome they prefer most rather than being told which outcome is “best” for them.

I believe that in our modern times this is an actual truth and not any kind of joke. Many people live car-less lives to reduce their CO2 emissions, and in an effort to be more sustainable would appreciate a free garden lawn mower which also produces milk and fertiliser. But as above, we’ll assume the sports car is the “best” prize.

The desire in this exercise is to explain the original probability problem, it is assumed that the unwanted prize behind two doors is still a goat and that the highly desirable prize behind only one door is a sports car, for authenticity and consistency with the problem in its original unadulterated form.

## Explanation
Initially a contestant chooses a door from a set of three doors. The likelihood of the contestant choosing the door masking the sports car at this point is one in three. The likelihood of the contestant choosing a door which masks a goat is two in three.

Monty opens a different door to the contestant’s choice and a goat is revealed. Hopefully the goat will have turned around and will have its bum facing the audience or it will be chewing on the set, for added humour.

Now that only two doors remain unopened the chance of the sports car being behind either door has now increased to one in two however the contestant’s initial choice was based on a one in three chance when all three doors were closed. By opening one of the doors to reveal a goat, and because Monty knew the door opened was masking a goat, a more likely location of the sports car has been implicitly revealed.

The contestant is now given a second chance to choose which door they want to open, they can choose to see what is behind the door they originally chose when all three doors where closed, or they can switch to see what is behind the other remaining closed door.

Four possible scenarios can unfold depending on whether the player chooses to switch their choice in door or not:

1. Switching == Win  
If the contestant initially chose a door which masks a goat, and Monty reveals the other goat, the remaining door must mask the sports car. In this case the “best” choice for the contestant is to switch to the third door before their chosen door is opened.

2. Sticking == Lose  
If the contestant initially chose a door which masks a goat, and Monty reveals the other goat, the remaining door must mask the sports car. Not switching will result in the contestant "losing" the game.

3. Switching == Lose  
If the contestant initially chose the door which masks the sports car, and Monty reveals a goat, the third door masks another goat. Switching to the third door will result in the contestant "losing" the game.

4. Sticking == Win  
If the contestant initially chose the door which masks the sports car, and Monty reveals a goat, the third door masks another goat. Sticking with their initial choice in door will cause the contestant to "win".

The problem regarding the choice to switch is knowing if the initially chosen door masks a goat or the sports car. This can't be known. However, the reason that the “best” strategy for the player is to always switch is that scenario 1 above will play out two out of three times when switching doors, meaning that the switching strategy gives a two out of three probability of "winning". The contestant will have initially chosen a door which masks a goat two out of three times, Monty will then always reveal the other goat, meaning that two out of three times the sports car is behind the third door thus switching doors before they are opened yields a two out of three probability of “winning”. Equally in the "sticking" scenario the player will lose two out of three times because two out of three times they will have initially chosen a door which masks a goat.

## Example
The output from the script is below. It runs 10,000 rounds of the game by default and it shows that the player wins two out of three games on average when they switch doors:
```bash
$./monty_hall.py

Results when a known loosing door is revealed by the host:
Player does not switch door
Player lost (original choice was incorrect) for 66.93% (6693/10000) games
Player won (original choice was correct) for 33.07% (3307/10000) games

Player switches door
Player lost (original choice was correct) for 33.29% (3329/10000) games
Player won (original choice was incorrect) for 66.71% (6671/10000) games
```

I have seen discrepancies on the Internet regarding whether Monty reveals a known loosing door (i.e. a door masking a goat) or a random door. Just to put this point of contention to rest, the script output above shows what happens when Monty opens a door known to mask a goat. The script output below shows what happens when Monty opens a door at random. It shows that the player cannot exceed a success rate of one in three and that the player has the same one in three chance of winning regardless of whether they switch doors or stick with their original choice:
```bash
Results when a random door is revealed by the host:
Player does not switch door
Player lost (original choice was incorrect) for 66.77% (6677/10000) games
	->Host accidently revealed winnning door for 33.41% (3341/10000) games
Player won (original choice was correct) for 33.23% (3323/10000) games

Player switches door
Player lost (original choice was correct) for 33.08% (3308/10000) games
	->Host accidently revealed winnning door for 33.13% (3313/10000) games
Player won (original choice was incorrect) for 33.79% (3379/10000) games
```
