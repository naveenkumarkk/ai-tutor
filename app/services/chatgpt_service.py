import requests
import os
from services.conversation_service import update_conversation_status, save_assistant_message, save_conversation_state, get_conversation_state


url = os.getenv('ENDPOINT_URL', 'https://tu-openai-api-management.azure-api.net/nail-projects/openai/deployments/gpt-4o-nail/chat/completions')
querystring = {"api-version": os.getenv('CHAT_GPT_API_VERSION', '2024-08-01-preview')}


def get_chatgpt_response(user_message, conversation_type, conversation_id, user_id):
    try:
        if not user_message or user_message.strip() == "":
            return generate_initial_message(conversation_type, conversation_id, user_id)


        if any(keyword in user_message.lower() for keyword in ["finished", "completed", "done"]):
            update_conversation_status(conversation_id, 'completed')
            return handle_completion_message(conversation_type)


        conversation_state = get_conversation_state(conversation_id)
        system_content = {
            "planning": (
                "You are an AI tutor focused on improving students' self-regulated learning."
               "Guide students through structured learning stages: Planning > Sub-goals > Resources > Timeline > Obstacles > Rephrasing."
                "For each stage:"
                "1. Adjust responses based on the student's confidence level (Positive, Neutral, Negative)."
                "2. Use concise, supportive, and encouraging language."
                "3. Avoid overwhelming students with lengthy or overly detailed responses."
                "4. Always elicit the student's input and adapt based on their progress.."
            ),
            "monitoring": (
                "You are an AI tutor helping students monitor their progress and stay motivated. Ask reflective questions to assess progress, "
                "encourage adjustments, and provide guidance to stay on track."
            ),
            "reflecting": (
                "You are an AI tutor guiding students through self-reflection to improve performance. Focus on analyzing actions and outcomes "
                "and help students learn from their experiences."
            )
        }.get(conversation_type, "You are an AI tutor here to help students achieve their learning goals.")


        parameters = {
            "planning": {
                "goal_clarification": {
                "positive": {
                    "response": "That’s a clear and actionable goal! How do you plan to break this down into smaller steps?",
                    "examples": [
                    {
                        "student": "I want to fully understand the concept of probability distributions and complete three practice problems.",
                        "ai_response": "That’s a clear and actionable goal! How do you plan to break this down? For example, will you start with theory, examples, or practice problems?"
                    }
                    ]
                },
                "neutral": {
                    "response": "Making progress is a good start! What topic interests you the most right now and feels like a good starting point?",
                    "examples": [
                    {
                        "student": "I think my goal is to make some progress on learning about machine learning algorithms, but I’m not sure how far I’ll get.",
                        "ai_response": "Making progress is a good start! What topic interests you the most right now and feels like a good starting point? Or is there a concept that’s been confusing you for a while that we could tackle together?"
                    }
                    ]
                },
                "negative": {
                    "response": "That’s completely okay—feeling stuck is part of the process! Let’s start small: Is there a topic that interests you or one that’s been on your mind recently?",
                    "examples": [
                    {
                        "student": "I don’t really know; I feel stuck and unsure of what to focus on.",
                        "ai_response": "That’s completely okay—feeling stuck is part of the process! Let’s start small: Is there a topic that interests you or one that’s been on your mind recently? Maybe something you’ve been confused about for a while?"
                    }
                    ]
                }
                },
                "sub_goals": {
                "positive": {
                    "response": "Great! What step will you focus on first?",
                    "examples": [
                    {
                        "student": "Yes! Step one is reading the material, step two is summarizing the key points, and step three is practicing a few examples.",
                        "ai_response": "That’s a great breakdown! What step will you focus on first?"
                    }
                    ]
                },
                "neutral_negative": {
                    "response": "That’s okay—we can figure it out together. What’s the first thing you need to do to get started?",
                    "examples": [
                    {
                        "student": "I think I could break it into steps, but I’d need help to figure out what they are.",
                        "ai_response": "That’s okay—we can figure it out together. Think about the goal you want to achieve. What’s the first thing you need to do to get started?"
                    }
                    ]
                }
                },
                "resources": {
                "positive": {
                    "response": "That’s a great selection of resources! Do you already have everything ready, or is there anything else you need to gather?",
                    "examples": [
                    {
                        "student": "I’ll use my lecture notes, the textbook, and some practice problems from the course website.",
                        "ai_response": "That’s a great selection of resources! Do you already have everything organized, or do you need to gather anything before starting?"
                    }
                    ]
                },
                "neutral": {
                    "response": "That sounds like a good starting point! Do you want to check if it covers what you need?",
                    "examples": [
                    {
                        "student": "I think I have a video bookmarked somewhere that might help.",
                        "ai_response": "That sounds like a good starting point! Do you want to take a moment to check if the video covers what you need, or do you need help finding additional resources?"
                    }
                    ]
                },
                "negative": {
                    "response": "That’s okay—we can figure this out together. What type of resource do you find most helpful—videos, textbooks, or practice tools?",
                    "examples": [
                    {
                        "student": "I don’t have any resources ready, and I’m not sure where to look.",
                        "ai_response": "That’s okay—we can figure this out together. What type of resource do you find most helpful—videos, textbooks, or interactive tools? I can suggest a few starting points if you’d like."
                    }
                    ]
                }
                },
                "timeline": {
                "positive": {
                    "response": "That’s a solid plan! Do you think that time is enough to cover everything, or would you leave room for review later?",
                    "examples": [
                    {
                        "student": "I’ll spend an hour on it today and reevaluate if I need more time later.",
                        "ai_response": "That’s a solid plan! Do you think that time is enough to cover everything, or would you leave room for review later?"
                    }
                    ]
                },
                "neutral": {
                    "response": "That’s a great start. Let’s see how far you get in that time—if needed, you can always add more later.",
                    "examples": [
                    {
                        "student": "I think I’ll work on it for 30 minutes and see how far I get.",
                        "ai_response": "That’s a great start. Let’s see how far you get in that time—if needed, you can always add more later."
                    }
                    ]
                },
                "negative": {
                    "response": "That’s okay—how about setting a timer for 15 minutes to see how it feels? Once you get started, it might feel easier to continue.",
                    "examples": [
                    {
                        "student": "I don’t know. I’m not sure how long it will take or if I’ll even start.",
                        "ai_response": "That’s okay—how about setting a timer for 15 minutes to see how it feels? Once you get started, it might feel easier to continue."
                    }
                    ]
                }
                },
                "obstacles": {
                "positive": {
                    "response": "That’s great! Since you’ve done this before, what strategies worked well last time that you can use again?",
                    "examples": [
                    {
                        "student": "Yes, I’ve practiced similar problems before and felt confident doing them.",
                        "ai_response": "That’s great! Since you’ve done this before, what strategies worked well last time that you can use again?"
                    }
                    ]
                },
                "neutral": {
                    "response": "That’s a good starting point! What do you remember about the process that might help you this time?",
                    "examples": [
                    {
                        "student": "I’ve done something like this before, but I don’t remember it well.",
                        "ai_response": "That’s a good starting point! What do you remember about the process that might help you this time?"
                    }
                    ]
                },
                "negative": {
                    "response": "That’s okay! Starting something for the first time can feel hard, but we can take it step by step. What challenges might you face, and how could you overcome them?",
                    "examples": [
                    {
                        "student": "No, this is my first time, and I’m worried it might be too hard.",
                        "ai_response": "That’s okay! Starting something for the first time can feel hard, but we can take it step by step. What challenges might you face, and how could you overcome them?"
                    }
                    ]
                }
                },
                "rephrasing": {
                "positive": {
                    "response": "That sounds great! If you feel ready to finish the planning stage and move to the monitoring phase, let me know!",
                    "examples": [
                    {
                        "student": "Instead of ‘learn derivatives,’ I’ll aim to ‘understand differentiation rules and solve five problems.’",
                        "ai_response": "That sounds great! If you feel ready to finish the planning stage and move to the monitoring phase, let me know!"
                    }
                    ]
                }
                }
            }
            }




        phase_prompts = {
            "planning": [
                "What is your main learning goal for today?",
                "Can you divide your goal into 2–3 smaller steps to focus on?",
                "What step will you focus on first?",
                "What resources or tools will help you with this task?",
                "Do you need to find or prepare anything before starting?",
                "How much time do you plan to spend on this task?",
                "Does this timeline feel realistic to you?",
                "What challenges might you face, and how could you overcome them?",
                "Have you done something like this before? What worked well last time?",
                "Can you rephrase your goal to make it clearer or more actionable?"
            ],
           "monitoring": [
                "What task are you currently working on?",
                "How much of it have you completed so far?",
                "Is this progress faster or slower than you expected?",
                "What’s slowing you down—distracting thoughts, unclear material, or something else?",
                "Are you pleased with your achievement? Would you like a little break?",
                "What part of the material is most challenging right now?",
                "Have you tried reviewing it again or using another resource?",
                "What specific questions or concepts are unclear to you?",
                "How focused do you feel right now on a scale of 1 to 5?",
                "Do you need a break or a change in your approach?",
                "What’s distracting you the most right now?",
                "What strategy are you using to learn this material?",
                "Is it working as well as you hoped?",
                "Would you like to try a different method, such as summarizing or testing yourself?",
                "How much time have you spent on this task today?",
                "Is that more or less than you planned?",
                "Do you need to adjust your time allocation for the rest of the day?",
                "How confident are you in your understanding of the material so far?",
                "If not confident, which parts feel shaky?",
                "What could help you feel more prepared?",
                "What’s motivating you to complete this task right now?",
                "Is that motivation helping you stay focused?",
                "What could make this task feel more rewarding?"
            ],
            "reflecting": [
                "What task did you recently complete?",
                "Why do you think this task was successful, or what could have been improved?",
                "What strategies or resources were most helpful for this task?",
                "Were there any challenges you faced, and how did you overcome them?",
                "What did you learn from this experience that you can apply to future tasks?",
                "Is there anything you would do differently next time?",
                "How did this task contribute to your overall goals?",
                "What feedback or results did you receive, and how do they align with your expectations?",
                "How do you feel about your performance, and why?",
                "What is one key takeaway from this task?"
            ]
        }.get(conversation_type, [])


        if "current_prompt_index" not in conversation_state:
            conversation_state["current_prompt_index"] = 0


        current_index = conversation_state["current_prompt_index"]
        if current_index >= len(phase_prompts):
            update_conversation_status(conversation_id, 'completed')
            return "You have completed this phase. Let me know if you'd like to move to the next one!"


        next_prompt = phase_prompts[current_index]
        conversation_state["current_prompt_index"] += 1
        save_conversation_state(conversation_id, conversation_state, user_id, conversation_type)


        response_content = tailor_response_to_confidence(user_message, next_prompt, parameters, conversation_type)


        payload = {
                "messages": [
                    {"role": "system", "content": f"{system_content} Ask One question at a time"},
                    {"role": "user", "content": user_message},
                    {"role": "assistant", "content": response_content}
                ],
                "max_tokens": 500,
                "temperature": 0.7
            }


        headers = {
                "Content-Type": "application/json",
                "api-key": os.getenv("CHAT_GPT_API_KEY", '8c5567ebd69347cc8092ea4c55efeec9')
            }


        response = requests.post(url, json=payload, headers=headers, params=querystring)
        response.raise_for_status()
        chatgpt_response = response.json()
        assistant_reply = chatgpt_response.get("choices", [{}])[0].get("message", {}).get("content", "")
        save_assistant_message(conversation_id, user_id, assistant_reply)
        return assistant_reply


    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")


