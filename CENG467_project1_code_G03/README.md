## File Descriptions (Feel free to fill in the STUBs to gain more GitHub readME creation experience!)

### `main.py`

Parses dataset, method, model, temperature and max_token_limit. Sets up output files, loads model and dataset, imports INSTRUCTION from CoMAT_Instruction, calls process_mmlu_redux_questions function from mmlu_redux.py.

### `mmlu_redux.py`

Processes MMLU-Redux dataset questions, evaluates model responses and extracts final answers from model outputs.

### `shapley_value_evaluation.py`

Implements Shapley value calculations to evaluate the importance of each individual step in CoMAT.

### `utils.py`

Contains the predict_model() function which applies predictions and returns the model response, and the model_evaluation() function that calls predict_model().

### `grpo_finetune.py`

Implements GRPO finetuning with a reward function that returns 1.0 or 0.0 for each completion. Also includes preprocess_function that creates the prompt with comat instruction, question and options. And finally includes the generate_and_save function that implements the result generation and saves the outputs.

### `CoMAT_Instruction.py`

Assigns the prompt-instruction to the INSTRUCTION variable.

