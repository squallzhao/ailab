正态分布（Normal distribution），也称“常态分布”，又名高斯分布（Gaussian distribution）

tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
	Args:	
		shape: A 1-D integer Tensor or Python array. The shape of the output tensor.用一个list表示产出的Tensor的形状
		mean: A 0-D Tensor or Python value of type dtype. The mean of the normal distribution.均值
		stddev: A 0-D Tensor or Python value of type dtype. The standard deviation of the normal distribution.标准差
		dtype: The type of the output.数据类型
		seed: A Python integer. Used to create a random seed for the distribution. See set_random_seed for behavior.
		name: A name for the operation (optional).
	Returns:
		A tensor of the specified shape filled with random normal values.
