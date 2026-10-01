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

Both agents will be implemented for the same game environment and evaluated through a series of matches.

The goal is to determine which agent performs better and explore **why their performance differs** and how factors such as search depth, computational budget, and decision time affect their behavior.

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
│   └── game.py
├── tournament/
│   └── tournament.py
├── results/
├── docs/
│   └── research.md
└── README.md
```

> The project structure is preliminary and may change during development.

---

## Team Roles

These are proposed responsibilities for a four-person team. Members can choose roles after the game and shared interface are agreed upon.

| Member | Main responsibility | Deliverables |
| --- | --- | --- |
| AJ | Game environment | Implement the rules, legal moves, win/draw detection, and a shared interface both agents can use. |
| Brady | Alpha-Beta agent | Implement Minimax with alpha-beta pruning, an evaluation function, and adjustable search depth. |
| Member 3 | MCTS agent | Implement selection, expansion, simulation, and backpropagation with an adjustable simulation budget. |
| Member 4 | Tournament and analysis | Implement match scheduling, a Random baseline, result collection, and comparisons of win rate and decision time. |

Everyone will test their own part, review at least one teammate's work, and help write the final findings and presentation. The group can adjust the split after choosing a game to keep the workload balanced.

---

## 🚧 Project Status

**Current Stage:** 🔎 Research & Planning

- [x] Select project topic
- [ ] Research Alpha-Beta Pruning
- [ ] Research Monte Carlo Tree Search
- [x] Select game environment
- [ ] Design game architecture
- [ ] Implement baseline agent
- [ ] Implement Alpha-Beta agent
- [ ] Implement MCTS agent
- [ ] Build tournament system
- [ ] Run experiments
- [ ] Analyze results
- [ ] Document findings

---

## 📚 Research & References

Research papers, tutorials, implementations, and other resources used while developing the project will be documented here as the project progresses.

---

## 💡 About This Project

This project is being developed as an exploration of **artificial intelligence, adversarial search, and game-playing algorithms**.

The repository will evolve as research is completed and design decisions are made.

---

### 🚀 More coming soon!

Currently researching the algorithms and designing the initial game environment.
