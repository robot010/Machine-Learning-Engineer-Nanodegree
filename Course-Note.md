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
- 
