## Reinforcement Learning

### Markov Decision Process

- Markovian property: Only present matter. Current state everything you need to remember from the past. 
- Stationary: Rules don't change. (Transition function doesn't change)
- Policy defines a solution to Markov Decision process, it takes in a state and output an action. It tells in this particular state, 
what action should you take. 
- Policy is different from "the idea of what actions to take in the next 20 steps", it's more like "whatever steps I happen to 
be in, what's the next best thing I can do.". And just always ask that question. The first notion just depends on where you started, 
while the second one, each action is depending on separate state. 
- What's makes MDP problem and reinforcement learning problem different from supervised learning problem?
    - Delayed reward. (You don't know what the immediate action is going to lead the thing down the road; You don't know which 
    action leads to the ultimate winning or losing)
        - In supervised learning problem setting, you're learning: given the state i'm in, and given the proper action I should take, 
        learning a function that maps from state to action. 
        - But in reinforcement learning case, say if we're in some state, you're given a series of (state, action, reward) triplets,
        and ultimately we have to figure out in a given state, which action should take in order to get the ultimate reward. 
        - This is called the temporal **Credit Assignment Problem**. 
- Reward is your domain knowledge. 
- Policy is affected by how many steps left you can take. 
- Discounted reward allows us to go infinite distance in finite time. (computer design faster and faster (infinite amount of)computer in finite time.)
- Reward of a state is different from the utility of the state. Reward->immediate feedback. Utility->Long term benefit. 
- Value iteration and policy iteration to solev bellman equation. 


### Reinforcement Learning

- Q Learning: Evaluating the bellman equation from data. That's we taking states, actions get rewards, then the next state. And we are trying to learn a Q function for it. 
- Q function: Utility function by taking a certain action. 
- When estimating Q function, we don't have access to reward and transition funciton. All we have is transition. 
- In RL, it's fundenmental to think of the exploration and exploitation dilemma. You have to utilize the things you know, and you also have to explore new data. It's a fundenmental trade off. 


### Game theory

- Definition: Mathmatics of conflict. 
- Goes from single agent to multiple agents. 
- Minimax and Maximin problem. 
- Pure strategy vs mixed strategy. 
- Nash Equilbrium: A strategy is in Nash Equilbrim if other players have no reason to change their strategy even if they are given the chance to do so. m


## Deep Learning

### Deep Neural Network

- Cross-entropy: If we have a bunch of events, and a bunch of probabilities. How likely that the events happen based on the probabilities. If it's very likely, then we have a small cross-entropy. 

- L1 regularization is good for feature selection because it prefers sparse features; while L2 regularization often produces good result, and its features are homogeneously small. 
