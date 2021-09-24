import random
import discord
from typing import List

import numpy as np
from discord import ChannelType, client

lunchbox_users = []
group_list = []

# adds user to lunchbox list if not already on it
# returns 1 if added, 0 if not
def add_user(user):
    if (user not in lunchbox_users):
        lunchbox_users.append(user)
        return 1
    else:
        return 0

def remove_user(user):
    if (user in lunchbox_users):
        lunchbox_users.remove(user)
        return 1
    else:
        return 0

def generate_group(members: List, user, group_population: int):
    # if desired group size is more than interested people, reduce group size 
    if len(lunchbox_users) < group_population:
        group_population = len(lunchbox_users)
    
    random.shuffle(members)
    # if user who generated group is on list, add them to group and reduce size by 1
    if (user in lunchbox_users):
        lunch_budies = [user]
        group_population -= 1
        lunchbox_users.remove(user)
    
    for i in range(group_population):
        person = random.choice(lunchbox_users)
        lunch_budies.append(person)
        lunchbox_users.remove(person)
    # add new generated list to list of generated groups
    group_list.append(lunch_budies)
    return lunch_budies


def get_channel_by_name(channels, name):
    for c in channels:
        if c.name == name:
            return c
    return None


def get_channel_by_position(channels, index):
    for c in channels:
        if c.position == index:
            return c
    return None


