#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:41:32 2020

@author: krishna
"""
from twitch.helix.api import TwitchHelix
import os
import sys
### Broadcast_ids of users


'''
list_layers={'Ninja':19571641,
'Aydan':120244187,
'Cloakzy':81687332,
'Dakotaz':39298218,
'DrDisrespect':17337557,
'HighDistortion':84752541,
'KingRichard':66691674,
'Lolitofdez':57793021,
'Mongraal':133705618,
'mrfreshasian':38594688,
'Myth':110690086,
'NICKMERCS':15564828,
'Ninja':19571641,
'Symfuhny':31688366,
'TimTheTatman':36769016,
'TSM_Daequan':127651530,
'TSM_Hamlinz':67143805,
'CouRageJD':106125347}
'''
list_layers = {'fortnite':55125740}



def get_links(response):
    all_links=[]
    for i in range(len(response)):
        item=response[i]
        try:
            link=item['url']
        except:
            continue
        all_links.append(link)
        print(link)
    return all_links



for player in list_layers.keys():
    filepath = 'fortnite/'+player+'.txt'
    fid = open(filepath,'w')
    for i in range(50):
        if i==0:
            client = TwitchHelix(client_id='******************************')
            response =client.get_clips(broadcaster_id=list_layers[player],page_size=100)
        else:
            next_cursor = response.cursor
            response =client.get_clips(broadcaster_id=list_layers[player],page_size=100,after=next_cursor)
        read_links = get_links(response)
        for row in read_links:
            fid.write(row+'\n')
    fid.close()

    

