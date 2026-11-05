# 🎮 Game-Playing AI Agent
### Alpha-Beta Pruning vs. Monte Carlo Tree Search

An artificial intelligence project exploring and comparing two approaches to adversarial game playing: **Alpha-Beta Pruning** and **Monte Carlo Tree Search (MCTS)**.

The agents will eventually compete against one another in a tournament-style evaluation to compare their performance, efficiency, and decision-making.

---

## 📌 Project Overview

Game-playing has played an important role in the development of artificial intelligence because games provide controlled environments for studying search, planning, and decision-making.

This project will explore two different approaches to game-playing AI:

- 🌳 **Alpha-Beta Pruning**
- 🎲 **Monte Carlo Tree Search (MCTS)**

Both agents will use a shared **Connect Four environment written in Python** and will be evaluated through a series of matches.

The goal is to determine which agent performs better and explore **why their performance differs** and how factors such as search depth, computational budget, and decision time affect their behavior.

---

## 🎮 Game Environment

The complete game environment is available on the [game-environment branch](https://github.com/alexanderjames5684-web/alpha-beta-mcts/tree/game-environment). It has not yet been merged into `main`, which still contains the horizontal-win checkpoint version.

### Implemented features

- Standard 6 × 7 board with gravity and alternating turns.
- Move validation for invalid inputs and full columns.
- Horizontal, vertical, and both diagonal wins.
- Draw detection and rejection of moves after the game ends.
- Independent board copies for search through `clone()`.
- ASCII opening title and bordered terminal board.
- Seven automated tests covering all 69 winning lines for both players, draw detection, move validation, copying, and 100 simulated games.

### Run locally

From an existing repository clone with your local work saved:

```bash
git switch game-environment
git pull
python game/game.py
```

Enter a column from **1–7**, or `q` to quit. The environment requires Python 3 with no third-party packages.

Run the tests from the repository root:

```bash
python -m unittest -v test_game
```

### Shared interface

| Method | Behavior |
| --- | --- |
| `legal_moves()` | Available columns 0–6, or an empty list when the game ends |
| `apply_move(column)` | Updates the board and switches players after a valid move |
| `get_winner()` | Returns 1 or 2 for a win, 0 for a draw, or None while ongoing |
| `is_terminal()` | Reports whether the game has ended |
| `is_draw()` | Reports a full board without a winner |
| `clone()` | Copies the board and current player independently |

Agent moves use **0–6** internally. The terminal translates human inputs **1–7**.
See the [environment guide](https://github.com/alexanderjames5684-web/alpha-beta-mcts/blob/game-environment/game/README.md) for examples and conventions.

---

## 🤖 Planned Agents

### 🌳 Alpha-Beta Agent

The Alpha-Beta agent will use adversarial search to evaluate possible future game states.

Alpha-Beta pruning improves traditional Minimax search by eliminating branches of the game tree that do not need to be evaluated.

**Planned concepts:**

- Minimax search
- Alpha-Beta pruning
- Evaluation functions
- Search depth
- Game-tree exploration

### 🎲 Monte Carlo Tree Search Agent

The MCTS agent will approach decision-making through repeated simulations rather than exploring the game tree in the same way as Alpha-Beta.

The algorithm generally follows four stages:

**Selection → Expansion → Simulation → Backpropagation**

**Planned concepts:**

- Tree search
- Random simulations
- Exploration vs. exploitation
- Simulation budgets
- Statistical decision-making

### 🎯 Baseline Agent

A simple baseline agent may also be implemented to provide a reference point for evaluating the more advanced agents.

A **Random Agent** is currently planned as the baseline.

---

## 🏆 Tournament Evaluation

Once the agents are implemented, they will compete in a tournament consisting of repeated games.

Possible matchups include:

| Matchup |
| --- |
| Alpha-Beta vs. MCTS |
| Alpha-Beta vs. Random |
| MCTS vs. Random |

Potential evaluation metrics include:

- 🏆 Win rate
- 🤝 Draw rate
- ⏱️ Average decision time
- 🔍 Search effort
- 🌳 Nodes explored
- 🎲 Number of MCTS simulations

The tournament will allow the algorithms to be compared under controlled conditions.

---

## 🔬 Possible Research Questions

Some questions that may be explored throughout the project include:

- How does Alpha-Beta search depth affect playing strength?
- How does the number of MCTS simulations affect playing strength?
- Which algorithm performs better when computational resources are limited?
- How does decision time differ between Alpha-Beta and MCTS?
- How consistently does each agent perform across repeated games?

These questions may change as the project develops.

---

## 🛠️ Planned Project Structure

```text
alpha-beta-mcts/
├── agents/
│   ├── alpha_beta.py
│   ├── mcts.py
│   └── random_agent.py
├── game/
│   ├── game.py
│   └── README.md
├── tournament/
│   └── tournament.py
├── results/
├── docs/
│   └── research.md
├── test_game.py
└── README.md
```

> This is the target structure. The `game/` guide and `test_game.py` are available on `game-environment`. Agent, tournament, results, and research paths are planned.

---

## Team Roles

The four team members own the following project components.

| Member | Main responsibility | Deliverables |
| --- | --- | --- |
| AJ | Game environment | Implement the rules, legal moves, win/draw detection, and a shared interface both agents can use. |
| Brady | Alpha-Beta agent | Implement Minimax with alpha-beta pruning, an evaluation function, and adjustable search depth. |
| Spencer | MCTS agent | Implement selection, expansion, simulation, and backpropagation with an adjustable simulation budget. |
| Matthew | Tournament and analysis | Implement match scheduling, a Random baseline, result collection, and comparisons of win rate and decision time. |

Everyone will test their own part, review at least one teammate's work, and help write the final findings and presentation. The group can adjust the split as integration progresses to keep the workload balanced.

---

## 🚧 Project Status

**Current Stage:** Game environment complete on its development branch. Agent implementation and tournament integration remain planned.

**Progress updated:** November 5, 2026

- [x] Select project topic
- [x] Research Alpha-Beta Pruning
- [ ] Research Monte Carlo Tree Search
- [x] Select game environment
- [x] Design game architecture
- [x] Implement and test complete Connect Four rules on `game-environment`
- [x] Add the shared game-state interface and terminal display
- [ ] Merge the completed environment into `main`
- [ ] Implement baseline agent
- [ ] Implement Alpha-Beta agent
- [ ] Implement MCTS agent
- [ ] Build tournament system
- [ ] Run experiments
- [ ] Analyze results
- [ ] Document findings

---

## 💡 About This Project

This project is being developed as an exploration of **artificial intelligence, adversarial search, and game-playing algorithms**.

The repository will evolve as research is completed and design decisions are made.

---

