import tensorflow as tf

# 检查可用的物理设备
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print("Physical Devices: ", tf.config.list_physical_devices())
