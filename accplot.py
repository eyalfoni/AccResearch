import json
import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

data = json.loads(open('malone_test_data.txt', 'r').read())['motion_data']
matrix = []

for x in range(0, len(data)):
    sub_list = [k for k in data[x]['acc'].values()]
    # print sub_list
    matrix.append(sub_list)

# print matrix
df = pd.DataFrame(matrix, columns=list('xyz'))
print df


"""
temp = data['motion_data'][0]['acc']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
Axes3D.scatter(temp['x'], temp['y'], zs=temp['z'])
"""
