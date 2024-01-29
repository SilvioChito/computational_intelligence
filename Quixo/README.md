try_first => [1, 378, 39, 0.5948568911764831, 348] lr = 0.001 o 0.0001 non ricordo...
try_second => 


# Deep Reinforcement Learning implementation of Quixo
versione del Game: commit 0edba49 modificata per essere row-column

## Introduction
Quixo is a two-player abstract strategy board game where players take turns shifting rows or columns in an attempt to align five of their pieces in a row. In this project, we explore the implementation of Deep Reinforcement Learning (DRL) techniques to develop an AI agent capable of playing Quixo.

## Deep Reinforcement Learning
In our Deep Reinforcement Learning (DRL) approach for Quixo, we rely on the concept of modeling a Q-function through a neural network. The essence of our methodology lies in the representation of the game state and the subsequent decision-making process orchestrated by this function. Specifically, we employ two separate models: one designated for the agent playing first and the other for the agent playing second. This deliberate separation stems from our observation that attempting to encapsulate all possible game configurations within a single model tends to result in suboptimal generalization.

Our algorithm is structured around the interaction between an agent (a neural network utilized for training) and the environment  (which is represented by the game board). At its core, our agent's learning process involves iteratively updating its neural network parameters based on the rewards received and the states resulting from its actions. These states are characterized by the actions taken by both our training agent and its opponent, with the latter's behavior potentially varying depending on the specific opponent model employed (the next state in which we fall is conditioned on the opponent's move).

During the training phase, our agent engages in matches against a randomly behaving opponent. Through these encounters, it learns to navigate the complexities of Quixo gameplay, gradually improving its strategy through reinforcement learning. By updating its neural network parameters in response to the observed rewards and state transitions, the agent refines its decision-making capabilities, ultimately aiming to outperform its adversaries in diverse game scenarios.

Inside our Algorithm we make use of another neural network called TargetNet (some model for making prediction), which is utilized to stabilize the training process by providing a fixed target for computing the loss function. This network is periodically updated to mirror the current parameters of the main neural network, ensuring a more consistent learning signal. Additionally, the replay buffer stores past experiences (state-action-reward transitions) and samples them randomly during training. This technique improves sample efficiency and reduces the correlation between consecutive experiences, leading to more stable and effective learning

(Talk about rewards ?)

## GA to support DRL
In our implementation, we extend the application of the Genetic Algorithm (GA) to address the hyperparameter selection process for both versions of the Quixo model, each specialized for different starting turns. This extension involves running the GA independently for each model's turn version, allowing us to tailor the hyperparameters to the specific requirements and dynamics associated with starting either first or second.

Similar to the previous description, for each turn version of the model, we generate a population of individuals, with each individual representing a unique configuration of hyperparameters. The hyperparameters considered include:

num_matches: Number of matches.
max_dim_replay_buff: Maximum dimension of the replay buffer.
time_to_update: Time interval for updating the neural network.
gamma: Discount factor.
batch_size: Size of the training batch.

We enforce constraints on the values of these hyperparameters to ensure they fall within predefined ranges, as specified by cell_max_values.

The fitness function for each individual is evaluated based on the accuracy achieved by training the corresponding model with the specified hyperparameters. By optimizing for accuracy, the GA aims to identify hyperparameter configurations that result in superior performance for each turn version of the Quixo model.

Given the computational demands of the problem, we maintain the limitation of 20 generations per turn version. However, the flexibility exists to adjust this parameter based on available computational resources, allowing for more extensive exploration of the hyperparameter space if desired. This approach ensures that each model's turn version is equipped with hyperparameters optimized for its specific gameplay dynamics and strategic considerations.

Note: For each best solution (one for the models that starts first and one for the one that starts second), we then try different learning rates (in the GA we used 0.0001 as default one => check better...)

... add numeric results for both best solutions

## Random Opponent vs QuixoNet / QuixoNet vs QuixoNet
In our experimentation with opponent training strategies, we initially pitted our Quixo agent against a random opponent. This served as a foundational training phase, allowing the agent to learn fundamental strategies and adapt to diverse game states. Once we achieved satisfactory performance with the trained models for both starting turns, we explored further training methodologies to enhance the agent's capabilities.

To capitalize on the acquired knowledge and refine the agent's strategies, we conducted additional training sessions where the trained agent for one starting turn (e.g., the first turn) competed against the agent specialized for the opposite starting turn (e.g., the second turn). During this training process, we kept the parameters of the opponent agent frozen to maintain consistency. This iterative training approach aimed to leverage the strengths and weaknesses of each agent to foster mutual improvement.

Following this training iteration, we evaluated the performance of the trained models by having them play against each other. Despite the expectation of observing improvements resulting from the iterative training process, our analysis revealed no discernible signs of enhancement in gameplay quality or strategic acumen.

Consequently, we concluded that the training against a random opponent sufficed in providing the necessary learning experiences for our Quixo agent. As such, we retained the model trained solely against the random opponent, as it demonstrated comparable or superior performance without the added complexity and computational burden associated with further training iterations against specialized opponents.

This decision underscores the importance of carefully evaluating training strategies and considering the trade-offs between complexity, computational resources, and performance gains in reinforcement learning tasks. By leveraging insights gained from our experimentation, we refined our approach to focus on training against a random opponent as the most effective strategy for developing a robust and adaptable Quixo agent.


In our final assessment, we achieved significant success with our Quixo agent, reaching an accuracy rate of 87% with the trained model


## How is the code structured

hyperparams_selection_genetic.ipynb => used in order to generate the hyperparameters of the network
training_phase.ipynb => used in order to train an agent
testing_phase.ipynb => used in order to test the trained agent.
trained_models => here you could find the model parameters to feed into the Training_Complete structure along with a boolean value that specifies wether the model starts as first or second. The structure provides a function that let modify this value in order to start as second
game.py => defines the Game, Player and QuixoNet (the NN used inside the Player)
