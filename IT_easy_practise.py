#!/usr/bin/env python
# coding: utf-8

# In[26]:


def say_plan():
    print("旅行プランの提案")
say_plan()


# In[22]:


def say_m(money,eat,train,drink,gozoo,hotel):
    return money-eat-train-drink-gozoo-hotel
say_m(money=100000,eat=2000,train=3000,drink=600,gozoo=2000,hotel=4000)


# In[23]:


#夏季休暇をお財布と相談
coin=88400
if coin >= 75000:
    print("2泊3日の海外旅行")
elif coin >= 30000:
    print("2泊3日の国内旅行")
elif coin >= 5000:
    print("友人と映画館に行く")
else:
    print("ネットフリックス")

