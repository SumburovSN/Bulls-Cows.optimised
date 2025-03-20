Rules of the game Bulls and Cows. 
Each player guesses a 4-digit number made up of different digits. Opponents try to guess their opponent's number by offering a 4-digit number, which must also consist of different digits. 
If a digit in the proposed number matches the guessed number but does not match the place, it is called a cow. If the digit matches the place, it is a bull. For example, the guessed number is 1234, and the proposed number is 1043. 
Therefore, the answer is 1 bull 2 ​​cows. Whoever guesses faster wins.

The game is launched via main.py. 
The course of the game is regulated by BullsCows.py through mutual questions and answers. For convenience and to avoid errors in preparing the answer, the number guessed by the player is saved by the program. 
Questions and answers are generated in CompPlayer.py for the player, who is a computer, and in UserPlayer.py for the user. 
The algorithm for finding the answer is written in DecisionMaker.py. 
Phrase.py offers translation of all phrases in 4 languages. 
Colors.py makes it easy to output messages in the console in different colors.

Analyser.py and GuessSelector.py are designed to study the speedup of answer search after 1 question-answer series.

Explanation of the answer search algorithm in DecisionMaker.py. 
The algorithm must find a number from all possible combinations, which we will call the search field. Initially, the search field includes 5040 numbers (arrangement of 4 elements out of 10). 
Any number from the initial search field splits the search field into several buckets depending on the answer to this number. 
There are 14 such outcomes in total, and they are specified in the possible_answers_set = [0, 1, 2, 3, 4, 10, 11, 12, 13, 20, 21, 22, 30, 40] field of the DecisionMaker class. 
For example, any number splits the initial search field into 14 buckets (Analyzer.get_example_initial_distribution(guess_example)): 
[[1, 1440], [2, 1260], [11, 720], [10, 480], [0, 360], [3, 264], [12, 216], [20, 180], [21, 72], [30, 24], [4, 9], [13, 8], [22, 6], [40, 1]], i.e. the answer 1 cow corresponds to 1440 numbers, and for example the answer 2 bulls 2 cows (22) is suitable for 6 numbers. 
After each question-answer pair, the search field narrows (DecisionMaker: narrow_decisions_field()). 
The task of the DecisionMaker algorithm is to make this path shorter. To do this:
The remaining search field is checked against the number from the original field and it is calculated how many numbers fall into a particular bucket with a certain answer (DecisionMaker: get_baskets_amounts()). The resulting array is sorted in reverse order.
The resulting distribution must be compared with the remaining numbers to select a shallower distribution: the minimum of the buckets with the maximum number (DecisionMaker: get_all_baskets_amounts()).
DecisionMaker: get_shallowest_baskets() selects the distribution with the minimum number of possible answers in the buckets (optimal distribution).
DecisionMaker: get_optimal_list() returns an array of numbers with the optimal distribution.
The answer is chosen randomly from the array with the optimal distribution, with the exception of the second question.
To find the second question, optimization is applied, calculated using Analyzer.build_first_level_optimization(). 

Finding an answer with a large search field takes a long time, but after the first answer it is enough to apply the data from the optimization. 
For example, after the answer 1 cow it is enough to select a basket with the outcome 1 (1 cow) from the initial distribution. 

PS 
Perhaps there is some other optimization after the second answer. I tried to find it in Analyzer.build_second_level_optimization(), but it is in development.
