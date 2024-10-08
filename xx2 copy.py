# 使用python画一个折线图
import matplotlib.pyplot as plt

# 定义x轴和y轴的数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 绘制折线图
plt.plot(x, y)

# 添加标题和坐标轴标签
plt.title('Multi_image_infer')
# 设置x只为整数
plt.xticks(x)
plt.xlabel('photo_num')
plt.ylabel('infer_time')

# 显示图形
plt.show()
# 保存图形
plt.savefig('fibonacci_sequence.png')