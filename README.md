# CoMAT Mathematical Reasoning Reproduction

A reproduction and experimental evaluation of **CoMAT-style mathematical reasoning** using Qwen language models on the **MMLU-Redux College Mathematics** benchmark.

This project investigates how model choice, sampling parameters, generation length, GRPO fine-tuning, and reasoning-step importance affect mathematical reasoning performance.

The project was developed as part of **CENG 467 — Natural Language Processing** at İzmir Institute of Technology.

---

## Overview

Large language models can generate detailed reasoning traces for mathematical problems, but their performance can vary considerably depending on the underlying model and inference configuration.

This project explores structured mathematical reasoning using a CoMAT-style prompting approach.

The experiments include:

- mathematical reasoning with Qwen language models
- comparison of Qwen2 and Qwen3
- temperature experiments
- maximum generation-length experiments
- evaluation on MMLU-Redux
- GRPO fine-tuning
- reasoning-step analysis
- Shapley-value-based reasoning-step importance estimation

The project focuses not only on whether the final answer is correct, but also on how different reasoning configurations influence model behavior.

---

## Dataset

The experiments use the **College Mathematics** subset of **MMLU-Redux**.

The repository contains the dataset used in the experiments:

```text
CENG467_project1_code_G03/
└── mmlu-redux-college_mathematics_dataset.csv
```

Each example contains a multiple-choice mathematics problem.

The problem and answer choices are combined with a structured CoMAT-style instruction and passed to the selected Qwen model.

The generated response is then processed to extract the final predicted answer and compare it with the reference answer.

---

## Method

The main evaluation workflow can be summarized as:

```text
MMLU-Redux Question
        │
        ▼
CoMAT-Style Instruction
        │
        ▼
Qwen Language Model
        │
        ▼
Generated Reasoning
        │
        ▼
Final Answer Extraction
        │
        ▼
Evaluation
```

The same general pipeline is used to compare different models and generation configurations.

---

## Models

The main evaluation code supports two Qwen models:

- **Qwen2-1.5B-Instruct**
- **Qwen3-1.7B**

The experiments compare the effect of:

- model generation
- temperature
- maximum token limit

on mathematical reasoning accuracy.

---

## Experimental Results

Several combinations of model, temperature, and maximum token length were evaluated.

| Model | Temperature | Maximum Tokens | Accuracy |
|---|---:|---:|---:|
| Qwen2 | 0.1 | 2000 | 23.23% |
| Qwen2 | 0.7 | 2000 | 22.22% |
| Qwen3 | 0.1 | 2000 | 40.40% |
| Qwen3 | 0.1 | 4000 | **69.70%** |

Among these evaluated configurations, the strongest result was obtained using:

```text
Model: Qwen3
Temperature: 0.1
Maximum Tokens: 4000
Accuracy: 69.70%
```

---

## Observations

### Model Choice

Qwen3 achieved substantially higher accuracy than the evaluated Qwen2 configurations.

The strongest Qwen2 experiment achieved:

```text
23.23%
```

while the strongest evaluated Qwen3 configuration achieved:

```text
69.70%
```

### Generation Length

Increasing the maximum generation length for the evaluated Qwen3 configuration from `2000` to `4000` tokens increased accuracy from:

```text
40.40%
```

to:

```text
69.70%
```

This suggests that allowing a larger reasoning budget can have an important effect on mathematical reasoning performance for the evaluated setup.

### Temperature

For the evaluated Qwen2 experiments, changing the temperature from `0.1` to `0.7` produced relatively similar results:

```text
Temperature 0.1 → 23.23%
Temperature 0.7 → 22.22%
```

Within these experiments, temperature had a considerably smaller effect than changing the model or increasing the available generation length.

---

## GRPO Fine-Tuning

The project also investigates **Group Relative Policy Optimization (GRPO)** as a reinforcement-learning-based fine-tuning strategy.

The GRPO workflow is implemented in:

```text
CENG467_project1_code_G03/grpo_finetune.py
```

The training pipeline constructs prompts containing:

- the CoMAT-style reasoning instruction
- the mathematical question
- the available answer choices

The reward function evaluates the correctness of generated completions.

A correct answer receives a positive reward, while an incorrect answer receives no reward.

The repository contains outputs for:

```text
Qwen2-0.5B Base
Qwen2-0.5B GRPO Fine-Tuned
```

These outputs allow the behavior of the base and fine-tuned models to be compared.

The corresponding results are stored under:

```text
CENG467_project1_code_G03/Q4_results/
```

---

## Reasoning-Step Analysis

Final-answer accuracy alone does not provide information about which parts of a reasoning trace contribute most strongly to the result.

For this reason, the project also investigates individual reasoning steps.

Generated reasoning traces are divided into separate steps and evaluated using **Shapley values**.

The general idea is:

```text
Generated Reasoning
        │
        ▼
Individual Reasoning Steps
        │
        ▼
Step Combination / Removal
        │
        ▼
Model Evaluation
        │
        ▼
Shapley Value Estimation
        │
        ▼
Reasoning-Step Importance
```

This analysis provides an additional perspective on model reasoning by estimating the contribution of individual steps.

The implementation is contained in:

```text
CENG467_project1_code_G03/shapley_value_evaluation.py
```

and related evaluation data is stored in:

