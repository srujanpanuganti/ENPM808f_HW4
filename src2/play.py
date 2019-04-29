# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:10:35 2019

@author: Srujan Panuganti
"""

import numpy as np
#import itertools 
from operator import add
#import random
from dots_and_boxes import dots_and_boxes as dbs
import q_algorithm
from agent import q_agent

class play:
    
    def __init__(self, env:dbs,agent1:q_agent,agent2 : q_agent):
        
        self.env = env
        self.agent1 = agent1
        self.agent2 = agent2
        
    def play_game(self, q_class):

        agent1_act = 0
        #agent1_prev_state = self.env.current_state
        agent1_tot_boxes = 0

        agent2_act = 0
        #agent2_prev_state = self.env.current_state
        agent2_tot_boxes = 0
        
        pos_act  = []
        
        while not self.env.game_over:

            my_turn1= 1
            
            
            while my_turn1 > 0 and not self.env.game_over:

                print('333')
                
                reward1 = 0
                 
                #pos_act = self.env.possible_actions_
                print('curr',self.env.current_state)
                
                print('pos',self.env.possible_actions_)
                #previous_state = self.env.current_state
                agent1_act = self.agent1.get_action(q_class,self.env.current_state,self.env.possible_actions_)
                
                print(agent1_act)
                
                current_state1,reward1, previous_state1 , number_of_boxes_complete1, is_box_created1  = self.env.do_action(agent1_act)
                
                agent1_tot_boxes += number_of_boxes_complete1
                
                prev_state_action1 = [previous_state1,agent1_act]
                
                q_class.q_update(self, prev_state_action1, self.env.current_state ,reward1, self.env.possible_actions_)

                my_turn1 = is_box_created1
            
            if self.env.game_over:
                break
            
            my_turn2 = 1

            while my_turn2 > 0 and not self.env.game_over:


                reward2 = 0
                 
                #previous_state = self.env.current_state
        
                agent2_act = self.agent2.get_action(q_class,self.env.current_state,self.env.possible_actions_)
                 
                current_state2,reward2, previous_state2 , number_of_boxes_complete2, is_box_created2   = self.env.do_action(agent2_act)
                
                agent2_tot_boxes += number_of_boxes_complete2
                
                prev_state_action2 = [previous_state1,agent1_act]
                
                q_class.q_update(self, prev_state_action2, self.env.current_state ,reward2, self.env.possible_actions_)
                
                my_turn2 = is_box_created2

        
        if agent1_tot_boxes == agent2_tot_boxes:
            winner = 0
        elif agent1_tot_boxes > agent2_tot_boxes:
            winner = 1
        elif agent1_tot_boxes < agent2_tot_boxes:
            winner = 2
        
        if winner == 1:
            q_class.q_update(self, prev_state_action1, self.env.current_state ,reward1, self.env.possible_actions_)
            print('agent 1 won')

        elif winner == 2:
            q_class.q_update(self, prev_state_action2, self.env.current_state ,reward2, self.env.possible_actions_)
            print('agent 2 won')

        else:
            print('draw')
         
        return winner, q_class

# =============================================================================
#                 
#     def who_won_the_game(score1, score2):
#         
#         winner = None
#         
#         if score1 > score2:
#             winner = str(player1)
#         elif score1 == score2:
#             winner = str(draw)
#         else:
#             winner = str(player2)
#         
#         return winner
# 
# 
# 
#     def turn(action):
#         
#         previous_state = game.current_state
#         
#         #current_action = player2.current_action
#         old_state_action = [previous_state,current_action]
#         
#         _, possible_actions = game.possible_actions()
#         
#         current_state, reward, previous_state= game.do_action(current_action)
#         
#         action = Q_agent.q_update(old_state_action,current_state,reward,current_action,possible_actions)
#         
#         if turn_change == False:
#             turn(action)
#         
#         if reward == 1:
#             turn_change = False
#         elif reward == 5:
#             turn_change = False
#             game_over = True
#         else:
#             turn_change = True
# 
#         
#     def play_game():
#         reward = 0
#         
#         previous_state = env.
#         current_action = epsilon_greedy()
# 
#         game = dots_and_boxes(grid_size = (2,2))
# 
#         x, y = turn(action)
# 
#         if game_over == True:
#             winner = who_won_the_game()
#         
#         return winner, Q_agent.q_table
# 
#             
# 
# =============================================================================