import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"检测到 {len(gpus)} 个 GPU：", gpus)
else:
    print("没有检测到可用 GPU！")