```text
CENG467_project1_code_G03/evaluation_with_steps.csv
```

---

## Code Components

The implementation is contained inside:

```text
CENG467_project1_code_G03/
```

### `main.py`

Main entry point for the model evaluation experiments.

It handles command-line parameters including:

- dataset
- reasoning method
- model
- temperature
- maximum token limit

It loads the selected Qwen model, processes the MMLU-Redux dataset, and stores the generated outputs and evaluation results.

---

### `mmlu_redux.py`

Processes the MMLU-Redux dataset.

Its responsibilities include:

- iterating over mathematics questions
- generating model responses
- extracting final answers
- evaluating predictions
- calculating accuracy

---

### `CoMAT_Instruction.py`

Contains the structured prompt instruction used to guide the model through the CoMAT-style mathematical reasoning process.

---

### `utils.py`

Contains utility functions used during model inference and evaluation.

---

### `grpo_finetune.py`

Implements the GRPO fine-tuning workflow.

It includes functionality for:

- prompt preprocessing
- reward calculation
- model fine-tuning
- text generation
- result storage

---

### `shapley_value_evaluation.py`

Implements reasoning-step importance analysis using Shapley values.

---

### `MMLU-Redux-college_mathematics_prompts/`

Contains prompt-related materials used for the College Mathematics experiments.

---

### `Q2_results/`

Contains model-comparison experiments involving Qwen2 and Qwen3 under different inference configurations.

---

### `Q4_results/`

Contains outputs related to the GRPO experiments, including base and fine-tuned model outputs.

---

## Repository Structure

```text
comat-math-reasoning-reproduction/
│
├── CENG467_project1_code_G03/
│   │
│   ├── CoMAT_Instruction.py
│   ├── main.py
│   ├── mmlu_redux.py
│   ├── utils.py
│   ├── grpo_finetune.py
│   ├── shapley_value_evaluation.py
│   │
│   ├── mmlu-redux-college_mathematics_dataset.csv
│   ├── evaluation_with_steps.csv
│   │
│   ├── MMLU-Redux-college_mathematics_prompts/
│   │
│   ├── Q2_results/
│   │   ├── Q2b_qwen2_temp01/
│   │   ├── Q2c_qwen2_temp07/
│   │   ├── Q2f_qwen3_token2000/
│   │   └── Q2g_qwen3_token4000/
│   │
│   ├── Q4_results/
│   │
│   └── README.md
│
├── CENG467_project1_report_G03.pdf
│
└── README.md
```

---

## Running the Main Evaluation

Clone the repository:

```bash
git clone https://github.com/behicekadioglu/comat-math-reasoning-reproduction.git
```

Enter the project directory:

```bash
cd comat-math-reasoning-reproduction/CENG467_project1_code_G03
```

The main evaluation script supports the following arguments:

```text
--dataset
--method
--model
--temperature
--max_token_limit
```

The supported model options are:

```text
qwen2
qwen3
```

For example, the Qwen3 experiment using a temperature of `0.1` and a maximum token limit of `4000` can be run with:

```bash
python main.py \
  --dataset mmlu-redux-college_mathematics \
  --method comat \
  --model qwen3 \
  --temperature 0.1 \
  --max_token_limit 4000
```

The script automatically selects CUDA when a compatible GPU is available and otherwise falls back to CPU.

Generated outputs are written to experiment-specific result directories.

---

## Main Libraries

The project uses Python and several machine learning and NLP libraries, including:

- PyTorch
- Hugging Face Transformers
- Pandas
- python-dotenv

Additional libraries are used by the GRPO fine-tuning workflow and evaluation scripts.

---

## Technologies & Concepts

### Natural Language Processing

- Large Language Models
- Mathematical Reasoning
- Prompt Engineering
- Structured Reasoning

### Models

- Qwen2
- Qwen3
- Transformer-based Language Models

### Reinforcement Learning

- Group Relative Policy Optimization
- Reward-Based Fine-Tuning

### Evaluation

- MMLU-Redux
- Accuracy
- Reasoning-Step Analysis
- Shapley Values

### Development

- Python
- PyTorch
- Hugging Face Transformers

---

## Project Report

A detailed academic report describing the experiments, methodology, and results is included in the repository:

[`CENG467_project1_report_G03.pdf`](./CENG467_project1_report_G03.pdf)

---

## Academic Context

This project was developed for **CENG 467 — Natural Language Processing** at **İzmir Institute of Technology**.

The objective was to reproduce and experimentally investigate ideas related to structured mathematical reasoning with large language models.

This repository represents an **academic reproduction and experimental study**.

It does not claim authorship of the original CoMAT method, MMLU-Redux dataset, Qwen models, or other referenced research contributions.

---

## Collaboration

This project was completed collaboratively by:

- **Behice Kadıoğlu**
- **Zeynep Naz Ödenir**

The implementation, experimentation, analysis, and project report were completed as part of the group coursework.

---

## Authors

### Behice Kadıoğlu

Computer Engineering  
İzmir Institute of Technology

GitHub: [@behicekadioglu](https://github.com/behicekadioglu)

### Zeynep Naz Ödenir

Project collaborator

---

## Disclaimer

This repository is an academic reproduction and experimentation project.

The original methods, datasets, model architectures, and referenced research belong to their respective authors and organizations.