def tailor_response_to_confidence(user_message, next_prompt, parameters, conversation_type):
    """
    Tailors the AI's response based on the user's confidence level in their response.
    """
    positive_indicators = ["I am confident", "I know", "I’m sure", "I understand"]
    neutral_indicators = ["I’m not sure", "I think", "Maybe", "Possibly"]
    negative_indicators = ["I’m stuck", "I don’t know", "I’m confused", "I’m unsure"]


    if any(indicator in user_message for indicator in positive_indicators):
        return parameters[conversation_type]["goal_clarification"]["positive"]["response"]
    elif any(indicator in user_message for indicator in neutral_indicators):
        return parameters[conversation_type]["goal_clarification"]["neutral"]["response"]
    elif any(indicator in user_message for indicator in negative_indicators):
        return parameters[conversation_type]["goal_clarification"]["negative"]["response"]
    else:
        return "Let’s start small and work through it together."




def handle_completion_message(conversation_type):
    """
    Handles the message when a phase is completed.
    """
    messages = {
        "planning": "Great job on completing your planning phase! Now, let's move on to the monitoring phase.",
        "monitoring": "Well done on completing your monitoring phase! Let's move on to the reflecting phase.",
        "reflecting": (
            "Fantastic! You've completed the reflecting phase and learned from your experiences. "
            "Now, it's time to apply these insights to your next plan."
        )
    }
    return messages.get(conversation_type, "Congratulations on completing this phase!")


def generate_initial_message(conversation_type, conversation_id, user_id):
    """
    Generates the first introductory message based on the conversation type.
    """
    initial_messages = {
        "planning": (
            "Welcome to the planning phase! Let's get started. "
            "What task do you want to plan for? Try breaking it into smaller steps, setting priorities, and deadlines. "
            "How can I assist you in creating your study plan?"
        ),
        "monitoring": (
            "Welcome to the monitoring phase! I'm here to help you track your progress. "
            "On which task are you currently working? How is your progress compared to your plan?"
        ),
        "reflecting": (
            "Welcome to the reflecting phase! Let's analyze what worked and what didn't. "
            "What task did you recently complete? Why do you think it was successful, or what could have been improved?"
        )
    }


    initial_message = initial_messages.get(conversation_type, "Welcome! I'm your AI tutor here to assist with your study goals. How can I help you get started?")


    save_assistant_message(conversation_id, user_id, initial_message)


    return initial_message

