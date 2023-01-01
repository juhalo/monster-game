# monster-game

## NOTE

This project was originally done without git and therefore there are commits that add a lot. The current goal is to evolve this and this is why the repo has been created.

## Description

This project is a 2d game created with Pygame. The goal of the game is to gather as many coins as possible while avoiding letting too many coins fall below the screen.

## Gameplay

Regardless of the rule set, there are things that are universal: the player has three lives and they lose one whenever a coin falls below the floor or lose all of them if hitting a monster in a way the rule set does not allow. Once certain amount of time has passed, the player gains a new life if the player's life count was below three lives. Monsters fall from the sky and they can be killed by jumping on the their top-side. Coins also fall from the sky and the amount of coins gathered determines the score of the game. Player can bounce of a monster's head. The game keeps track of the scores for each rule type and difficulty level.

### Rule Sets

There are currently three different rule sets: bounce, remove, and replace. With bounce rule set, the monsters can only be removed by hitting their head and hitting them from below when they are descending, causes player to bounce back. With remove rule set, the monsters are also removed when hitting a descending monster from below (but not from sides). With replace rule set, a monster is replaced with a coin when a player when jumping on the bottom of the monster.

### Difficulty Levels

There are four difficulty levels: easy, medium, hard, and brutal. The difficulty level affects the speed at which monsters spawn and move. It should be noted that these also increase as time passes and therefore difficulty levels can be seen as a way of determining the starting position, i.e. you will reach the same difficulty eventually even when playing with easy difficulty as you would when starting with brutal.

## Example game (with Bounce+Brutal)

![gif](https://github.com/juhalo/monster-game/blob/main/img/output11.gif)