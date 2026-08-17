"""

Group 3:
Behice Kadıoğlu - 300201123
Zeynep Naz Ödenir - 300201091

"""

def predict_model(model, tokenizer, messages, configuration=None):
    ######################################
    ### STUB: INSERT THE CODE HERE###
    ######################################

    # apply_chat_template function used to fit the format qwen needs.
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    # Tokenize the input and move model to device.
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    
    # Model generates output, according to temperature and max_token_limit.
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=configuration["max_token_limit"],
        temperature=configuration["temperature"],
        do_sample=True if configuration["temperature"] > 0 else False
    )
    
    # Extract only the generated new tokens(output).
    generated_ids = [
        output_ids[len(input_ids):] 
        for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    
    # Return response (extracted output) as text.
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response
    
    # commented this out to avoid error during execution
    # raise NotImplementedError("Build the Transformers package operations here based on the configurations given in the assignment")
    """
    This function, `predict_model`, is designed to interact with QWEN models to generate predictions
    based on a conversation history. 

    Args:
        model: The pre-trained language model to be used for generating responses.
        tokenizer: the tokenizer corresponding to the model.
        messages: A list of dictionaries representing the conversation history,
                  where each dictionary has a "role" (e.g., "system", "user", or "assistant") 
                  and "content" (the message text).
        configuration: initially, the model used should be max_token_limit of 2000, with temperature of 0.1
        The assessment would mainly be assessed the correctness of the implementation, rather than the performance

    Returns:
        The model's response as a string.
    """

def model_evaluation(model_type, model, tokenizer, system_content, question, formatted_options, configuration=None):
    if model_type == "qwen2" or model_type == "qwen3":
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"Question: {question}\n\nOptions:\n{formatted_options}"}
        ]
        model_result = predict_model(model, tokenizer, messages, configuration)
    else: 
        raise ValueError(f"Unknown model_type: {model_type}")

    #  print(f"Model result: {model_result}")
    return model_result
