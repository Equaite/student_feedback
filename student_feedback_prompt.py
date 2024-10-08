import json

if __name__ == "__main__":

    student_feedback_extract_prompt = """
    You will be given a Question, Mark Scheme, Student Answer and a Graded Answer on that answer.
    The Graded Answer has feedback for how a student can improve their answer.
    Your task is to reorientate and expand the Graded Answer to make the student the subject for the advice, you speak in a straightforward, clear and supportive way to the student and offer them specific advice on how their answer can be improved to achieve full marks.

    Here are guidelines to follow:
    1. The advice you give to improve the Student Answer must be consistent with the advice in the Graded Answer.
    2. Illustrate any advice given to the student with examples. These examples should be what the student wrote in their answer. If the example earns low marks, refine it to be worthy of higher marks.
    3. Speak in second or third person, do not speak in first person.
    4. You are speaking to high-school students, avoid using complicated vocabulary that students may find difficult to understand.

    Below are examples to guide you:

    Question:
    The Alliance System was the main cause of the First World War.' How far do you agree with this statement? Explain your answer.

    Mark Scheme:
    Level_4:\n  description: \n    - Complex explanation of stated factor and other factor(s) leading to a sustained judgement\n    - Answer demonstrates a range of accurate and detailed knowledge and understanding that is relevant to the question\n    - Answer demonstrates a complex, sustained line of reasoning which has a sharply-focused coherence and logical structure that is fully substantiated, with well-judged relevance.\n    - Extends Level 3.\n  marks_awarded:\n    maximum: 16\n    minimum: 12\n  criteria:\n    - Complex explanation of stated factor and other factor(s)\n    - Accurate and detailed knowledge and understanding\n    - Complex, sustained line of reasoning with coherence and logical structure\n  progression:\n    - Students may progress from a developed explanation of causation by complex explanation of the relationship between causes supported by detailed factual knowledge and understanding to form a sustained judgement.\n  example_answer:\n    - ‘the Alliance system was one of the long term causes of the war in the wider context of European rivalry over empires. It did not in itself make war inevitable, but it created a framework for conflict. This was triggered in the short-term by the Austrian ultimatum to Serbia in 1914.’\n\nLevel_3:\n  description: \n    - Developed explanation of the stated factor and other factor(s)\n    - Answer demonstrates a range of accurate knowledge and understanding that is relevant to the question\n    - Answer demonstrates a developed, sustained line of reasoning which has coherence and logical structure; it is well substantiated, and with sustained, explicit relevance.\n    - Extends level 2 \n    - Answer may suggest that one reason has greater merit.\n  marks_awarded:\n    maximum: 12\n    minimum: 9\n  criteria:\n    - Developed explanation of the stated factor and other factor(s)\n    - Accurate knowledge and understanding\n    - Developed, sustained line of reasoning with coherence and logical structure\n  progression:\n    - Students may progress from a simple explanation of causation with developed reasoning supported by factual knowledge and understanding.\n  example_answer:\n    - “explaining the motives and rivalries that led to the Triple Alliance and the Triple Entente. This system resulted in Europe being divided into opposing armed camps and resulted in Germany worrying about ‘encirclement’.”\n\nLevel_2:\n  description: \n    - Simple explanation of stated factor or other factor(s)\n    - Answer demonstrates specific knowledge and understanding that is relevant to the question\n    - Answer demonstrates a simple, sustained line of reasoning which is coherent, structured, substantiated and explicitly relevant.\n    - Answers arguing a preference for one judgement but with only basic explanation of another view will be marked at this level.\n  marks_awarded:\n    maximum: 8\n    minimum: 5\n  criteria:\n    - Simple explanation of stated factor or other factor(s)\n    - Specific knowledge and understanding\n    - Simple, sustained line of reasoning with coherence and structure\n  progression:\n    - Students may progress from a basic explanation of causation by simple reasoning and supporting it with factual knowledge and understanding.\n  example_answer:\n    - ‘the main reason a war broke out was the rivalry that had been developing between Britain and Germany over the size of their empires and their armed forces. Both countries felt threatened by the development of the other and wanted an opportunity to show their superiority by winning a war.’\n\nLevel_1:\n  description: \n    - Basic explanation of one or more factors\n    - Answer demonstrates basic knowledge and understanding that is relevant to the question\n    - Answer demonstrates a basic line of reasoning, which is coherent, structured with some substantiation; the relevance might be implicit.\n  marks_awarded:\n    maximum: 4\n    minimum: 1\n  criteria:\n    - Basic explanation of one or more factors\n    - Basic knowledge and understanding\n    - Basic line of reasoning with coherence and structure\n  progression:\n    - Students recognise and provide a basic explanation of one or more factors.\n  example_answer:\n    - Students may offer a basic explanation of the stated factor, such as, the Alliance system brought all the European powers into a war together. They had promised to support each other if a war broke out.\n    - Students may offer basic explanations of other factor(s), for example, the assassination of Archduke Franz Ferdinand caused Austria to declare war and this became a World War.\n\nLevel_0:\n  description: \n    - Students either submit no evidence or fail to address the question\n  marks_awarded:\n    maximum: 0\n    minimum: 0\n  criteria:\n    - No evidence or fail to address the question\n  progression:\n    - N/A\n  example_answer:\n    - N/A

    Student Answer:
    I agree to some extent that the alliance system was the main cause of WW1. The 'Alliance system' was a factor in the causes of WW1 because, for example, Austria-Hungary had annexed Bosnia so Serbia was unhappy. Serbia had then got Russia involved which left Austria getting Germany's help because they had signed the 'blank cheque'. Another example was the failure of the Schlieffen plan as Britain and France were an alliance and they had step foot in Belgium (Britain and Belgium signed a treaty). In conclusion I agree to a certain extent that the alliance system was the main cause that that had led to WWI.

    Graded Answer:
    The student provides a basic explanation of the alliance system and its role in the causes of WW1. They mention the involvement of Austria-Hungary, Serbia, Russia, and Germany, as well as the failure of the Schlieffen Plan and the involvement of Britain and Belgium. However, the explanation lacks depth and detailed factual knowledge. The student does not fully develop their reasoning or provide a sustained line of argument.\n\nThe answer demonstrates basic knowledge and understanding of the alliance system and its impact on the outbreak of WW1. The line of reasoning is coherent but not well-developed or substantiated. The conclusion is brief and does not add much to the overall argument.\n\nTo reach a higher level, the student would need to provide a more detailed and developed explanation of the alliance system and other factors that contributed to the outbreak of WW1. They should also aim to create a more sustained and coherent line of reasoning, supported by accurate and detailed factual knowledge.\n\nOverall, the answer falls into Level 1 and should be awarded 4 marks.

    Student Feedback:
    You've made a good start by acknowledging the role of the alliance system, and it's clear that you have some understanding of how different nations were involved. Here are specific ways you can improve your response to achieve higher marks:
    1. **Deepen Your Explanation of the Alliance System**: You mentioned that the alliance system was a factor in the causes of WWI, but it's important to elaborate on how it functioned. For instance, you could explain that the alliance system created a network of treaties that turned a local conflict into a larger war. Try mentioning how the Triple Alliance (Germany, Austria-Hungary, and Italy) and the Triple Entente (Britain, France, and Russia) were designed to provide mutual defense and how this heightened tensions. This added detail shows a deeper understanding of the alliances' implications.
    2. **Provide More Detailed Factual Knowledge**: While you discuss the involvement of Austria-Hungary, Serbia, and Russia, try to enhance your argument with specific details. For example, you noted that Russia supported Serbia after Austria-Hungary annexed Bosnia. You could mention how this annexation caused unrest in the Balkans and how nationalist sentiments were further fueled, leading to the assassination of Archduke Franz Ferdinand. Including these details would strengthen your argument significantly and demonstrate your knowledge.
    3. **Develop Your Reasoning and Structure**: You have a coherent line of reasoning, but it could be more sustained and persuasive. Instead of stating, "I agree to some extent," you could clarify whether you believe the alliance system was the primary cause or if other factors were equally important. For example, you might say, "While the alliance system contributed significantly to the outbreak of WWI by creating divided camps, factors such as nationalism and imperialism also played crucial roles." This type of reasoning will help you form a more complex judgment.
    4. **Expand Your Conclusion**: Your conclusion is brief and doesn't add much depth to your argument. Instead of simply restating your opinion, summarize your main points more comprehensively and reinforce why the alliance system was significant in your analysis. You might say, "In conclusion, although the alliance system was a crucial factor leading to WWI by entangling nations in mutual defense obligations, it's important to recognize that other elements such as rising nationalism, imperial competition, and militarism also significantly contributed to the war's outbreak." This gives the reader a clearer sense of your overall argument.
    5. **Use Clear Examples to Illustrate Points**: When discussing the Schlieffen Plan, consider elaborating on why it failed and its impact. You mentioned that "the failure of the Schlieffen Plan" occurred, but you could specify how this plan intended to quickly knock out France to avoid fighting a two-front war, leading to Germany’s inability to mobilize effectively and further entrenching Britain and France as allies against them.
    By implementing these strategies, you'll enhance your answer by demonstrating a more complex understanding of the various causes of World War I, which is crucial for reaching the higher levels of the mark scheme. Keep up the hard work!

    Question:
    {question_text}

    Mark Scheme:
    {mark_scheme_text}

    Student Answer:
    {answer_text}

    Graded Answer:
    {llm_graded_answer}

    Student Feedback:
    """.strip()

    prompt_dict = {"prompt": student_feedback_extract_prompt}

    # Serializing json
    json_object = json.dumps(prompt_dict, indent=4)
    
    # Writing to sample.json
    with open("student_feedback_prompt.json", "w") as outfile:
        outfile.write(json_object)
