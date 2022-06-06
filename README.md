# Car-Trajactory-Simulator

## Usage:
`python main.py input_file output_directory`
You can press `SPACE` to pause excusion in any time.

## Map:
There are trajectories with 4, 16, 24 coflict zones in `myMap`, which you don't need to import them by yourself. You are welcome to use your customized map if you want.

#### There are some parameters in `Class Map` that you may want to define:
- `x <int>`: the width of the map grid
- `y <int>`: the height of the map grid
-  `path <list>`: the list of trajectories coordinates
-  `zone_list <list>`: the list of conflict zone coordinates
-  `tunnel_list <list>`: the list of "tunnels", [p1 = (x1, y1), p2 = (x2, y2)] establishs a tunnel when p1 and p2 are not adjent coordinates but cars can moves from p1 to p2 or from p2 to p1.

All adject coordinates would be seen that cars can come and go.

#### There is an example for map16:

<img width="579" alt="截圖 2022-06-07 04 31 54" src="https://user-images.githubusercontent.com/45334378/172243813-91282e88-f6a7-4f8b-86c2-97274363a73a.png">

```python=
class Map:
    def __init__(self):
        
        self.x = 5
        self.y = 5

        ### DEFINE TRAJECTORIES ###
        self.path = [ [(6, 2), (5, 2), (4, 2), (3, 2), (2, 3), (2, 4), (2, 5), (2, 6)] ]

        self.zone_list = [        (1, 0),         (3, 0),
                          (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                                  (1, 2),         (3, 2),
                          (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
                                  (1, 4),         (3, 4)         ]
        
        self.tunnel_list = [    [(1, 0), (0, 1)], [(3, 0), (4, 1)], [(0, 3), (1, 4)], [(3, 4), (4, 3)],
                                [(2, 1), (1, 2)], [(2, 3), (1, 2)], [(2, 1), (3, 2)], [(3, 2), (2, 3)]  ]
```

For defined map4, map16, map24, You can only adjust your own `path` in `Map`.

## Input:
You will need to input your driving situation as `input_file`. There are some input examples in `src`.

After you define your trajectories, you need to define your cars in your input_file.
The first line of input_file, should be the name of your map_file, like `map4`, `map16`, `map24`.
The second line of input_file should be a integer `N`, which means the count of cars.
Then, there should have N lines, represent `path_type`, `depart_time` of each car.

For example, for an input_file like:
```
map4
2
0 0
1 2
```
That means there are 2 cars driving in map4. 
The first car driving in trajectory 1 (`path[0]` in `Map`), and it apears at time 0.
The second car driving in trajectory 2 (`path[1]` in `Map`), and it apears at time 2.

## Scheduler:
Now, all cars would move simply when their target zone is empty. Therefore, deadlock my happend in this simulator.

If you want, you can change the strategy defined at `scheduler.py`.

## Output:
You will get pictures about the result in each unit of time. All pictures will be saved in `output_directory` that you input.

---

## Execusion with map4, map16, map24:
<img width="800" alt="截圖 2022-05-31 04 23 48" src="https://user-images.githubusercontent.com/45334378/171055713-dad7b5d5-9df0-4234-8213-0d319f162b2d.png">

<img width="801" alt="截圖 2022-05-31 04 24 06" src="https://user-images.githubusercontent.com/45334378/171055791-0aacdebe-6df2-4eb0-9a98-82159c1700ed.png">

<img width="800" alt="截圖 2022-05-31 04 24 23" src="https://user-images.githubusercontent.com/45334378/171056021-373c176b-244e-4c27-ab59-de94824b0901.png">

