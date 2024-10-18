import numpy as np
import matplotlib.pyplot as plt
import os

class Maze:
    def __init__(self, width=7, height=10):
        self.width = width
        self.height = height
        self.start = (8, 1)  # 7x10の迷路に合わせて開始位置を調整
        self.goal = (1, 4)  # ゴールも調整
        self.maze = self._generate_maze(width, height)
        self.current = self.start

        # 描画のための初期設定
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.set_xticks(np.arange(self.width))
        self.ax.set_yticks(np.arange(self.height))
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.grid(which='both')

    def _generate_maze(self, width, height):
        maze = np.ones((height, width))
        # for i in range(size):  # 外周も含めて全てのセルに対して
        #     for j in range(size):
        #         maze[i][j] = np.random.choice([0, 1], p=[0.7, 0.3])  # 70% の確率で通路, 30% の確率で壁
        
        maze[1][2]=0
        maze[1][3]=0
        maze[1][4]=0

      
        maze[2][2]=0
        maze[1][3]=0
        maze[2][4]=0
        maze[1][5]=1
        maze[1][6]=1
     
    
        maze[3][2]=0
        maze[2][3]=1
        maze[3][4]=0
        maze[2][5]=1
        maze[2][6]=1
       
        maze[4][2]=0
        maze[3][3]=1
        maze[4][4]=0
        maze[3][5]=1
        maze[3][6]=1
       
 
        maze[5][2]=0
        maze[5][4]=0
        maze[6][2]=0
        maze[6][3]=0
        maze[6][4]=0
        maze[6][5]=1
        maze[7][4]=0
        maze[8][1]=1
        maze[8][2]=0
        maze[8][3]=0
        maze[8][4]=0
        maze[self.start] = 0
        maze[self.goal] = 0
        return maze


    def reset(self):
        self.current = self.start
        return self.current

    def step(self, action):
        next_x, next_y = self.current
        if action == 0:  # 上
            next_x = max(0, self.current[0]-1)
        elif action == 1:  # 右
            next_y = min(self.width-1, self.current[1]+1)
        elif action == 2:  # 下
            next_x = min(self.height-1, self.current[0]+1)
        elif action == 3:  # 左
            next_y = max(0, self.current[1]-1)

        if self.maze[next_x][next_y] == 0:  # 移動可能な場所なら移動
            self.current = (next_x, next_y)

        # ゴールとの距離を計算
        distance_to_goal = np.sqrt((self.current[0] - self.goal[0]) ** 2 + (self.current[1] - self.goal[1]) ** 2)
        reward = 1.0 / (1.0 + distance_to_goal)  # ゴールに近づくほど報酬が増える

        # ゴールに到達したかどうかをチェック
        if self.current == self.goal:
            return self.current, reward, True  # ゴールに到達
        return self.current, reward, False  # まだゴールに到達していない


    def render(self, agent_position):
        self.ax.clear()
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_xticks(np.arange(self.width))
        self.ax.set_yticks(np.arange(self.height))
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.grid(which='both')

        for i in range(self.height):
            for j in range(self.width):
                color = 'black' if self.maze[i][j] == 1 else 'lightgray'  # 壁のセルは黒く表示
                self.ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))

                # 開始とゴールの位置を描画
                if (i, j) == self.start:
                    self.ax.text(j + 0.5, i + 0.5, 'S', ha='center', va='center', color='green')
                elif (i, j) == self.goal:
                    self.ax.text(j + 0.5, i + 0.5, 'G', ha='center', va='center', color='red')

        # エージェントの位置を描画
        self.ax.text(agent_position[1] + 0.5, agent_position[0] + 0.5, 'A', ha='center', va='center', color='blue', fontsize=12)
        plt.savefig(f'{name}/meiro.png')
        plt.pause(0.1)


class ProfitSharingAgent:
    def __init__(self, num_actions, learning_rate=0.1, discount_factor=0.9):
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.values = {}  # 状態とアクションの組み合わせの価値を保存する辞書
        self.memory = []  # アクションの履歴を保存

    def get_action(self, state):
        # 探索 vs 活用 (ここではランダムにアクションを選択します)
        if np.random.rand() < 0.1:  # 20% の確率でランダムに行動
            return np.random.choice(self.num_actions)
        values = [self.values.get((state, a), 0.0) for a in range(self.num_actions)]
        return np.argmax(values)

    def remember(self, state, action, reward):
        self.memory.append((state, action, reward))

    def learn(self):
        G = 0
        for state, action, reward in reversed(self.memory):
            G = reward + self.discount_factor * G
            value = self.values.get((state, action), 0.0)
            self.values[(state, action)] = value + self.learning_rate * (G - value)
        self.memory = [] # メモリをリセット

# 学習とテストのコード
if __name__ == "__main__":
    maze = Maze()
    agent = ProfitSharingAgent(num_actions=4)
  
    from datetime import datetime
    # 現在の時刻を取得
    current_time = datetime.now()
    name = f'{current_time}'
    flag=0
    # 保存するディレクトリを作成
    if not os.path.exists(name):
        os.makedirs(name)

    # ファイルのパスを指定
    file_path = os.path.join(name, "maze_steps_actions_rewards.txt")
     # ファイル名を指定
    
    with open(file_path, "a") as file:
        # もし新規ファイルの場合はヘッダーを書き込む
        if file.tell() == 0:  # ファイルが空ならヘッダーを書き込む
            file.write("Episode, Step, Action, Reward, Done\n")
        num_episodes = 10000
        steps_per_episode = []  # エピソードごとのステップ数を記録するリスト
        for episode in range(num_episodes):
            state = maze.reset()
            done = False
            step=0
            while not done:
                action = agent.get_action(state)
                
                next_state, reward, done = maze.step(action)
                file.write(f"{episode}, {step}, {action}, {reward}, {done}\n")
                agent.remember(state, action, reward)
                state = next_state
                if flag==0:
                    maze.render(state)  # 各ステップごとに状態を表示
                    flag += 1
                step = step+1
                

            
            steps_per_episode.append(step)  # エピソードごとのステップ数を記録
            print(step)
            agent.learn()  # エピソード終了後に学習
            print(f"Episode {episode} finished")
            plt.close(maze.fig)

# ステップ数のグラフを作成
plt.figure()
plt.plot(range(num_episodes), steps_per_episode, marker='o')
plt.xlabel('Episode')
plt.ylabel('Steps')

plt.title('Steps per Episode')
plt.grid(True)
plt.savefig(f'{name}/step.png')

