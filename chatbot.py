import pandas as pd

faq_list = pd.read_csv('faq.csv');

while True:
    # USer ask questions
    print('Ask me any question')
    user_question = input('You: ')
    if user_question.lower() == 'bye':
        print("Bot: Goodbye! Have a great day.")
        break

    # Search qns
    matched_row = faq_list[faq_list['question'].str.lower().str.contains(user_question.lower())]
    if not matched_row.empty:
        print("Bot:", matched_row.iloc[0]['answer'])
    else:
        print("Bot: Sorry, I don't know that yet.")
        user_choice = input("Do you help me to know the answer? (y/n): ")
        if user_choice.lower() == 'y':
            new_answer = input("Please enter the answer:")
            new_row = pd.DataFrame({"question":[user_question],"answer":[new_answer] })
            faq_list = pd.concat([faq_list, new_row], ignore_index=True)
            new_row.to_csv('faq.csv', mode='a', header=False, index=False)
            print("Bot: Thanks! I've learned something new. 😊")

