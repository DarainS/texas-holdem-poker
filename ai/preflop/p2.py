import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Reshape, Flatten
from keras.optimizers import Adam
import rl


processor=rl.core.Processor()
env=rl.core.Env()
space=rl.core.Space()

nb_actions=['fold','call','raise']


agent=rl.agents.ddpg.DDPGAgent(nb_actions, actor, critic, critic_action_input, memory, gamma=0.99, batch_size=32, nb_steps_warmup_critic=1000, nb_steps_warmup_actor=1000, train_interval=1, memory_interval=1, delta_range=None, delta_clip=inf, random_process=None, custom_model_objects={}, target_model_update=0.001)