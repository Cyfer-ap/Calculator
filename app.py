import gradio as gr

def calculator(num1, operator, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Invalid input. Please enter numbers."

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

# Define the interface components
num1_input = gr.Textbox(label="Number 1")
operator_input = gr.Dropdown(['+', '-', '*', '/'], label="Operator")
num2_input = gr.Textbox(label="Number 2")

output = gr.Textbox(label="Result")

# Create the Gradio interface
iface = gr.Interface(
    fn=calculator,
    inputs=[num1_input, operator_input, num2_input],
    outputs=output,
    title="Simple Calculator",
    description="Enter two numbers and select an operator."
)

iface.launch()
