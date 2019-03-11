import os
import stat
import random
from argparse import ArgumentParser

import portpicker
from mlagents_envs import UnityEnvironment

# Binary we want to work with
binary_path = os.path.abspath('gridworld/gridworld.x86_64')

# chmod +x binary
st = os.stat(binary_path)
os.chmod(binary_path, st.st_mode | stat.S_IEXEC)

# Create unity environment
env = UnityEnvironment(file_name=binary_path,
                       worker_id=0,
                       base_port=portpicker.pick_unused_port(),
                       docker_training=True,
                       )
brain_name = env.brain_names[0]

# Do initial reset
env_info = env.reset(train_mode=True)[brain_name]
obs = env_info.visual_observations[0][0]

# Forever
while True:
    # Step environment with random action
    env_info = env.step([random.randint(1, 4)])[brain_name]
    obs = env_info.visual_observations[0][0]
    reward = env_info.rewards[0]
    done = env_info.local_done[0]

    print('step!')

    if done:
        # Reset if the episode is done
        env_info = env.reset(train_mode=True)[brain_name]
        obs = env_info.visual_observations[0][0]
