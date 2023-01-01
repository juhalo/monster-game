import pygame
import random

class Cashmoney:
    def __init__(self):
        pygame.init()
        # The specs of the display
        self.width = 640
        self.height = 480
        self.window = pygame.display.set_mode((self.width, self.height))
        # The name of the game
        pygame.display.set_caption('Robot vs Monster')
        #The font used
        self.font = pygame.font.SysFont('Arial', 24)
        self.enter = False
        # Get the pictures used
        self.load_pics()
        self.start_diff = 0
        # At start the ruleset/difficulty are chosen, see the screen to know which buttons to press.
        self.set_ruleset()


    def load_pics(self):
        self.pics = []
        for name in ['robot', 'coin', 'monster']:
            self.pics.append(pygame.image.load(name + '.png'))

    def set_ruleset(self):
        # This can take values 0,1,2,3 and determines which ruleset is used for the game, 0 means nothing has been set
        self.ruleset = 0
        # Ruleset where you bounce, but don't remove the monster when hitting underside of it
        self.rule_bounce = False
        # Ruleset where you remove the monster if you hit it from below
        self.rule_remove = False
        # Ruleset where you replace the monster with coin if you hit it from below
        self.rule_replace = False
        while True:
            self.window.fill((0,0,0))
            rules = []
            rules.append(self.font.render('Choose from 3 different rulesets:', True, (255,0,0)))
            rules.append(self.font.render('1. Press 1 for the bounce ruleset', True, (255,0,0)))
            rules.append(self.font.render('2. Press 2 for the remove ruleset', True, (255,0,0)))
            rules.append(self.font.render('3. Press 3 for the replace ruleset', True, (255,0,0)))
            rules.append(self.font.render('The rules for these will be introduced soon, pick one for now', True, (255,0,0)))
            rules.append(self.font.render('Try each for a whole new experience', True, (255,0,0)))
            rules.append(self.font.render('You can return to this screen at any point by pressing F1', True, (255,0,0)))
            rules.append(self.font.render('You can exit the game at any time by pressing Esc', True, (255,0,0)))
            y = 50
            for rule in rules:
                if rule == rules[-3]:
                    y += 25
                self.window.blit(rule, (30, y))
                y += 25
            pygame.display.flip()
            # Check if F1 is pressed
            self.check_em()
            if self.enter == True:
                break
            if self.rule_bounce:
                self.ruleset = 1
                self.set_diff()
            if self.rule_remove:
                self.ruleset = 2
                self.set_diff()
            if self.rule_replace:
                self.ruleset = 3
                self.set_diff()

    def set_diff(self):
        # This tells potential difficulties and allows the player to choose which one they like
        self.start_diff = 0
        while True:
            self.window.fill((0,0,0))
            rules = []
            rules.append(self.font.render('Choose from the following difficulties:', True, (255,0,0)))
            rules.append(self.font.render('Press 4 for the easy difficulty', True, (255,0,0)))
            rules.append(self.font.render('Press 5 for the medium difficulty', True, (255,0,0)))
            rules.append(self.font.render('Press 6 for the hard difficulty', True, (255,0,0)))
            rules.append(self.font.render('Press 7 for the brutal difficulty', True, (255,0,0)))
            y = 50
            for rule in rules:
                self.window.blit(rule, (30, y))
                y += 25
            pygame.display.flip()
            # Check if 4,5 or 6 is pressed
            self.check_em()
            if self.start_diff != 0:
                self.we_go_again()
                self.rules()

    def rules(self):
        # Tells the rules to the player, the rules depend on the chosen ruleset
        self.startto = False
        while True:
            self.window.fill((0,0,0))
            rules = []
            rules.append(self.font.render('Rules (for the chosen ruleset):', True, (255,0,0)))
            rules.append(self.font.render('1. You have 3 lives, miss a coin and you lose one', True, (255,0,0)))
            rules.append(self.font.render('2. Touch a monster and you lose all of them, unless a rule disagrees', True, (255,0,0)))
            rules.append(self.font.render('3. Collecting coins gives points', True, (255,0,0)))
            rules.append(self.font.render('4. Jumping on a head of a monster makes it disappear', True, (255,0,0)))
            if self.ruleset == 1:
                rules.append(self.font.render('5. Jumping on the underside of a monster bounces you back', True, (255,0,0)))
            elif self.ruleset == 2:
                rules.append(self.font.render('5. Jumping on the underside of a monster removes the monster', True, (255,0,0)))
            elif self.ruleset == 3:
                rules.append(self.font.render('5. Jumping on the underside of a monster replaces it with a coin', True, (255,0,0)))
            rules.append(self.font.render('6. Left = a, Right = d, Jump = w, Quit the game = Esc',True, (255,0,0)))
            rules.append(self.font.render('7. Every 30 second you get an extra life if you have less than 3',True,(255,0,0)))
            rules.append(self.font.render('PRESS F2 TO START', True, (255,0,0)))
            y = 50
            for rule in rules:
                if rule == rules[-1]:
                    y += 25
                self.window.blit(rule, (30, y))
                y += 25
            pygame.display.flip()
            # Check if F1 is pressed
            self.check_em()
            if self.startto == True:
                self.game()

    def check_em(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.enter = True
                    # This resets the values to default or creates the default values
                    self.we_go_again()
                    # Start the game
                    self.set_ruleset()
                if event.key == pygame.K_F2:
                    self.startto = True
                if event.key == pygame.K_a:
                    self.left = True
                if event.key == pygame.K_d:
                    self.right = True
                if event.key == pygame.K_w:
                    self.up1 = True
                    # Used to setup gravitation/jump
                    if self.y_r+self.pics[0].get_height()>=self.height:
                        self.v_up = -1.5*self.v
                        self.y_r += self.v_up
                        self.jump_num = 1
                if event.key == pygame.K_1:
                    self.rule_bounce = True
                    # This resets the values to default or creates the default values
                    if self.ruleset == 0:
                        self.we_go_again()
                if event.key == pygame.K_2:
                    self.rule_remove = True
                    # This resets the values to default or creates the default values
                    if self.ruleset == 0:
                        self.we_go_again()
                if event.key == pygame.K_3:
                    self.rule_replace = True
                    # This resets the values to default or creates the default values
                    if self.ruleset == 0:
                        self.we_go_again()
                if event.key == pygame.K_4:
                    if self.start_diff == 0:
                        self.start_diff = 1
                if event.key == pygame.K_5:
                    if self.start_diff == 0:
                        self.start_diff = 2
                if event.key == pygame.K_6:
                    if self.start_diff == 0:
                        self.start_diff = 3
                if event.key == pygame.K_7:
                    if self.start_diff == 0:
                        self.start_diff = 4
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_F1:
                    self.enter = False
                if event.key == pygame.K_a:
                    self.left = False
                if event.key == pygame.K_d:
                    self.right = False
                if event.key == pygame.K_w:
                    self.up1 = False
                if event.key == pygame.K_1:
                    self.rule_bounce = False
                if event.key == pygame.K_2:
                    self.rule_remove = False
                if event.key == pygame.K_3:
                    self.rule_replace = False
            if event.type == pygame.QUIT:
                exit()

    def we_go_again(self):
        # For now the difficulty means how fast the monsters will move and how often they spawn. Will probably add more settings for this. Changes over time
        self.diff = 1
        # List of the coins
        self.list_c = []
        # List of the monsters
        self.list_m = []
        # x_r = the x-coordinate of the robot (You), y_r = the y-coordinate, these are the initial coordinates
        self.x_r = 0
        self.y_r = self.height-self.pics[0].get_height()
        # Setup the clock
        self.clock = pygame.time.Clock()
        # The speed of robot, the coins, the monsters (speed of coins = speed of monsters)
        self.v = 3+0.25*(self.start_diff-1)
        self.v_c = self.diff+0.25*(self.start_diff-1)
        # Amount of points
        self.points = 0
        # Set up the directions
        self.right = False
        self.left = False
        self.up1 = False
        self.enter = False
        # Lives
        self.lives = 3
        # Terms related to the gravity that the robot faces when jumping
        self.grav = 0.1+0.02*(self.start_diff-1)
        self.v_up = 0
        # Number of jumps before hitting the ground, which makes this number zero
        self.jump_num = 0
        # Ticks
        self.tick_num = 0

    def draw_window(self):
        # We want a dark color for the background but not as dark as our monster
        self.window.fill((25,25,25))
        self.window.blit(self.pics[0], (self.x_r, self.y_r))
        # ADD coins and monsters
        for coin in self.list_c:
            self.window.blit(self.pics[1], (coin[0], coin[1]))
        for monster in self.list_m:
            self.window.blit(self.pics[2], (monster[0], monster[1]))
        txt = []
        txt.append(self.font.render(f'Points: {self.points}', True, (255,0,0)))
        txt.append(self.font.render(f'Lives: {self.lives}',True,(255,0,0)))
        txt.append(self.font.render(f'Time: {(self.diff-1)*30+self.tick_num/60:.0f}',True,(255,0,0)))
        txt.append(self.font.render(f'Level: {self.diff}',True,(255,0,0)))
        y = 25
        for text in txt:
            self.window.blit(text, (self.width-text.get_width()-10,y))
            y += 25
        pygame.display.flip()

    def three_fiddy(self):
        # Note here how the difficulty changes a lot of things
        # First we see if the lists of monsters and coins have to be changed
        # we'll use random-module to randomize the process.
        # Of importance is to realize that the randomization of coins is made such
        # that it's always (in theory) possible for a player to catch the coins while
        # only moving in x-direction, if course the added element of monsters might make
        # this impossible.

        # Add potential coin
        self.add_c()
        # Add potential monster
        self.add_m()
        # Now finally move the robot
        self.move_r()
        # Move the coins
        self.move_c()
        # Move the monsters
        self.move_m()
        #Check if robot touched underside of a monster
        self.bounce()
        # Check if robot catches a monster
        self.catch()
        # Check if monster touches the robot but roboto doesn't catch the monster, resulting in a loss
        self.touch()

    def add_c(self):
        # We don't want monsters and coins to overlap because this would make the game too hard
        if random.randint(0,59) == 0:
            add_coin = True
            x_c = random.randint(0,self.width-self.pics[1].get_width())
            y_c = -self.pics[1].get_height()
            for monster in self.list_m:
                    if abs(x_c+self.pics[1].get_width()/2-monster[0]-self.pics[2].get_width()/2)<=(self.pics[1].get_width()+self.pics[2].get_width())/2:
                        # There WAS a problem here, might work now
                        if monster[1]<0:
                            add_coin = False
            if add_coin:
                if len(self.list_c)==0:
                    self.list_c.append([x_c,y_c])
                else:
                    x_b = self.list_c[-1][0]
                    y_b = self.list_c[-1][1]
                    if x_c-x_b < 0 and abs(x_c-x_b-self.pics[0].get_width())<=self.v*y_b/self.v_c:
                        self.list_c.append([x_c,y_c])
                    elif abs(x_c-x_b)<=self.v*y_b/self.v_c:
                        self.list_c.append([x_c,y_c])

    def add_m(self):
        # We don't want monsters and coins to overlap because this would make the game too hard
        # Used pass as a placeholder (might put something here later)
        if self.diff < 1:
            pass
        else:
            # This used to be: if random.randint(0,300/self.diff)==0:
            # Scaled too fast with difficulty, therefore the following was used
            if self.start_diff == 1:
                a = (self.diff+2)/3
            elif self.start_diff == 2:
                a = (self.diff+2)/2
            elif self.start_diff == 3:
                a = self.diff+1
            elif self.start_diff == 4:
                a = 1.5*self.diff+1
            if random.randint(0,300//a)==0:
                add_mon = True
                x_m = random.randint(0,self.width-self.pics[2].get_width())
                y_m = -self.pics[2].get_height()
                # This checks whether or not the potential monster overlaps with a coin (too much), doesn't currently work maybe because doesn't account for v_c
                for coin in self.list_c:
                    if abs(x_m+self.pics[2].get_width()/2-coin[0]-self.pics[1].get_width()/2)<=(self.pics[2].get_width()+self.pics[1].get_width())/2:
                        # And here
                        if coin[1]<0:
                            add_mon = False
                if add_mon:
                    self.list_m.append([x_m,y_m])


    def move_r(self):
        if self.left and self.x_r-self.v>=0:
            self.x_r -= self.v
        if self.right and self.x_r+self.v+self.pics[0].get_width()<= self.width:
            self.x_r += self.v
        if self.y_r+self.v_up+self.pics[0].get_height()>=self.height:
            self.y_r = self.height-self.pics[0].get_height()
            self.v_up = 0
        elif self.v_up < 0 and self.y_r-self.v_up <=0:
            self.v_up = -self.v_up
            self.y_r = 0
        else:
            self.v_up += self.grav
            self.y_r += self.v_up


    def move_c(self):
        for coin in self.list_c:
            coin[1] += self.v_c
            if abs(self.x_r+self.pics[0].get_width()/2-coin[0]-self.pics[1].get_width()/2)<=(self.pics[0].get_width()+self.pics[1].get_width())/2:
                if self.y_r-self.pics[1].get_height()<=coin[1]<=self.y_r+self.pics[0].get_height():
                    self.list_c.remove(coin)
                    self.points += 1
            if coin[1]>=self.height and self.lives>0:
                self.lives -= 1
                self.list_c.remove(coin)

    def move_m(self):
        for monster in self.list_m:
            if monster[1]+self.pics[2].get_height()+self.v_c<self.height:
                monster[1] += self.v_c
            else:
                if monster[0]<self.x_r:
                    monster[0] += self.v_c
                elif monster[0]>self.x_r:
                    monster[0] -= self.v_c

    def bounce(self):
        # Note: change of difficulty during bounce back can mess things up, I have tried to take this into account by checking if robot could reach the bottom
        # before the difficulty changes, if this doesn't happen, I have increased robots speed to compensate
        for monster in self.list_m:
            # Checks if player and a monster overlap in x-coordinate, doesn't take into account self.v currently, must be fixed in the future
            if abs(self.x_r+self.pics[0].get_width()/2-monster[0]-self.pics[2].get_width()/2)<=(self.pics[0].get_width()+self.pics[2].get_width())/2:
                a = 1
                # The following factor is always bigger than the relative increase in speed when the difficulty increases, calculate for different values of
                # self.diff to convince yourself of this fact (hint: the speeds for self.v_c are 1, 1.25, 1.5, 1.75; and therefore the ratios are the next
                # speed divided by the previous speed; the following formula is this ratio rounded down to two decimals plus +0.01, i.e. always bigger than
                # the ratio)
                # Used to be: d = ((100+25*self.diff)//(1+0.25*(self.diff-1)))/100+0.01
                # Idea: d = ((100+25*(self.diff+self.start_diff-1))//(1+0.25*((self.diff+self.start_diff-1)-1)))/100+0.01
                d = ((100+25*(self.diff+self.start_diff-1))//(1+0.25*((self.diff+self.start_diff-1)-1)))/100+0.01
                # Calculate how many ticks there are before the difficulty changes
                t = 60*30-self.tick_num
                # The following calculates the new speed for the player when hitting underside of monster
                if monster[1]+self.pics[2].get_height()-self.y_r <= abs(self.v_c-self.v_up) and self.y_r <= monster[1]+self.pics[2].get_height():
                    if self.v_up <= 0 and 0.75*abs(self.v_up)>self.v_c:
                        if 0.75*abs(self.v_up)*t+self.y_r+self.pics[0].get_height()<self.height:
                            a = d
                        self.v_up = 0.75*a*abs(self.v_up)
                    elif self.v_up <= 0 and abs(self.v_up)>self.v_c:
                        if abs(self.v_up)*t+self.y_r+self.pics[0].get_height()<self.height:
                            a = d
                        self.v_up = a*abs(self.v_up)
                    else:
                        self.v_up = d*self.v_c
                    # Update the y-coord of player to 1 pixel below the monster to make this work with other functions involving the monster (also makes sense)
                    self.y_r = monster[1]+self.pics[2].get_height()+1
                    if self.ruleset == 2 or self.ruleset == 3:
                        if self.ruleset == 3:
                            self.list_c.insert(0,[monster[0],monster[1]])
                        self.list_m.remove(monster)


    def catch(self):
        for monster in self.list_m:
            # This tries to fix the problem of going too fast and not being able to kill monster due to it, if moves very fast (more than +-10) this wont help
            # The +-abs(self.v_up) is there to make sure that the speed of robot doesn't cause monster to kill the robot instantly
            if self.y_r+self.pics[0].get_height()-5-abs(self.v_up) <= monster[1] <= self.y_r+self.pics[0].get_height()+5+abs(self.v_up):
                if abs(self.x_r+self.pics[0].get_width()/2-monster[0]-self.pics[2].get_width()/2)<=(self.pics[0].get_width()+self.pics[2].get_width())/2:
                    self.list_m.remove(monster)
                    # Makes the robot jump when killing a monster, give breathing room when many monsters next to each other
                    # Used to be:
                    #self.v_up += -1.5*self.v*(1+self.jump_num/2)
                    if self.jump_num == 1:
                        self.v_up = -(1.5)*abs(self.v_up)
                    else:
                        self.v_up = -(1.0+1/4)*abs(self.v_up)
                    # This might cause problems
                    self.y_r += self.v_up
                    self.jump_num += 1


    def touch(self):
        # The +7's are to make it more generous to the player, also to account for the empty space in the png-files
        for monster in self.list_m:
            if self.y_r+self.pics[0].get_height()<self.height:
                if monster[1]-self.pics[0].get_height()<self.y_r<=monster[1]+self.pics[2].get_height():
                    if abs(self.x_r+self.pics[0].get_width()/2-monster[0]-self.pics[2].get_width()/2)+7<=(self.pics[0].get_width()+self.pics[2].get_width())/2:
                        self.lives = 0
            elif self.y_r+self.pics[0].get_height()>=self.height:
                if self.y_r<=monster[1]+self.pics[2].get_height():
                    if abs(self.x_r+self.pics[0].get_width()/2-monster[0]-self.pics[2].get_width()/2)+7<=(self.pics[0].get_width()+self.pics[2].get_width())/2:
                        self.lives = 0

    def lost(self):
        # All the functions etc. that are executed upon losing a game
        if self.lives == 0:
            # Setting these up for the up-coming while loop
            gametypes = ['bounce','remove','replace','joke']
            difficulties = ['easy', 'medium', 'hard', 'brutal']
            n = 0
            points = self.points
            diff = self.diff
            tick_num = self.tick_num
            ruleset = self.ruleset
            start_diff = self.start_diff
            # Create or open the file that has all the scores stored, used try-except to try to fix potential problems with the scores.txt file
            #gametypes = ['bounce','remove','replace','joke']
            #thefile = f'{gametypes[self.ruleset-1]}.txt'
            thefile = f'scores.csv'
            try:
                with open(thefile, 'a') as file:
                    file.write(f'{points};{ruleset};{start_diff}\n')
                score_list = []
                # Reads the file and extracts the scores
                with open(thefile, 'r') as file:
                    for row in file:
                        parts = row.strip().split(';')
                        if int(parts[1]) == ruleset and int(parts[2]) == start_diff:
                            score_list.append(int(parts[0]))
                score_list.sort(reverse=True)
                n = 1
                for score in score_list:
                    if points == score:
                        break
                    n += 1
            except:
                pass
            self.we_go_again()
            # The endscreen
            while True:
                self.window.fill((0,0,0))
                txt = []
                txt.append(self.font.render(f'For the ruleset ({gametypes[ruleset-1]}) and difficulty ({difficulties[start_diff-1]}):',True,(255,0,0)))
                if n == 1:
                    txt.append(self.font.render(f'NEW HIGHSCORE!', True, (255,0,0)))
                elif n == 0:
                    pass
                else:
                    txt.append(self.font.render(f'There are {n-1} scores better than yours!', True, (255,0,0)))
                    txt.append(self.font.render(f'The best score is {score_list[0]}', True, (255,0,0)))
                txt.append(self.font.render(f'Your score was {points}', True, (255,0,0)))
                txt.append(self.font.render(f'Your lasted {(diff-1)*30+tick_num/60:.0f} seconds',True,(255,0,0)))
                txt.append(self.font.render(f'Press Esc to quit', True, (255,0,0)))
                txt.append(self.font.render(f'Press F1 to restart', True, (255,0,0)))
                y = 100
                for text in txt:
                    if text == txt[-2]:
                        y += 25
                    self.window.blit(text, (self.width/2-text.get_width()/2,y))
                    y += 25
                pygame.display.flip()
                self.check_em()

    def diff_change(self):
        self.tick_num += 1
        # Difficulty increases by 1 every 30 seconds, some speeds etc. also change then (also monster spawn rate increases)
        if self.tick_num == 60*30:
            self.diff += 1
            self.tick_num = 0
            self.v += 0.25
            self.v_c += 0.25
            # Gravity has to increase a bit, otherwise the jumps become too slow as difficulty increases
            self.grav += 0.02
            # Player gets one more life if they survive 30 secs and they have less than 3 lives
            if self.lives<3:
                self.lives += 1

    def game(self):
        while True:
            # Check key presses that are relevant
            self.check_em()
            # Change the current state of the screen
            self.three_fiddy()
            # Draw the current state of the screen
            self.draw_window()
            # Check if the player lost
            self.lost()
            # Increase the difficulty if enough time has passed, also count the ticks
            self.diff_change()
            # Time the clock
            self.clock.tick(60)



if __name__ == "__main__":
    # Starts the class, i.e. the game screen
    Cashmoney()
