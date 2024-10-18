
### ファイル説明
- `profit_sharing.py`: Profit Sharingアルゴリズムのメインロジック。エージェントが環境と相互作用し、行動価値を更新する。
- `environment.py`: エージェントが学習するためのシンプルな環境を定義。例えば、グリッドワールドなどの環境を用意。

### 主要なメソッド
- `select_action(state)`: 現在の状態に基づいて次に取るべき行動を選択します。
- `update_values(state, action, reward)`: 得られた報酬に基づいて行動価値を更新します。

## 実行方法

Profit Sharingアルゴリズムを実行するための手順は以下の通りです：

### 必要なツール
- Python 3.x
- 必要なパッケージは`requirements.txt`に記載されています

### 手順
1. リポジトリをクローンします：
    ```bash
    git clone https://github.com/yourusername/profit_sharing_rl.git
    cd profit_sharing_rl
    ```

2. 必要なライブラリをインストールします：
    ```bash
    pip install -r requirements.txt
    ```

3. Profit Sharingアルゴリズムを実行します：
    ```bash
    python src/profit_sharing.py
    ```

4. 結果は`results/sample_results.csv`に出力され、エージェントの学習履歴を確認できます。

## サンプル結果

以下は、Profit Sharingアルゴリズムを用いた学習のサンプル結果です。学習が進むにつれ、エージェントは環境の報酬構造に適応し、徐々に最適な行動を選択するようになります。

| エピソード | 累積報酬 |
|------------|----------|
| 1          | 15       |
| 10         | 50       |
| 100        | 200      |
| 1000       | 450      |

これらの結果は、`results/sample_results.csv`に保存され、詳細な解析が可能です。

## ライセンス
このプロジェクトはMITライセンスのもとでライセンスされています。詳細は`LICENSE`ファイルを参照してください。
