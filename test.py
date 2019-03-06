import os
import stat

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
                       )
brain_name = env.brain_names[0]

env_info = env.reset(train_mode=True)
obs = env_info.visual_observations[0]

print(obs)
